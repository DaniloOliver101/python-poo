i = 0
contador = int(input("Informe a quantidade de vezes que deseja calcular o IMC: "))
for i in range(contador):
    peso = float(input("Informe o peso: "))
    altura = float(input("Informe a altura: "))
    
    if peso <= 0 or altura <= 0:
        print("Peso e altura devem ser maiores que zero")
    elif peso > 200 or altura > 2.5:
        print("Peso e altura fora do padrão")
    else:
        imc = peso / (altura * altura)
        print(f"O IMC é {imc:.2f}")
        
        if imc < 18.5:
            print("Abaixo do peso")
        elif 18.5 <= imc < 25:
            print("Peso normal")
        elif 25 <= imc < 30:
            print("Sobrepeso")
        elif 30 <= imc < 35:
            print("Obesidade grau 1")
        elif 35 <= imc < 40:
            print("Obesidade grau 2")
        else:
            print("Obesidade grau 3")
    
    resp = input("Deseja calcular o IMC novamente? sim ou não: ")
    if resp.lower() != 'sim':
        break
