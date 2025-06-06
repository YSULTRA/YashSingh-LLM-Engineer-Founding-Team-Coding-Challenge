# YashSingh-LLM-Engineer-Founding-Team-Coding-Challenge

## Demo Video


https://github.com/user-attachments/assets/b744790c-131d-4d58-8c62-6614c5f593d2


![image](https://github.com/user-attachments/assets/4a1d298a-67ed-4b31-8c67-cd6ff32e9803)
![image](https://github.com/user-attachments/assets/df865e96-8feb-4a61-90b1-467eb22de080)
![image](https://github.com/user-attachments/assets/4286f9c1-493d-47e8-80c1-a492c67e03ec)


- Sending multiple prompts in a chat space.
- NER highlighting and PII details panel.
- Loading bars during processing.
- Creating and switching between chat spaces.
- Console logs for debugging.


- `app.py` (FastAPI backend with spaCy NER and Ollama integration, as commented in the previous response).
- `index.html` (GUI with multiple chat spaces, loading bars, scrolling, and NER highlights, as provided earlier).
- `requirements.txt` (generated via `pip freeze`).


---

```markdown
# PrivChat: PII Detection and LLM Interaction

**PrivChat** is a web application that processes user prompts to detect Personally Identifiable Information (PII) using spaCy's named entity recognition (NER) and generates contextual responses via the LLaMA 3 model hosted by Ollama. Built with FastAPI for the backend and a custom HTML/CSS/JavaScript frontend, it features a modern, dark-themed GUI with multiple chat spaces, real-time NER highlighting, a PII details panel, loading indicators, and smooth scrolling. This project was developed as part of the **LLM Engineer Coding Challenge**.

## Features

- **Backend**:
  - FastAPI server with a `/process_prompt` endpoint for prompt processing.
  - spaCy (`en_core_web_sm`) for extracting named entities (e.g., PERSON, ORG, GPE, DATE).
  - Ollama (`llama3`) for generating natural language responses.
  - CORS middleware to enable frontend-backend communication.
  - Console logging of named entities and LLM responses for debugging.
- **Frontend**:
  - macOS-style, dark-themed GUI with smooth animations.
  - Multiple chat spaces to manage separate conversations.
  - Real-time NER highlighting (orange for PERSON, blue for other entities).
  - PII details panel displaying entity types and confidence scores.
  - Animated loading bars during prompt processing.
  - Smooth scrolling for long conversations with multiple prompts.
  - Sticky input field and send button for consistent user interaction.
  - Client-side validation to prevent empty prompts, avoiding `422` errors.
- **Demo Video**: Watch the application in action [here](https://drive.google.com/file/d/14ELd9xDBU9T2HiR1_kf8tFZy2SD0WdVU/view?usp=sharing).

## Repository Structure

```plaintext
├── app.py              # FastAPI backend with NER and Ollama integration
├── index.html          # Frontend GUI with chat interface
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Prerequisites

Before setting up the project, ensure your laptop meets the following requirements:

- **Operating System**: Windows, macOS, or Linux (tested on Windows 11).
- **Python**: Version 3.8 or higher (recommended: 3.11).
- **Ollama**: Installed and running with the `llama3` model pulled.
- **Internet Connection**: Required for initial dependency installation and model downloads.
- **Hardware**:
  - Minimum: 8 GB RAM, 2-core CPU.
  - Recommended: 16 GB RAM, 4-core CPU for faster Ollama processing.
- **Disk Space**: Approximately 5 GB for virtual environment, spaCy model, and Ollama model.
- **Tools**: Git for cloning the repository, a terminal (e.g., PowerShell, Bash), and a web browser (e.g., Chrome, Firefox).

## Setup Instructions

Follow these steps to set up and run the project on your laptop. Instructions are provided for **Windows (PowerShell)** with notes for **macOS/Linux** where differences apply.

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/YSULTRA/YashSingh-LLM-Engineer-Founding-Team-Coding-Challenge.git
```


If Git is not installed:
- **Windows**: Download from [git-scm.com](https://git-scm.com/) and install.
- **macOS**: Install via Homebrew (`brew install git`).
- **Linux**: Use your package manager (e.g., `sudo apt install git` on Ubuntu).

### 2. Install Python

Ensure Python 3.8+ is installed. Check with:

```bash
python --version
```

Or:

```bash
python3 --version
```

If not installed:
- **Windows**: Download from [python.org](https://www.python.org/downloads/). Ensure "Add Python to PATH" is checked during installation.
- **macOS**: Install via Homebrew (`brew install python`).
- **Linux**: Install via package manager (e.g., `sudo apt install python3 python3-pip` on Ubuntu).

### 3. Create and Activate a Virtual Environment

Create a virtual environment to isolate dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:
- **Windows (PowerShell)**:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

You should see `(venv)` in your terminal prompt.

### 4. Install Python Dependencies

Install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install the core dependencies manually:

```bash
pip install fastapi uvicorn spacy requests pydantic
```

Download the spaCy English model for NER:

```bash
python -m spacy download en_core_web_sm
```

### 5. Install and Configure Ollama

Install Ollama to run the LLaMA 3 model locally:
- Download from [ollama.ai](https://ollama.ai/download) and follow the installation instructions for your OS.
- Start the Ollama server:
  ```bash
  ollama serve
  ```
  (Run in a separate terminal or as a background process.)
- Pull the `llama3` model:
  ```bash
  ollama pull llama3
  ```

Verify Ollama is running by checking `http://localhost:11434` in a browser or via:

```bash
curl http://localhost:11434
```

Expected response: `{"status":"ok"}`.

### 6. Run the FastAPI Backend

With the virtual environment activated, start the FastAPI server:

```bash
uvicorn app:app --reload
```

- `app:app`: Refers to the FastAPI app instance in `app.py`.
- `--reload`: Enables auto-reload for development.

The server will run at `http://localhost:8000`. You should see logs like:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### 7. Run the Frontend

In a new terminal (with the virtual environment activated), start a simple HTTP server to serve `index.html`:

```bash
python -m http.server 8080
```

The frontend will be accessible at `http://localhost:8080`.

- **macOS/Linux Note**: Use `python3 -m http.server 8080` if `python` refers to Python 2.

Open `http://localhost:8080` in a web browser (e.g., Chrome, Firefox) to access the GUI.

### 8. Verify the Setup

Ensure all components are running:
- **FastAPI**: Check `http://localhost:8000/docs` for the Swagger UI.
- **Ollama**: Verify `http://localhost:11434` responds.
- **Frontend**: Confirm the GUI loads at `http://localhost:8080`.

## Using the Application

1. **Access the GUI**:
   - Open `http://localhost:8080` in your browser.
   - The interface features:
     - A sidebar with chat spaces (e.g., "Chat Space 1", "Chat Space 2").
     - A "+ New Chat" button to create additional chat spaces.
     - A chat window with prompt input and send button (sticky at the bottom).
     - NER highlights (orange for PERSON, blue for other entities).
     - A PII details panel (toggle via the "i" button when PII is detected).
     - Loading bars during prompt processing.

2. **Test with Sample Prompts**:
   - Enter a prompt in the input field, e.g., "Elon Musk and Jeff Bezos are launching a SpaceX rocket from Cape Canaveral next week."
   - Click "Send" or press Enter.
   - Observe:
     - Loading bars appear during processing.
     - The prompt appears on the right with highlighted entities.
     - The LLM response appears on the left.
     - The PII panel (if entities are detected) shows entity details.
     - The chat window scrolls to show the latest messages.
   - Switch chat spaces or create a new one to test separate conversations.

3. **Console Logs**:
   - Check the FastAPI terminal for logs, e.g.:
     ```
     Named Entities: [('Elon Musk', 'PERSON'), ('Jeff Bezos', 'PERSON'), ('SpaceX', 'ORG'), ('Cape Canaveral', 'GPE'), ('next week', 'DATE')]
     LLM Response: That’s exciting! SpaceX...
     INFO: 127.0.0.1:XXXXX - "POST /process_prompt HTTP/1.1" 200 OK
     ```

## Testing with `curl`

Test the FastAPI endpoint directly using `curl` to verify backend functionality:

```bash
curl -X POST http://localhost:8000/process_prompt -H "Content-Type: application/json" -d "{\"prompt\": \"Elon Musk and Jeff Bezos are launching a SpaceX rocket.\"}"
```

**Expected Response** (JSON):

```json
{
  "entities": [
    ["Elon Musk", "PERSON"],
    ["Jeff Bezos", "PERSON"],
    ["SpaceX", "ORG"]
  ],
  "llm_response": "That’s exciting! SpaceX, led by Elon Musk, frequently launches rockets..."
}
```

**Windows (PowerShell)**:
Use `curl.exe` to avoid alias issues:

```powershell
curl.exe -X POST http://localhost:8000/process_prompt -H "Content-Type: application/json" -d '{"prompt": "Elon Musk and Jeff Bezos are launching a SpaceX rocket."}'
```

If you encounter errors (e.g., `422 Unprocessable Entity`), check the JSON syntax or ensure the FastAPI server is running.

## Troubleshooting

- **FastAPI Server Fails to Start**:
  - Ensure the virtual environment is activated (`.\venv\Scripts\Activate.ps1` on Windows).
  - Verify all dependencies are installed (`pip install -r requirements.txt`).
  - Check for port conflicts (e.g., another app using port 8000). Change port with `uvicorn app:app --port 8001`.
- **Ollama Not Responding**:
  - Confirm Ollama is running (`ollama serve`).
  - Verify the `llama3` model is pulled (`ollama pull llama3`).
  - Test `curl http://localhost:11434`.
  - If errors persist, check Ollama logs or restart the server.
- **Frontend Not Loading**:
  - Ensure the HTTP server is running (`python -m http.server 8080`).
  - Open `http://localhost:8080` in a browser.
  - Check browser console (F12 > Console) for JavaScript errors.
- **NER Highlights Missing**:
  - Verify spaCy model is installed (`python -m spacy download en_core_web_sm`).
  - Test with a prompt containing entities (e.g., "Elon Musk").
- **Scrolling Issues**:
  - Ensure you’re using the latest `index.html`.
  - Test with multiple prompts in one chat space.
  - Report issues with browser console logs (F12 > Console).
- **422 Errors**:
  - Ensure JSON payload is valid in `curl` or GUI requests.
  - Avoid empty prompts in the GUI (validation prevents this).

For further assistance, check FastAPI logs, browser console, or open an issue in this repository.



## Development Notes

- **Backend**:
  - `app.py` uses FastAPI for high-performance API handling.
  - spaCy’s `en_core_web_sm` model may misclassify some entities (e.g., `Tesla` as NORP instead of ORG), a known limitation.
  - Ollama’s `llama3` model provides robust responses but may be slow on lower-end hardware.
- **Frontend**:
  - `index.html` is a single-page application with vanilla JavaScript.
  - CSS uses a dark theme with macOS-inspired aesthetics.
  - Loading bars and scrolling are optimised for UX.
- **Improvements**:
  - Add authentication for secure API access.
  - Use a larger spaCy model (e.g., `en_core_web_lg`) for better NER accuracy.
  - Implement persistent chat history (e.g., via local storage or a database).
  - Optimise Ollama performance with GPU acceleration.

---



#### **Test Cases**
Use the prompts from prior responses:
1. **Prompt 1**: "Elon Musk and Jeff Bezos are launching a SpaceX rocket from Cape Canaveral next week."
   - Expected: 5 entities, LLM response, loading bars, scrolling.
2. **Prompt 2**: "I’m traveling from New York to Tokyo via London in December 2025."
   - Expected: 4 entities, scrolling for multiple prompts.
3. **Prompt 3**: "Barack Obama met with Apple’s Tim Cook in Paris to discuss climate change on January 15, 2023."
   - Expected: 5 entities, long response scrolls correctly.

**GUI Test**:
- Open `http://localhost:8080`.
- Send prompts in Chat Space 1, create a new chat space, and verify:
  - Loading bars appear.
  - NER highlights (orange/blue).
  - Scrolling works for multiple prompts.
  - PII panel shows entities.
  - Console logs entities and responses.

**Curl Test**:
```powershell
curl.exe -X POST http://localhost:8000/process_prompt -H "Content-Type: application/json" -d '{"prompt":"Elon Musk and Jeff Bezos are launching a SpaceX rocket."}'
```


