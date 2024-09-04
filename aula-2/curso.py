class Curso:
    def __init__(self, nome, carga_horaria, categoria):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.categoria = categoria

    def __str__(self):
        return f"{self.nome} ({self.categoria}) - {self.carga_horaria}h"