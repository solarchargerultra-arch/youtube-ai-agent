import os
from flask import Flask
from google import genai

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def run_agent():
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
res = client.models.generate_content(model="gemini-2.5-flash", contents="Crea un titolo e descrizione per un video YouTube tech.")
return f"OK: {res.text}", 200

if name == "__main__":
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
