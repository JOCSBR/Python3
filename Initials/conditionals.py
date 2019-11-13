# conditionals

age = int(input('Enter age: '))
genre = input('Enter genre M or F: ').lower()

if genre == 'm':
    if age > 18: print('Man > 18')
    else: print('Man <= 18')
elif genre == 'f':
    if age > 18: print('Woman > 18')
    else: print('Woman <= 18')
else: print('Unrecognized data')


# if age > 18 and genre == 'm':
#     print('Man > 18')
# elif age <= 18 and genre == 'm':
#     print('Man <= 18')
# elif age > 18 and genre == 'f':
#     print('Woman > 18')
# elif age <= 18 and genre == 'f':
#     print('Woman <= 18')
# else: print('Unrecognized data')


# if age == 18:
#     print('Age equal 18')
# elif age == 17:
#     print('Age iqual 17')
# else:
#     print('Age is not 17 or 18')
# 
# if age != 20:
#     print('Age is not = 20')

# x = -1
# if x: print('less than 0')
# x = 0
# if x: print('zero')
# x = 1
# if x: print('greather than 0')
#  
# lista1 = []
# if lista1: print('Lista OK') 
# else: print('Lista empty')
#  
# lista1.append(' ')
# if lista1: print('Lista OK') 
# else: print('Lista empty')