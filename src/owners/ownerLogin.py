from flask import Blueprint, render_template, request, flash, redirect, url_for
import sqlite3

login_bp = Blueprint("login", __name__, template_folder="../templates")

@login_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")  # Renderiza el formulario de login

    elif request.method == "POST":
        # Obtener datos del formulario
        email = request.form.get("email")
        password = request.form.get("password")

        # Validar credenciales
        if validate_login(email, password):
            # flash("Login successful", "success")
            return render_template("home.html")  # Redirigir a la página principal
        else:
            flash("Invalid credentials. Please try again.", "danger")
            return render_template("login.html")


def validate_login(email, password):
    try:
        # Conectar a la base de datos
        db_path = r"C:\Users\stile\OneDrive\Escritorio\Aplicacion\src\db\database.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Buscar el usuario con el email y contraseña
        cursor.execute(
            """
            SELECT * FROM owners
            WHERE email = ? AND password = ?
            """,
            (email, password),
        )
        user = cursor.fetchone()

        # Si encuentra un usuario, devuelve True
        return user is not None

    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")
        return False

    finally:
        if "conn" in locals() and conn:
            conn.close()
