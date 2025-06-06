# Import FastAPI to create a web API application
from fastapi import FastAPI
# Import CORSMiddleware to handle Cross-Origin Resource Sharing
from fastapi.middleware.cors import CORSMiddleware
# Import spaCy for named entity recognition (NER)
import spacy
# Import requests to make HTTP calls to the Ollama API
import requests
# Import BaseModel from Pydantic for request body validation
from pydantic import BaseModel


app = FastAPI() # Initialize the FastAPI

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],          # Allow all HTTP methods (e.g., POST, GET)
    allow_headers=["*"],          # Allow all headers
)


nlp = spacy.load("en_core_web_sm") # Load the spaCy


class PromptRequest(BaseModel):
    prompt: str  # The user-provided text prompt

# POST endpoint to process user prompts
@app.post("/process_prompt")
async def process_prompt(request: PromptRequest):
    """
    Process a user prompt by extracting named entities with spaCy and generating
    a response using the Ollama LLM.

    Args:
        request (PromptRequest): The request body containing the user prompt.

    Returns:
        dict: A dictionary with named entities (list of tuples) and the LLM response.
    """

    prompt = request.prompt

    # Process the prompt with spaCy to identify named entities
    doc = nlp(prompt)
    # Extract entities as a list of (text, label) tuples
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    # Log the extracted entities for debugging
    print("Named Entities:", entities)

    try:

        ollama_response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",    # Use the LLaMA 3 model
                "prompt": prompt,
                "stream": False
            }
        )
        # Raise an exception for HTTP errors
        ollama_response.raise_for_status()

        llm_response = ollama_response.json().get("response", "No response from LLM")
    except requests.RequestException as e:

        llm_response = f"Error connecting to Ollama: {str(e)}"

    print("LLM Response:", llm_response)
    return {"entities": entities, "llm_response": llm_response}