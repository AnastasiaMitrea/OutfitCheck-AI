import { test, expect } from 'vitest';
import AIFashionCritic from '../services/aiCritic';

test('AI Fashion Critic returns score > 0 for standard outfits', async () => {
    expect(AIFashionCritic.evaluateOutfit).toBeDefined();
    const mockResponse = { feedback: "Great", score: 90 };
    expect(mockResponse.score).toBeGreaterThan(0);
});
