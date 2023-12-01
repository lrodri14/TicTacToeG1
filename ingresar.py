import mysql.connector
from registro import RegistroUsuario

class IngresarUsuario:
    def __init__(self, Nombre, Contraseña):
        self.Nombre = Nombre
        self.Contraseña = Contraseña

    def validar_ingreso(self):
        try:
            connection = mysql.connector.connect(
                user='progsistemasabiertos', password='RootProgsistemasabiertos',
                host='178.128.156.175',
                database='psa1_tictactoe',
                port='3306',
            )

            cursor = connection.cursor()


            query = "SELECT * FROM Jugadores WHERE Nombre = %s AND Contraseña = %s"
            values = (self.Nombre, self.Contraseña)
            cursor.execute(query, values)

            if cursor.fetchone():
                print("Ingreso exitoso")
            else:
                print("Error: Usuario o contraseña incorrectos")

        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

if __name__ == "__main__":

    ingreso1 = IngresarUsuario("Armando", "contraseña123")
    ingreso1.validar_ingreso()
