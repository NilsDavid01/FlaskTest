from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Python Flask!"

if __name__ == '__main__':
    # Specified port=300 here
    app.run(debug=True, port=300)
