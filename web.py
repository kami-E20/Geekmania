from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Gedaj est actif sur Render 🚀"

def run_web():
    app.run(host='0.0.0.0', port=10000)