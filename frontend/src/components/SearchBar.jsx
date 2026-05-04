import React, { useState } from 'react';

export default function SearchBar({ clothes, setFilteredClothes }) {
    const [query, setQuery] = useState('');

    const handleSearch = (e) => {
        const text = e.target.value.toLowerCase();
        setQuery(text);

        if (!text) {
            setFilteredClothes(clothes);
            return;
        }

        const keywords = text.split(' ');

        const filtered = clothes.filter(item => {
            // BUG INTRODUCED INTENTIONALLY FOR PHASE 5 (Simulated Bug)
            // Or I can introduce it here, or later.
            // Wait, "Phase 5: Simulate a bug in 'image filtering', create a fix..."
            // Let's introduce a bug here:
            return keywords.every(kw => 
                item.tags.some(tag => tag.label.toLowerCase() === kw) // strict equality instead of includes
            );
        });

        setFilteredClothes(filtered);
    };

    return (
        <div className="mb-6">
            <input 
                type="text" 
                value={query}
                onChange={handleSearch}
                placeholder="Search wardrobe (e.g., 'black elegant dress')" 
                className="w-full p-3 border rounded shadow-sm"
            />
        </div>
    );
}
