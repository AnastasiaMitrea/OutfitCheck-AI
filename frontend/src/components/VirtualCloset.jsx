import React, { useState } from 'react';
import AIAutoCategorizer from '../services/ai';

export default function VirtualCloset({ clothes, setClothes }) {
    const [isAnalyzing, setIsAnalyzing] = useState(false);

    const handleFileUpload = async (event) => {
        const file = event.target.files[0];
        if (!file) return;

        const imageUrl = URL.createObjectURL(file);
        
        setIsAnalyzing(true);
        try {
            const tags = await AIAutoCategorizer.categorizeItem(imageUrl);
            
            const newItem = {
                id: Date.now(),
                imageUrl,
                tags
            };

            setClothes(prev => [...prev, newItem]);
        } catch (error) {
            console.error("AI Error:", error);
            setClothes(prev => [...prev, {
                id: Date.now(),
                imageUrl,
                tags: [{label: 'unknown clothing', confidence: 1.0}]
            }]);
        } finally {
            setIsAnalyzing(false);
        }
    };

    const deleteItem = (id) => {
        setClothes(prev => prev.filter(item => item.id !== id));
    };

    return (
        <div className="p-4">
            <h2 className="text-2xl font-bold mb-4">My Virtual Closet</h2>
            
            <div className="mb-6">
                <input 
                    type="file" 
                    accept="image/*" 
                    onChange={handleFileUpload} 
                    className="block w-full text-sm text-gray-500
                    file:mr-4 file:py-2 file:px-4
                    file:rounded-full file:border-0
                    file:text-sm file:font-semibold
                    file:bg-violet-50 file:text-violet-700
                    hover:file:bg-violet-100"
                />
                {isAnalyzing && <p className="mt-2 text-sm text-blue-600">AI is analyzing your item...</p>}
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {clothes && clothes.map(item => (
                    <div key={item.id} className="border rounded-lg overflow-hidden shadow-sm">
                        <img src={item.imageUrl} alt="Clothing item" className="w-full h-48 object-cover" />
                        <div className="p-3">
                            <h3 className="font-semibold text-lg mb-2">AI Tags:</h3>
                            <ul className="text-sm text-gray-600 mb-3">
                                {item.tags.map((tag, idx) => (
                                    <li key={idx}>- {tag.label} ({Math.round(tag.confidence * 100)}%)</li>
                                ))}
                            </ul>
                            <button 
                                onClick={() => deleteItem(item.id)}
                                className="w-full bg-red-500 text-white py-1 rounded hover:bg-red-600"
                            >
                                Delete
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
