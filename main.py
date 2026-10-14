import os
from flask import Flask
from google import genai

app = Flask(__name__)

@app.route("/")
def home():
try:
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
res = client.models.generate_content(
model="gemini-2.5-flash",
contents="Crea un titolo accattivante per un video YouTube sulla tecnologia."
)
return f"<h1>Agente attivo!</h1><p>{res.text}</p>", 200
except Exception as e:
return f"Errore durante la chiamata a Gemini: {str(e)}", 500

if name == "__main__":
port = int(os.environ.get("PORT", 8080))
app.run(host="0.0.0.0", port=port)
