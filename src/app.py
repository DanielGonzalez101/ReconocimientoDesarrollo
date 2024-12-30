from flask import Flask, redirect, url_for
from owners.ownerRegister import register_bp  # Importa el blueprint de registro
from owners.ownerLogin import login_bp  # Importa el blueprint de login

# Inicializa la app
app = Flask(__name__, template_folder="templates")
app.secret_key = "your_secret_key"  # Necesario para flash messages

# Registrar blueprints
app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(register_bp, url_prefix="/register")

# Redirige la raíz al login
@app.route("/")
def home():
    return redirect(url_for("login.login"))  # Redirige al blueprint de login

# Punto de entrada
if __name__ == "__main__":
    app.run(debug=True)
