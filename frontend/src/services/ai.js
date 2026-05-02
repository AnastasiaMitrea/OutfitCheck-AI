import { pipeline, env } from '@xenova/transformers';

// Skip local model checks to avoid some errors in the browser if weights are missing
env.allowLocalModels = false;

class AIAutoCategorizer {
    static instance = null;

    static async getInstance(progressCallback = null) {
        if (this.instance === null) {
            // Using a lightweight vision model (e.g., zero-shot image classification)
            this.instance = await pipeline('image-classification', 'Xenova/vit-base-patch16-224', {
                progress_callback: progressCallback
            });
        }
        return this.instance;
    }

    static async categorizeItem(imageUrl) {
        const classifier = await this.getInstance();
        const results = await classifier(imageUrl);
        
        // Map the results to clothing categories and colors
        // In a real app we would use a clothing-specific model or zero-shot. 
        // Here we just take the top 3 labels.
        return results.slice(0, 3).map(res => ({
            label: res.label,
            confidence: res.score
        }));
    }
}

export default AIAutoCategorizer;
