#functions

def imc(weight, size):
    val_imc = weight / (size**2)
    return(val_imc)

if imc(120,1.79) > 32:
    print('Obeso')
else: print('OK')
print('\n')

# def imc(weight, size):
#     val_imc = weight / (size*size)
#     print(val_imc)
#
# imc(120,1.79)

# user = 'joao'
# def message(name):
#     print('Welcome ' + name.title())
#
# message(user)


# def message():
#     print('Welcome!')
# message()
