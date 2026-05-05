# Architecture

## High-Level Overview
OutfitCheck-AI uses a modern 3-tier architecture:
1. **Frontend:** React + Vite SPA using Vanilla CSS.
2. **Backend:** FastAPI (Python) server handling business logic, authentication, and orchestrating AI Agents.
3. **Database & Storage:** PostgreSQL for relational data (via SQLAlchemy) and Local File Storage (for MVP) to hold uploaded clothing images.

## AI Agents Integration
We integrate two main AI Agents powered by the OpenAI API (GPT-4o):
- **Wardrobe Item Analyzer Agent:** Triggered on image upload to extract metadata (color, category, style, season) using Vision capabilities.
- **Outfit Recommender / Fashion Critic Agent:** Orchestrated by the backend to fetch wardrobe items and user context (occasion) to compose an outfit and provide styling feedback.

## Deployment Strategy (Future)
- Frontend deployed to a static host (e.g., Vercel, Netlify).
- Backend deployed to a scalable platform (e.g., Render, Heroku, AWS).
- Database migrated to a managed PostgreSQL provider.
- Storage migrated to an S3-compatible service (e.g., Supabase Storage).
