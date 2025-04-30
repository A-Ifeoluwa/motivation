from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            message = f"Hey {name}, keep going! You're doing great! 💪 and thanks for checking this out 😍"
        else:
            message = "Please enter your name."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
