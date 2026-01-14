# AI-Powered Text Summarizer

An intelligent text summarization application powered by DeepSeek-R1 LLM. This project provides both a REST API and a user-friendly web interface for summarizing text content.

## 📋 Project Overview

This application leverages state-of-the-art AI models to generate concise and accurate summaries of text documents. It offers flexibility with multiple deployment options:
- **FastAPI REST API** - For programmatic access and integration
- **Gradio Web Interface** - For interactive, user-friendly text summarization

## 🛠️ Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Backend Framework** | FastAPI | Latest |
| **Web Server** | Uvicorn | Latest |
| **LLM Model** | Deepseek-R1 | Via Ollama |
| **Model Runtime** | Ollama | 11434 (default port) |
| **Frontend Interface** | Gradio | Latest |
| **HTTP Client** | Requests | Latest |
| **Python** | Python | 3.13.9 |
| **Environment Management** | Virtual Environment (venv) | Built-in |

## ✨ Features

- **Fast REST API** - Lightning-fast summarization endpoint
- **Auto Documentation** - Interactive Swagger UI at `/docs`
- **User-Friendly Interface** - Gradio web UI for non-technical users
- **Local Processing** - Runs locally with Ollama (no cloud costs)
- **Easy Integration** - RESTful API for third-party integrations
- **Configurable** - Easily switch to cloud LLMs (OpenAI, HuggingFace, etc.)

## 📦 Prerequisites

- **Python 3.13+** installed
- **Ollama** installed and running (port 11434)
- **Deepseek-R1 model** pulled in Ollama
- Git for version control

## 🚀 Installation

### 1. Clone Repository
```bash
git clone https://github.com/ankushkhakale/AI-Powered-Text-Summarizer.git
cd AI-Powered-Text-Summarizer
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install fastapi uvicorn requests gradio
```

### 5. Ensure Ollama is Running
```bash
ollama serve
```

In another terminal, pull the Deepseek model:
```bash
ollama pull deepseek-r1
```

## 💻 Usage

### Option 1: FastAPI REST API

Start the server:
```bash
uvicorn app:app --reload
```

Server runs at: `http://localhost:8000`

**Access Interactive Docs:**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

**API Endpoint:**
```
POST http://localhost:8000/summarize/
```

**Request (JSON):**
```json
{
  "text": "Your long text here that needs to be summarized..."
}
```

**Response:**
```json
{
  "response": "Summarized text here..."
}
```

**Example with cURL:**
```bash
curl -X POST "http://localhost:8000/summarize/" \
  -H "Content-Type: application/json" \
  -d '{"text":"Your text to summarize"}'
```

### Option 2: Gradio Web Interface

Run the Gradio app:
```bash
python "text summarizer.py"
```

Opens automatically in browser (usually `http://localhost:7860`)

## 📁 Project Structure

```
AI-Powered-Text-Summarizer/
├── app.py                      # FastAPI REST API
├── text summarizer.py          # Gradio web interface
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .env                        # Environment variables (optional)
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/summarize/` | Summarize text content |
| GET | `/docs` | Interactive API documentation |
| GET | `/redoc` | ReDoc API documentation |


## 📝 Environment Variables

Optional configuration in `.env`:
```
OLLAMA_URL=http://localhost:11434/api/generate
OLLAMA_MODEL=deepseek-r1
API_PORT=8000
```

## 🤝 Contributing

Feel free to fork, modify, and submit pull requests!

## 📄 License

MIT License - feel free to use this project for personal or commercial purposes.


## 📧 Contact & Support

For issues or questions, open a GitHub issue in the repository.
