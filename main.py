import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
api_key = os.getenv("OPENAI_API_KEY")
# .env is not committed, so the key may be missing; start anyway and report it on /chat.
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com") if api_key else None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    if client is None:
        return jsonify({"response": "Server has no API key. Add OPENAI_API_KEY=<your key> to a .env file next to main.py and restart."}), 500

    user_message = request.json.get("message", "")
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user_message},
        ],
        stream=False  # Changed to False for simplicity
    )
    
    bot_response = response.choices[0].message.content
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
