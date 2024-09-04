resp = "sim"
imc = 00
while resp == "sim":
    peso = float(input("informe o peso"))
    altura = float(input("informe a altura"))
    if(peso  <= 0 or altura <= 0):
        print("Peso e altura devem ser maiores que zero")


    elif(peso > 200 or altura > 2.5):
        print("Peso e altura fora do padrão")
    imc = peso / (altura * altura)
    print(f"O IMC é {imc}")
    
    if(imc < 18.5):
        print("Abaixo do peso")
    elif(imc >= 18.5 and imc < 25):
        print("Peso normal")
    elif(imc >= 25 and imc < 30):
        print("Sobrepeso")
    elif(imc >= 30 and imc < 35):
        print("Obesidade grau 1")
    elif(imc >= 35 and imc < 40):   
        print("Obesidade grau 2")
    else:
        print("Obesidade grau 3")
        
    resp = input("Deseja calcular o IMC novamente? sim ou não")