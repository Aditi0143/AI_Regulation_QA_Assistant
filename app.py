from flask import Flask, request, render_template_string
from rag_pipeline import load_chunks, create_faiss_index, load_llm, retrieve, generate_answer

app = Flask(__name__)

# Load data and initialize models on server start
chunks = load_chunks("data/ai_regulations.txt")  # Ensure this file exists
faiss_index, embedder, all_chunks = create_faiss_index(chunks)
llm = load_llm()  # Loads flan-t5-base as text2text-generation

# Simple HTML form UI
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Regulation Assistant</title>
</head>
<body style="font-family: Arial; padding: 40px;">
    <h1>🤖 Ask About AI Laws & Regulations</h1>
    <form method="POST">
        <textarea name="query" rows="4" cols="80" placeholder="Ask a question about AI regulations...">{{ query }}</textarea><br><br>
        <input type="submit" value="Submit">
    </form>
    {% if answer %}
        <h3>Answer:</h3>
        <div style="background: #f0f0f0; padding: 15px; border-radius: 5px;">{{ answer }}</div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():  # ✅ renamed from 'index'
    answer = ""
    query = ""
    if request.method == "POST":
        query = request.form["query"]
        docs = retrieve(query, faiss_index, embedder, all_chunks)
        context = "\n\n".join(docs)
        answer = generate_answer(llm, context, query)
    return render_template_string(HTML_TEMPLATE, answer=answer, query=query)

if __name__ == "__main__":
    app.run(debug=True)
