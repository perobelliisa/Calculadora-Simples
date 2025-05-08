from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_oper', methods=['POST'])
def calcular_oper():
    calculo = (request.form['calculo'])
    numero1 = float(request.form['numero1'])
    numero2 = float(request.form['numero2'])
    if calculo == "+":
        resultado = numero1+numero2
    if calculo == "-":
        resultado = numero1-numero2
    if calculo == "*":
        resultado = numero1*numero2
    if calculo == "/":
        resultado = numero1/numero2

    return render_template('index.html', resultado=resultado)
if __name__ =='__main__':
    app.run(debug=True)