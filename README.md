<h1 align="center">🤖 AI Regulation Q&A Assistant</h1>

<p align="center">
  <em>A lightweight Retrieval-Augmented Generation (RAG) system using <strong>google/flan-t5-base</strong> to answer policy-level questions about AI laws and regulations.</em>
</p>

<hr>

<h2>📌 Project Overview</h2>
<p>
  This project is an AI-powered assistant designed to provide accurate, context-aware answers to questions about global AI regulations.
  It uses a curated dataset of documents such as:
</p>
<ul>
  <li>EU AI Act</li>
  <li>NIST AI Risk Management Framework</li>
  <li>OECD AI Principles</li>
</ul>
<p>
  Built with a RAG (Retrieval-Augmented Generation) architecture, the assistant retrieves the most relevant legal text using semantic similarity and generates human-readable answers using the <code>google/flan-t5-base</code> language model.
</p>

<h2>🚀 Features</h2>
<ul>
  <li>Semantic search over AI policy documents using <strong>FAISS</strong></li>
  <li>Question answering via HuggingFace’s <code>flan-t5-base</code></li>
  <li>Flask-based web interface</li>
  <li>Supports CPU or GPU (if available)</li>
</ul>

<h2>🛠 Tech Stack</h2>
<ul>
  <li><strong>Hugging Face Transformers:</strong> <code>flan-t5-base</code> for generation</li>
  <li><strong>Sentence-Transformers:</strong> for embedding and semantic search</li>
  <li><strong>FAISS:</strong> vector database for similarity search</li>
  <li><strong>Flask:</strong> lightweight Python web server</li>
</ul>

<h2>📂 File Structure</h2>

<pre>
├── app.py                 # Flask app entry point
├── rag_pipeline.py        # Embedding, retrieval, and generation logic
├── requirements.txt       # Python dependencies
├── .env                   # Store your Hugging Face API key here
├── data/
│   └── ai_regulations.txt # Curated AI regulation documents
</pre>

<h2>🔑 Add Your Hugging Face API Key</h2>
<p>
  To use the Hugging Face model, create a <code>.env</code> file in the root of your project with the following content:
</p>

<pre>
HUGGINGFACE_HUB_TOKEN=your_huggingface_api_key_here
</pre>

<p>
  You can get your token by visiting your Hugging Face account at 
  <a href="https://huggingface.co/settings/tokens" target="_blank">https://huggingface.co/settings/tokens</a>
</p>

<h2>⚙️ Installation & Running</h2>

<pre>
# Clone the repo
git clone https://github.com/Aditi0143/AI-Regulation-QA-Assistant
cd AI-Regulation-QA-Assistant

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
</pre>

<h2>🌐 How It Works</h2>
<ol>
  <li>Documents are split into chunks and embedded using Sentence Transformers.</li>
  <li>FAISS indexes the vectors for fast semantic retrieval.</li>
  <li>User queries retrieve top-k most relevant chunks.</li>
  <li>The <code>flan-t5-base</code> model is prompted with retrieved context to generate the final answer.</li>
</ol>

<h2>📸 Demo Screenshot</h2>
<p><em>Add your screenshot here by uploading to the repo and linking below:</em></p>
<pre>
<img src="screenshots/demo.png" alt="App Screenshot" width="700">
</pre>

<h2>📜 License</h2>
<p>This project is open-source and released under the MIT License.</p>

<h2>🙌 Acknowledgments</h2>
<ul>
  <li><a href="https://huggingface.co/google/flan-t5-base">google/flan-t5-base</a> by Google</li>
  <li><a href="https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2">all-MiniLM-L6-v2</a> by SentenceTransformers</li>
  <li><a href="https://github.com/facebookresearch/faiss">Facebook FAISS</a></li>
</ul>
