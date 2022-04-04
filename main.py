from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return  "<h1>Welcome</h1>"

@app.route("/login")
def Login():
    return render_template("login.html")

@app.route("/register")
def Register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run()