
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/sistema")
def sistema():
    return render_template("sistema.html")


@app.route("/vacante")
def vacante():
    return render_template("vacante.html")


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        return redirect(url_for("evaluacion"))

    return render_template("registro.html")


@app.route("/evaluacion")
def evaluacion():
    return render_template("evaluacion.html")


if __name__ == "__main__":
    app.run(debug=True)
