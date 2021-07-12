class alumno():
    def __init__(self,
                 codigo_alumno,
                 nombres,
                 dni,
                 edad,
                 email,
                 id_salon = 0):
        self.codigo_alumno = codigo_alumno
        self.nombres = nombres
        self.dni = dni
        self.edad = edad
        self.email = email
        self.id_salon = id_salon
    
    def __str__(self) -> str:
        return f"{self.codigo_alumno} - {self.nombres}"
