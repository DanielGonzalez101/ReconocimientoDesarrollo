from flask import Blueprint, render_template, request, flash
import sqlite3

# Define el blueprint
owners_bp = Blueprint("owner", __name__, template_folder="../templates")


@owners_bp.route("/registerOwner", methods=["GET", "POST"])
def registerOwner():
    if request.method == "GET":
        return render_template(
            "registerOwner.html"
        )  # Renderiza el formulario de registro

    elif request.method == "POST":
        # Obtiene datos del formulario
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        age = request.form.get("age")
        id_number = request.form.get("id_number")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        if password != confirm_password:
            print("Passwords do not match", "danger")
            return render_template("registerOwner.html")

        insert_owner(first_name, last_name, age, id_number, email, password)

        # Lógica de registro o base de datos
        print("Registration successful", "success")
        print(first_name, last_name, age, id_number, email, password)
        return render_template("login.html")


def insert_owner(first_name, last_name, age, id_number, email, password):
    try:
        # Conexión a la base de datos SQLite
        conn = sqlite3.connect(
            r"C:\Users\stile\OneDrive\Escritorio\Aplicacion\src\db\database.db"
        )
        cursor = conn.cursor()

        # Inserta datos en la tabla owners
        cursor.execute(
            """
            INSERT INTO owners (first_name, last_name, age, id_number, email, password)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (first_name, last_name, age, id_number, email, password),
        )
        # Guarda los cambios
        conn.commit()

    except sqlite3.Error as e:
        print(f"Error inserting data into SQLite: {e}")

    finally:
        # Cierra la conexión
        conn.close()
