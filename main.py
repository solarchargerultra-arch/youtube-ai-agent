import os
from flask import Flask
from google import genai

app = Flask(__name__)

# Inizializza il client di Gemini usando la chiave gratuita
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def run_agent():
# Chiediamo a Gemini di generare un'idea per il video
response = client.models.generate_content(
model="gemini-2.5-flash",
contents="Crea un titolo accattivante e una descrizione per un video YouTube sulla tecnologia moderna.",
)

print(f"Idea generata: {response.text}")
return f"Agente eseguito con successo! Ecco l'idea:\n\n{response.text}", 200

if name == "__main__":
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
