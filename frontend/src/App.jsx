import React, { useState } from 'react';
import VirtualCloset from './components/VirtualCloset';
import OutfitCanvas from './components/OutfitCanvas';

function App() {
  const [clothes, setClothes] = useState([]);

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <header className="mb-8">
        <h1 className="text-4xl font-extrabold text-gray-900">AI Virtual Wardrobe</h1>
        <p className="text-gray-600">Manage your clothes and get style advice</p>
      </header>
      
      <main>
        <VirtualCloset clothes={clothes} setClothes={setClothes} />
        <OutfitCanvas availableClothes={clothes} />
      </main>
    </div>
  );
}

export default App;
