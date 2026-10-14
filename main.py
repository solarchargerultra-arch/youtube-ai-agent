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
contents="Crea un titolo e una descrizione per un video YouTube sulla tecnologia moderna."
)
return f"<h1>Agente Attivo!</h1><p>{res.text}</p>", 200
except Exception as e:
return f"Errore: {str(e)}", 500

if name == "__main__":
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
