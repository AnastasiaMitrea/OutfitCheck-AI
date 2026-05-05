import { test, expect } from 'vitest';

test('Search functionality filters clothes by tags', () => {
    const mockClothes = [
        { id: 1, tags: [{ label: 'black' }, { label: 'dress' }] },
        { id: 2, tags: [{ label: 'red' }, { label: 'shirt' }] }
    ];
    
    const query = 'black';
    const keywords = query.split(' ');
    
    const filtered = mockClothes.filter(item => {
        return keywords.every(kw => 
            item.tags.some(tag => tag.label.toLowerCase().includes(kw))
        );
    });
    
    expect(filtered.length).toBe(1);
    expect(filtered[0].id).toBe(1);
});
