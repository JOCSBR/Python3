# tupple
monthsnames = ('jan','fev','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')

# input + print
dtnascim = input('Birth date DD-MM-YYYY')
mesnascim = int(dtnascim[3:5])
print('Birth month =',monthsnames[mesnascim-1])


print(monthsnames)
print(type(monthsnames))
print(len(monthsnames))
print(monthsnames[0])

#list
people = ['john','mary','peter','louis']
people2 = ['sara','shanna']
print(people)
print(type(people))
print(len(people))  # qtty elements of list
print(people[0])
people[1] = 'marylu'    # get by index
print(people)
people.append('richard')    # insert last
print(people)
people.insert(1, 'paul')    # insert by index
print(people)
people.sort()   # sort ascending
print(people)
people.pop(1)   # revove by index
print(people)
people.remove('peter')  # remove by content
print(people)
totalpeople = people + people2  # sum lists
print(totalpeople)
posicao = 3
print(totalpeople[posicao]) # get from variable


