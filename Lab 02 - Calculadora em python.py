print("\n*******************Calculadora em Python************************\n")

print("\nSelecionae o número da operação desejada:\n")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("\nDigite uma das opções acima:\n")
numero1 = int(input("\nDigite primeiro número : \n"))
numero2 = int(input("\nDigite segundo número : \n"))

if operacao == "1":
    soma = numero1 + numero2
    print(f'{numero1} + {numero2} = {soma}')
elif operacao =="2":
    sub = numero1 - numero2
    print(f'{numero1} - {numero2} = {sub}')
elif operacao =="3":
    multp = numero1 * numero2
    print(f'{numero1} * {numero2} = {multp}')
elif operacao =="4":
    divs = numero1 + numero2
    print(f'{numero1} / {numero2} = {divs}')
else:
    print("Operação não identificada, escolha uma opção de 1 a 4")