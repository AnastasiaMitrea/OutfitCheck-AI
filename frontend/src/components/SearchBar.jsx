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
            // FIX: Use includes instead of strict equality for partial tag matching
            return keywords.every(kw => 
                item.tags.some(tag => tag.label.toLowerCase().includes(kw))
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
