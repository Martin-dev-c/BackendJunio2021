
class profesor:
    def __init__(self,codigo_profesor,nombres,dni,edad,email):
        self.codigo_profesor = codigo_profesor
        self.nombres = nombres
        self.dni = dni
        self.edad = edad
        self.email = email
    
    def __str__(self) -> str:
        return f"{self.codigo_profesor} - {self.nombres}"
