from pessoa import Pessoa
from cliente import Cliente
from cao import Cao
from curso import Curso 

carlos = Pessoa()
carlos.nome = "Carlos"
carlos.idade = 30
carlos.sexo = "M"

print(F"{carlos.nome} tem {carlos.idade} anos e é do sexo {carlos.sexo}")

maria = Pessoa()
maria.nome = "Maria"
maria.idade = 25
maria.sexo = "F"

print(F"{maria.nome} tem {maria.idade} anos e é do sexo {maria.sexo}")

ernani = Cao()
ernani.nome = "Ernani"
ernani.idade = 3
ernani.sexo = "M"
ernani.raca = "Poodle"

print(F"{ernani.nome} tem {ernani.idade} anos, é do sexo {ernani.sexo} e da raça {ernani.raca}")

regina = Cao()
regina.nome = "Regina"
regina.idade = 2
regina.sexo = "F"
regina.raca = "Vira-lata"

print(F"{regina.nome} tem {regina.idade} anos, é do sexo {regina.sexo} e da raça {regina.raca}")

rogerio  =  Cliente()
rogerio.nome = "Rogerio"
rogerio.idade = 40
rogerio.sexo = "M"
rogerio.cpf = "123.456.789-00"


print(F"{rogerio.nome} tem {rogerio.idade} anos, é do sexo {rogerio.sexo} e tem o CPF {rogerio.cpf}")
curso_python = Curso("Python", 40, 20)

print(str(curso_python))


