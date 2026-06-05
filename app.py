from flask import Flask, render_template, request

app = Flask(__name__)

def sumar(a, b):
    return a + b

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        resultado = sumar(num1, num2)

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)