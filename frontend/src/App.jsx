import React, { useState, useEffect } from 'react';
import VirtualCloset from './components/VirtualCloset';
import OutfitCanvas from './components/OutfitCanvas';
import SearchBar from './components/SearchBar';

function App() {
  const [clothes, setClothes] = useState([]);
  const [filteredClothes, setFilteredClothes] = useState([]);

  // Sync filtered clothes when clothes change
  useEffect(() => {
    setFilteredClothes(clothes);
  }, [clothes]);

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <header className="mb-8">
        <h1 className="text-4xl font-extrabold text-gray-900">AI Virtual Wardrobe</h1>
        <p className="text-gray-600">Manage your clothes and get style advice</p>
      </header>
      
      <main>
        <SearchBar clothes={clothes} setFilteredClothes={setFilteredClothes} />
        {/* Pass filteredClothes to VirtualCloset to display only search results */}
        <VirtualCloset clothes={filteredClothes} setClothes={setClothes} />
        <OutfitCanvas availableClothes={clothes} />
      </main>
    </div>
  );
}

export default App;
