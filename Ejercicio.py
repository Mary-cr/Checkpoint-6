class Usuario:
    def __init__(self, nombre_de_usuario, contraseña):
        self.nombre_de_usuario = nombre_de_usuario
        self.contraseña = contraseña


Usuario = Usuario("Cecilia_Ramos", "55123MC")

print(Usuario.nombre_de_usuario)
print(Usuario.contraseña)
