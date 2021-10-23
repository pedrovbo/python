#Programa para cálculo de IMC
print('Programa para cálculo do IMC')
peso = float(input('Entre com seu peso: '))
altura = float(input('Entre com sua altura: '))
imc = peso/altura**2
#print(imc)

if(imc < 18.5):
    print('Você está magro(a).')
if(imc > 18.5 and imc < 24.9):
    print('Você está no peso normal.')
if(imc > 25.0 and imc < 29.9):
    print('Você está sobrepeso.')
if(imc > 30.0 and imc < 39.9):
    print('Você está obeso.')
if(imc > 40):
    print('Você está gravemente obeso.')

print('Fim do Programa')