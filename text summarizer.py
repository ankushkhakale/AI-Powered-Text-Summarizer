import requests
import gradio as gr

# Deepseek API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def summarize_text(text):
    """
    Uses Deepseek AI to summarize the given text.
    """
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Summarize the following text in **3 bullet points**:\n\n{text}",
        "stream": False,
    }
    response = requests.post(OLLAMA_URL, json=payload)
    if response.status_code == 200:
        return response.json().get("response","No summary generated.")
    else:
        return f"Error: {response.text}"
    