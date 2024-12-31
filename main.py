from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="sk-cbe5783f4f90406082384eb9315e12d7", base_url="https://api.deepseek.com")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
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
