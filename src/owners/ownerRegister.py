from flask import Blueprint, render_template, request, flash
import sqlite3

# Define el blueprint
register_bp = Blueprint("register", __name__, template_folder="../templates")

def password_confirm(password, confirm_password):

    if password == confirm_password:
        return True
    else:
        return False


def verify_email(email):
    try:
        # Conexión a la base de datos SQLite
        print("Intentando conectar a la base de datos...")
        conn = sqlite3.connect(
            r"C:\Users\stile\OneDrive\Escritorio\Aplicacion\src\db\database.db"
        )
        cursor = conn.cursor()

        # Verifica si el email ya está registrado
        cursor.execute(
            """
            SELECT email
            FROM owners
            WHERE email = ?
            """,
            (email,),
        )

        result = cursor.fetchone()
        if result is not None:
            return True  # Retorna True si el email ya está registrado
        else:
            return False  # Retorna False si el email no está registrado

    except sqlite3.Error as e:
        print(f"Error verifying email in SQLite: {e}")
        return False  # Retorna False si hay un error

    finally:
        # Cierra la conexión
        if "conn" in locals():
            conn.close()


@register_bp.route("/", methods=["GET", "POST"])
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

        # Verifica los datos recibidos
        # print(
        #     f"Datos recibidos: {first_name}, {last_name}, {age}, {id_number}, {email}, {password}, {confirm_password}"
        # )

        if verify_email(email):
            flash("Email already registered", "error")
            return render_template("registerOwner.html")

        # Valida las contraseñas
        if password_confirm(password, confirm_password):
            insert_owner(first_name, last_name, age, id_number, email, password)
            return render_template("login.html")  # Redirige al login si es exitoso
        elif not password_confirm(password, confirm_password):
            flash("Passwords do not match", "error")
            return render_template("registerOwner.html")
        else:
            flash(
                "An error occurred while saving your data. Please try again.", "error"
            )
            return render_template("registerOwner.html")

def insert_owner(first_name, last_name, age, id_number, email, password):
    try:
        # Conexión a la base de datos SQLite
        print("Intentando conectar a la base de datos...")
        conn = sqlite3.connect(
            r"C:\Users\stile\OneDrive\Escritorio\Aplicacion\src\db\database.db"
        )
        cursor = conn.cursor()

        # Inserta datos en la tabla owners
        print("Insertando datos en la base de datos...")
        cursor.execute(
            """
            INSERT INTO owners (first_name, last_name, age, id_number, email, password)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (first_name, last_name, age, id_number, email, password),
        )

        # Guarda los cambios
        conn.commit()
        print("Datos guardados exitosamente.")
        return True  # Retorna True si fue exitoso

    except sqlite3.Error as e:
        print(f"Error inserting data into SQLite: {e}")
        return False  # Retorna False si hay un error

    finally:
        # Cierra la conexión
        if "conn" in locals():
            conn.close()