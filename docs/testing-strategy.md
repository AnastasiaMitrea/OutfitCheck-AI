# Testing Strategy

## Overview
Quality assurance is achieved through automated testing for both standard application logic and AI Agent behavior.

## 1. Backend Testing (Pytest)
- **Unit Tests:** For testing API routes, database CRUD operations, and core utility functions.
- **Integration Tests:** For testing the communication between the API and the database.

## 2. Frontend Testing (Vitest)
- **Component Tests:** Verifying that React components render correctly with mocked data.
- **State & Logic Tests:** Ensuring standard user flows (like the upload form) behave as expected.

## 3. AI Agent Evaluations
- Given the non-deterministic nature of LLMs, we will implement deterministic test cases using `pytest` to evaluate the **Agentic Output**.
- **Strategy for Analyzer Agent:** Upload test images with known ground-truth attributes (e.g., a "Red T-shirt"). Assert that the LLM extracts the correct category (`top`) and color (`red`).
- **Strategy for Recommender Agent:** Provide a fixed, mocked wardrobe and a specific occasion ("Formal Event"). Assert that the generated outfit contains pieces appropriate for the occasion and that the pieces actually exist in the mock wardrobe.

## 4. CI/CD Pipeline
A GitHub Actions workflow will be configured to run automatically on every Pull Request. To ensure code quality and prevent broken code from being merged into `main`, the pipeline will check:
- **Backend tests:** Executes Pytest suite.
- **Frontend tests:** Executes Vitest suite.
- **AI Agent Evals:** Runs the deterministic evaluation tests for the agents.
- **Linting & Formatting:** Checks code style (e.g., using ESLint/Prettier for frontend, Flake8/Black for backend) once configured.
