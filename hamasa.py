from flask import Flask

app = Flask(__name__)

@app.route('/')

def WelcomeToMyPage():
    return "Welcome ❤️‍🔥"

if __name__=="__main__":
    app.run(host="0.0.0.0", depug=True)