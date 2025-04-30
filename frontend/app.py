from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace this with your Azure Function URL
AZURE_FUNCTION_URL = "https://<YOUR-FUNCTION-URL>"

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "message": request.form.get("message")
        }

        try:
            response = requests.post(AZURE_FUNCTION_URL, json=data)
            message = response.text
        except Exception as e:
            message = f"Error: {str(e)}"

    return render_template("index.html", status=message)

if __name__ == "__main__":
    app.run(debug=True)
