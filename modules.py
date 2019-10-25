def imc(peso,altura):
    imc = peso / (altura*altura)
    return imc
 
def class_imc(sexo,peso,altura):
    valor_imc = imc(peso,altura)
# 
#     if sexo == 'm':
#         if valor_imc < 20.7:
#             return "Abaixo do peso"
#         elif valor_imc >= 20.7 and valor_imc < 26.4:
#             return "Peso normal"
#         elif valor_imc >= 26.4 and valor_imc < 27.8:
#             return "Marginalmente acima do peso"
#         elif valor_imc >= 27.8 and valor_imc < 31.1:
#             return "Acima do peso ideal"
#         elif valor_imc >= 31.1:
#             return "Obesidade"
#         else:
#             return "Erro de calculo. Entre em contato com o administrador"
# 
#     if sexo == 'f':
#         if valor_imc < 19.1:
#             return "Abaixo do peso"
#         elif valor_imc >= 19.1 and valor_imc < 25.8:
#             return "Peso normal"
#         elif valor_imc >= 25.8 and valor_imc < 27.3:
#             return "Marginalmente acima do peso"
#         elif valor_imc >= 27.3 and valor_imc < 32.3:
#             return "Acima do peso ideal"
#         elif valor_imc >= 32.3:
#             return "Obesidade"
#         else:
#             return "Erro de calculo. Entre em contato com o administrador"

import funcmodules as f

print('Vamos calcular o seu imc?')

valid_sexo = False
while valid_sexo == False:
    sexo = input('Digite o seu sexo (M ou F): ').lower()
    if sexo != 'm' and sexo != 'f':
        print('Sexo invalido. Digite M ou F.')
    else:
        valid_sexo = True
        print('\n')

valid_peso = False
while valid_peso == False:
    peso = input('Digite o peso (ex. 68.5): ')
    try:
        peso = float(peso)
        if peso <= 0 or peso > 350:
            print('Peso invalido. Numero nao pode ser zero ou negativo e deve ser inferior a 350.')
        else:
            valid_peso = True
            print('\n')
    except:
        print('Peso invalido. Use apenas numeros e separe os decimais com ponto.')

valid_altura = False
while valid_altura == False:
    altura = input('Digite a altura em metros (ex. 1.70): ')
    try:
        altura = float(altura)
        if altura <= 0 or altura > 3:
            print('Altura invalida. Numero nao pode ser zero ou negativo e deve ser inferior a 3 metros.')
        else:
            valid_altura = True
            print('\n')
    except:
        print('Altura invalida. Use apenas numeros e separe os decimais com ponto.')


v_imc = str(f.imc(peso,altura))
c_imc = f.class_imc(sexo,peso,altura)

print('O seu IMC e:',v_imc[0:5])
print('A sua classificacao e:',c_imc)
