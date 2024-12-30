from flask import Flask, render_template
from owners.ownerRegister import owners_bp  # Importa el blueprint

# Inicializa la app
app = Flask(__name__, template_folder="templates")
app.secret_key = "your_secret_key"  # Necesario para usar flash messages

# Registrar el blueprint
app.register_blueprint(owners_bp)

# Ruta para el login
@app.route("/", methods=["GET", "POST"])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)