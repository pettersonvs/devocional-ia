from flask import Flask, render_template, request
from pipeline.gerador import gerar_devocional

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    devocional = None

    if request.method == "POST":
        tema = request.form.get("tema")
        devocional = gerar_devocional(tema)

    return render_template("index.html", devocional=devocional)

if __name__ == "__main__":
    app.run(debug=True)
