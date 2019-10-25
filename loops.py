# loops

fatura = []
total = 0
product = ''
 
while product != 'x':
    product = input('Input product: ').lower()
    if product == 'x':
        break
    price = float(input('Input price: '))
    fatura.append([product, price])
    total += price
 
for i in fatura:
    print(i[0], i[1])
print('Total =',total)


# products = []
# prices = []
# fatura = {}
# counter = 0
# product = ''
# 
# while product != 'x':
#     product = input('Input product: ')
#     if product == 'x':
#         break
#     price = int(input('Input price: '))
#     products.append(product)
#     prices.append(price)
#     counter += 1
# 
# counter = 0
# total = 0
# for i in products:
#     print(products[counter], prices[counter])
#     total += prices[counter]
#     counter += 1
# print('Total =',total)


# for i in range(0,10):
#     print(i, 10-i)

# letters = [['a','b','c'],['x','y','z'],['1','2']]
# for i in letters:
#     for item in i:
#         print(i, item)
        

# colors = {'green':'verde', 'blue':'azul', 'red':'vermelho', 'yellow':'amarelo'}
# for i in colors:
#     print(i, colors[i])


# sales = [100, 200, 450, 330, 569]
# total = 0
# for i in sales:
#     total += i
#     print(i, 'total =',total)

# list1 = ['a','b','c','d','e']
# for i in list1:
#     print(i)

# x = 0
# people = []
# 
# while 'x' not in people:
#     name = input('Input name: ')
#     if name == 'x':
# #         continue
#         break
#     people.append(name)
# print(people)


# while x < 4:
#     nome = input('Input name ')
#     x += 1
#     people.append(nome)
#     print(nome, x)
#     print(people)
# print(x)
