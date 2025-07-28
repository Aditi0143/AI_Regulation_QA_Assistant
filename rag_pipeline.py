import os 
import faiss
import torch
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from sentence_transformers import SentenceTransformer
from huggingface_hub import login

# Load environment variables
load_dotenv()
hf_token = os.getenv("HUGGINGFACE_HUB_TOKEN")
if hf_token:
    login(token=hf_token)

# Load and chunk documents
def load_chunks(file_path, chunk_size=500):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

# Embed and build FAISS
def create_faiss_index(chunks, embed_model_name='all-MiniLM-L6-v2'):
    embedder = SentenceTransformer(embed_model_name)
    embeddings = embedder.encode(chunks, show_progress_bar=True)
    faiss_idx = faiss.IndexFlatL2(embeddings.shape[1])  # ✅ renamed to avoid conflict
    faiss_idx.add(embeddings)
    return faiss_idx, embedder, chunks

# Retrieve top-k relevant chunks
def retrieve(query, faiss_idx, embedder, chunks, k=3):
    query_vec = embedder.encode([query])
    distances, indices = faiss_idx.search(query_vec, k)
    return [chunks[i] for i in indices[0]]

# Load the LLM (Flan-T5 or Falcon)
@torch.no_grad()
def load_llm(model_name='google/flan-t5-base', hf_token=hf_token):
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=hf_token)
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto",
        use_auth_token=hf_token
    )
    generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    return generator

# Generate response from context
@torch.no_grad()
def generate_answer(llm, context, query):
    prompt = f"""Given the following legal or policy text, answer the question.

Context:
{context}

Question:
{query}

Answer:"""
    result = llm(prompt, max_new_tokens=300)
    return result[0]['generated_text'].strip()
