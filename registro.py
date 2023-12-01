import mysql.connector
#pip install mysql-connector-python

class RegistroUsuario:
    def __init__(self, Nombre, Contraseña, verify_Contraseña, Correo):
        self.Nombre = Nombre
        self.Contraseña = Contraseña
        self.verify_Contraseña = verify_Contraseña
        self.Correo = Correo

    def validar_registro(self):
        if self.Contraseña == self.verify_Contraseña:
            self.guardar_en_base_datos()
            print("Registro exitoso")
        else:
            print("Error: Las contraseñas no coinciden")

    def guardar_en_base_datos(self):
        try:
            connection = mysql.connector.connect(
                user='progsistemasabiertos', password='RootProgsistemasabiertos',
                host='178.128.156.175',
                database='psa1_tictactoe',
                port='3306',
            )

            cursor = connection.cursor()


            query = "INSERT INTO Jugadores (Nombre, Contraseña, Correo) VALUES (%s, %s, %s)"
            values = (self.Nombre, self.Contraseña, self.Correo)
            cursor.execute(query, values)

            connection.commit()

        except Exception as e:
            print(f"Error al guardar en la base de datos: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

if __name__ == "__main__":

    registro1 = RegistroUsuario("Juan", "contraseña123", "contraseña123", "maria@hotmail.com")
    registro1.validar_registro()
