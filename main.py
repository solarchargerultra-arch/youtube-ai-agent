import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
api_key = os.environ.get("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1models/gemini-2.5-flash:generateContent?key={api_key}"

# Se la chiamata diretta dà problemi, intanto facciamo rispondere Flask per vedere se va "Live"
return "<h1>Server Online e Funzionante!</h1>", 200

if name == "__main__":
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
