# Calculadora de Python

# Perguntar ao usuário qual o tipo de operação
# Perguntar o primeiro número
# Perguntar o segundo número
# Cálculo desses dois números
# Imprimir o resultado na tela

while True:
    operacao = input(
        'Qual operação (+, -,*,/) você quer fazer? ou digite \'s\' para sair ')
    if operacao == 's' or operacao == 'S':
        break
    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    else:
        print('Operação inválida')

    if operacao == '+':
        total = num1 + num2
        print(total)
    elif operacao == '-':
        total = num1 - num2
        print(total)
    elif operacao == '*':
        total = num1 * num2
        print(total)
    elif operacao == '/':
        total = num1 / num2
        print(total)
   

