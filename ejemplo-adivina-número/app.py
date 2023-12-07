from flask  import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'clave secreta'

#crear ruta raíz

@app.route('/')
def index():
    if 'numero_secreto' not in session:
        session['numero_secreto'] = random.randint(0,2)
        session['intentos'] = 0
    print(f"Número secreto: {session['numero_secreto']}")
    return render_template('index.html')

@app.route('/procesar_numero_usuario', methods=['POST'])
def procesar_numero():
    session['numero_usuario'] = int(request.form['numero_usuario'])
    session['intentos'] += 1
    print(f"Número ingresado por el usuario: {session['numero_usuario']}")
    return redirect('/')

@app.route('/reset_session')
def eliminar_sesion():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=9500)