from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/profile/<username>")
def profile(username):
    # Vulnerable code: User-controlled path directly used
    try:
        with open(f"data/{username}.txt", "r") as file:
            user_data = file.read()
            return render_template("profile.html", user_data=user_data)
    except FileNotFoundError:
        return "User not found."

if __name__ == "__main__":
    app.run(debug=True)
