valor_compra = float(input('Digite o valor da compra: '))
quantidade_parcelas =  int(input('Digite a quantidade de parcelas: '))
juros = float(input('Digite o valor do juros: '))

def calcular_parcelas(valor_compra, quantidade_parcelas,taxa_juros):
    if(quantidade_parcelas>1):
        valor_compra = valor_compra * 1.05
    
    valor_parcela = valor_compra / quantidade_parcelas
    return valor_parcela


valor_parcela = calcular_parcelas(valor_compra, quantidade_parcelas, juros)
print(f'O valor da parcela é {valor_parcela:.2f}')
