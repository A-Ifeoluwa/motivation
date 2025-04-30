from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of motivational messages
motivational_messages = [
    "Hey {name}, keep going! You're doing great! 💪 and thanks for checking this out 😍",
    "You're amazing, {name}! Keep pushing forward, success is within reach! ✨",
    "You’ve got this, {name}! Keep chasing your dreams, you're unstoppable! 🚀",
    "Great things are coming your way, {name}! Stay focused and keep moving forward! 🌟",
    "Hey {name}, you are stronger than you think! Keep shining! 💖"
]

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            # Select a random motivational message
            selected_message = random.choice(motivational_messages)
            message = selected_message.format(name=name)
        else:
            message = "Please enter your name."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
