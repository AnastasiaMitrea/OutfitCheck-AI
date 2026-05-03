import { pipeline, env } from '@xenova/transformers';

env.allowLocalModels = false;

class AIFashionCritic {
    static instance = null;

    static async getInstance(progressCallback = null) {
        if (this.instance === null) {
            // Using a lightweight text classification model for sentiment/feedback
            // In a real app, this could be a vision-language model.
            this.instance = await pipeline('text-classification', 'Xenova/distilbert-base-uncased-finetuned-sst-2-english', {
                progress_callback: progressCallback
            });
        }
        return this.instance;
    }

    static async evaluateOutfit(items) {
        const critic = await this.getInstance();
        
        // Construct a text prompt based on the outfit items
        const tags = items.flatMap(item => item.tags.map(t => t.label)).join(", ");
        const promptText = `Outfit consisting of: ${tags}`;
        
        // Get sentiment-like score to mock a style evaluation
        const results = await critic(promptText);
        const score = results[0].score;
        const isGoodMatch = results[0].label === "POSITIVE" || score > 0.5;

        return {
            feedback: isGoodMatch 
                ? "Great color coordination! This outfit looks stylish and well put together."
                : "The colors might clash a bit. Consider swapping one item for a neutral tone.",
            score: Math.round(score * 100)
        };
    }
}

export default AIFashionCritic;
