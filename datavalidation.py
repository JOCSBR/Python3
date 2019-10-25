fatura = []
total = 0
product = ''
valid_price = False

while product != 'x':
    product = input('Input product: ').lower()
    if product == 'x':
        break
    while valid_price == False:
        price = input('Input price: ')    
        try:
            price = float(price)
            if price <= 0:
                print('Please price >0')
            else:
                valid_price = True
        except:
            print("Invalid format, only numbers and '.'")
    
    fatura.append([product, price])
    total += price
    valid_price = False
 
for i in fatura:
    print(i[0], i[1])
print('Total =',total)
