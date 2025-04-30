from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            message = f"Hey {name}, A Big Thank You! 🌷
We are so grateful that you’re testing this out, and we hope it brings you a bit of joy, 
positivity, and a renewed sense of purpose! Whether it’s a rough day or you’re just in need of a little inspiration,
remember: you’re not alone. Our goal is to build a community where everyone can feel motivated, 
appreciated, and empowered to take on whatever challenges come their way.

If this message made you smile, share it with someone who might need it too! Spread the love, and let’s keep
motivating each other. You’re not just testing a tool, you’re part of a movement. 🌍💪

Keep shining and keep striving – amazing things are ahead of you. ✨

With gratitude,
Team Motivation@ifeOps💙💪"
        else:
            message = "Please enter your name."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
