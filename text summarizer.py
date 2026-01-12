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
    
# Create a gradio interface
interface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, placeholder="Enter text to summarize here="),
    outputs=gr.Textbox(label="Summarized Text"),
    title="AI-Powered Text Summarizer",
    description="Enter a long text and AI will generate a concise summary"
)

# Launch the interface
if __name__ == "__main__":
    interface.launch()
