import React, { useState } from 'react';
import AIFashionCritic from '../services/aiCritic';

export default function OutfitCanvas({ availableClothes }) {
    const [selectedItems, setSelectedItems] = useState([]);
    const [favorites, setFavorites] = useState([]);
    const [feedback, setFeedback] = useState(null);
    const [isEvaluating, setIsEvaluating] = useState(false);

    const toggleItem = (item) => {
        if (selectedItems.find(i => i.id === item.id)) {
            setSelectedItems(prev => prev.filter(i => i.id !== item.id));
        } else {
            setSelectedItems(prev => [...prev, item]);
        }
        setFeedback(null); // Reset feedback when outfit changes
    };

    const evaluateOutfit = async () => {
        if (selectedItems.length < 2) {
            alert("Please select at least 2 items to evaluate.");
            return;
        }

        setIsEvaluating(true);
        try {
            const result = await AIFashionCritic.evaluateOutfit(selectedItems);
            setFeedback(result);
        } catch (error) {
            console.error("Critic Error:", error);
            setFeedback({ feedback: "Looks like a great outfit! (AI Offline fallback)", score: 100 });
        } finally {
            setIsEvaluating(false);
        }
    };

    const saveFavorite = () => {
        if (selectedItems.length === 0) return;
        const newFavorite = {
            id: Date.now(),
            items: [...selectedItems],
            feedback: feedback
        };
        setFavorites(prev => [...prev, newFavorite]);
    };

    return (
        <div className="p-4 mt-8 bg-white rounded-lg shadow-md">
            <h2 className="text-2xl font-bold mb-4">Outfit Visualization Canvas</h2>
            
            <div className="mb-4">
                <h3 className="text-lg font-semibold mb-2">Select items from your closet:</h3>
                <div className="flex gap-2 overflow-x-auto pb-2">
                    {availableClothes && availableClothes.map(item => (
                        <div 
                            key={item.id} 
                            onClick={() => toggleItem(item)}
                            className={`flex-shrink-0 w-24 h-24 rounded cursor-pointer border-4 ${selectedItems.find(i => i.id === item.id) ? 'border-green-500' : 'border-transparent'}`}
                        >
                            <img src={item.imageUrl} alt="Item" className="w-full h-full object-cover rounded" />
                        </div>
                    ))}
                    {(!availableClothes || availableClothes.length === 0) && <p className="text-gray-500">Upload clothes first.</p>}
                </div>
            </div>

            <div className="p-4 bg-gray-100 rounded-lg min-h-[200px] flex items-center justify-center gap-4">
                {selectedItems.length === 0 ? (
                    <p className="text-gray-400">Select items to preview your outfit</p>
                ) : (
                    selectedItems.map(item => (
                        <img key={item.id} src={item.imageUrl} className="w-32 h-32 object-cover rounded shadow" alt="Outfit piece" />
                    ))
                )}
            </div>

            <div className="mt-4 flex gap-4">
                <button 
                    onClick={evaluateOutfit} 
                    disabled={isEvaluating || selectedItems.length < 2}
                    className="bg-purple-600 text-white px-4 py-2 rounded disabled:bg-gray-400"
                >
                    {isEvaluating ? 'AI is Evaluating...' : 'Ask AI Fashion Critic'}
                </button>
                <button 
                    onClick={saveFavorite}
                    disabled={selectedItems.length === 0}
                    className="bg-yellow-500 text-white px-4 py-2 rounded disabled:bg-gray-400"
                >
                    Save to Favorites
                </button>
            </div>

            {feedback && (
                <div className="mt-4 p-4 bg-blue-50 border border-blue-200 rounded text-blue-800">
                    <h4 className="font-bold">AI Fashion Critic says:</h4>
                    <p>{feedback.feedback}</p>
                    <p className="text-sm mt-1 opacity-70">Confidence Score: {feedback.score}%</p>
                </div>
            )}

            {favorites.length > 0 && (
                <div className="mt-8 border-t pt-4">
                    <h3 className="text-xl font-bold mb-4">Favorite Outfits</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {favorites.map(fav => (
                            <div key={fav.id} className="border p-2 rounded bg-gray-50">
                                <div className="flex gap-2">
                                    {fav.items.map(i => (
                                        <img key={i.id} src={i.imageUrl} className="w-16 h-16 object-cover rounded" alt="Fav piece" />
                                    ))}
                                </div>
                                {fav.feedback && <p className="text-sm mt-2 italic">"{fav.feedback.feedback}"</p>}
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
}
