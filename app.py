# solicitar ao usuário seu peso e altura
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))

# calcular o IMC (BMI)
imc = peso / (altura ** 2)

# exibir o resultado
print("Seu IMC é: {:.2f}".format(imc))

# interpretar o IMC (BMI)
if imc < 18.5:
    print("Você está abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Seu peso está saudável")
elif 24.9 <= imc < 29.9:
    print("Seu peso está acima do peso")
else:
    print("Você está obeso")