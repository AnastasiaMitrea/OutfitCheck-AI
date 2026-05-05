# Raport despre folosirea toolurilor de AI în timpul dezvoltării

În cadrul etapei intermediare a proiectului OutfitCheck-AI, am integrat intensiv instrumente de inteligență artificială în toate fazele de dezvoltare, conform cerințelor:

## 1. Planificare și Backlog (User Stories)
- **Tool folosit**: ChatGPT / Gemini
- **Mod de utilizare**: Am folosit prompturi pentru a genera lista de User Stories plecând de la o descriere de nivel înalt a aplicației (OutfitCheck-AI). AI-ul a ajutat la definirea formatului standard de *Role-Goal-Benefit* și la identificarea funcționalităților cheie (ex. *Digital Visualization*, *Contextual Styling*).

## 2. Arhitectură și Diagrame
- **Tool folosit**: Claude 3 / Gemini (Mermaid.js generation)
- **Mod de utilizare**: Am descris componentele aplicației și am cerut generarea codului Mermaid pentru o diagramă de arhitectură și un flux de secvență (sequence diagram). Acestea ilustrează interacțiunea dintre Web App și cei 2 agenți AI locali.

## 3. Implementare Cod și Agenți AI (App.py)
- **Tool folosit**: GitHub Copilot / Gemini Advanced / Hugging Face
- **Mod de utilizare**:
  - Am folosit AI pentru a scrie boilerplate-ul aplicației în Streamlit.
  - Cei doi agenți ceruți (Contextual Stylist Agent și Fashion Critic Agent) folosesc modele de limbaj mici (Small Language Models) de pe Hugging Face (`google/flan-t5-small`) prin `transformers.pipeline`.
  - Promturile pentru LLM-ul local au fost dezvoltate și rafinate cu ajutorul AI.

## 4. Testare Automată și Evaluări Agenți (Evals)
- **Tool folosit**: ChatGPT
- **Mod de utilizare**: A generat codul de testare folosind `pytest`. Testele sunt specifice pentru agenții AI (Evals) – verifică dacă modelele locale generează un răspuns valid (non-empty string) pentru prompturi date (ex. feedback pentru o ținută de plajă).

## 5. Integrare Continuă (CI/CD)
- **Tool folosit**: GitHub Copilot
- **Mod de utilizare**: Am generat fișierul `.github/workflows/main.yml` pentru a rula testele de evals automat la fiecare push/pull request pe branch-ul principal.

## 6. Raportare Bug și Rezolvare
- **Tool folosit**: ChatGPT
- **Mod de utilizare**: Am simulat găsirea unui bug în pipeline-ul AI (ex. răspunsuri goale la un context prea scurt) și am folosit AI pentru a genera soluții de validare (try-except blocks pentru încărcarea modelelor).
