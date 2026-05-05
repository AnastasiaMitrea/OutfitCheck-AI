# Diagrams

*(Note: These Mermaid diagrams will be updated as the system implementation progresses.)*

## System Architecture

```mermaid
graph TD
    UI[Frontend: React/Vite] --> API[Backend: FastAPI]
    API --> DB[(PostgreSQL)]
    API --> Storage[Local File Storage]
    API --> OpenAIApi(OpenAI GPT-4o API)
```

## AI Agent Flow (Upload)

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Storage
    participant AnalyzerAgent

    User->>Frontend: Upload clothing photo
    Frontend->>Backend: POST /upload
    Backend->>Storage: Save image file
    Backend->>AnalyzerAgent: Process image with GPT-4o Vision
    AnalyzerAgent-->>Backend: Return structured metadata (category, color, etc.)
    Backend->>DB: Save item record with metadata
    Backend-->>Frontend: Item successfully added
```

## AI Agent Flow (Recommendation & Critique)

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant RecommenderCriticAgent

    User->>Frontend: Request outfit for "Formal Dinner"
    Frontend->>Backend: POST /recommend
    Backend->>DB: Fetch user's wardrobe items
    Backend->>RecommenderCriticAgent: Prompt with wardrobe list & occasion
    RecommenderCriticAgent-->>Backend: Return selected outfit & style feedback
    Backend-->>Frontend: Display outfit and critique
```
