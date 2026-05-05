# Product Backlog

## Must Have (MVP)
- Monorepo infrastructure setup & CI/CD pipeline (GitHub Actions).
- Minimal JWT User Authentication.
- PostgreSQL Database schema (Users, Wardrobe Items).
- Image upload to local file storage (with abstraction for future cloud migration).
- **Agent 1:** Wardrobe Item Analyzer (OpenAI GPT-4o Vision) to extract category, color, style, season, and tags from uploaded photos.
- Basic UI for Wardrobe Management (View, Add, Delete).
- **Agent 2:** Outfit Recommender / Fashion Critic Agent (OpenAI GPT-4o) to generate outfits and provide feedback based on occasion and wardrobe items.

## Should Have
- Weather API Integration for contextual recommendations.
- Visual display of generated outfits (combining top, bottom, shoes).
- Natural language search for the digital closet.
- Automated testing (Pytest/Vitest) and simple Agent evaluation pipelines.

## Nice to Have
- "Save to Favorites" for generated outfits.
- Upload an inspiration photo and find similar items in the user's closet.
- Search online for matching vibe/style.
