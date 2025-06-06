from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import spacy
import requests
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

nlp = spacy.load("en_core_web_sm")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/process_prompt")
async def process_prompt(request: PromptRequest):
    prompt = request.prompt
    doc = nlp(prompt)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print("Named Entities:", entities)
    try:
        ollama_response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        ollama_response.raise_for_status()
        llm_response = ollama_response.json().get("response", "No response from LLM")
    except requests.RequestException as e:
        llm_response = f"Error connecting to Ollama: {str(e)}"
    print("LLM Response:", llm_response)
    return {"entities": entities, "llm_response": llm_response}