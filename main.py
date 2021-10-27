from datetime import datetime

name = input("enter your name:")

lists = '''
rice Rs 30/kg
dal Rs 25/kg
sugar Rs 30/kg
salt Rs 20/kg
oil Rs 80/liter
pannier Rs 120/kg
maggi Rs 30/pack
boost Rs 90/each
colgate Rs 85/each
'''
price = 0
pricelist = []
totalprice = 0
ilist = []
qlist = []
plist = []

items = {
         'rice':30,
         'dal':25,
         'sugar':30,
         'salt':20,
         'oil':80,
         'pannier':120,
         'maggi':30,
         'boost':90,
         'colgate':85
         }
option = int(input('list of items press 1:'))
if option == 1:
    print(lists)
    for inp1 in range(len(items)):
        inp1 = int(input('if you want to buy press 1 or 2 for exit:'))
        if inp1 == 2:
            break
        if inp1 == 1:
            item = input('Enter your items:')
            quantity = int(input('Enter quantity :'))
            if item in items.keys():
                price = quantity * (items[item])
                pricelist.append([item, quantity, items, price])
                totalprice += price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                gst = (totalprice*5)/100
                finalamount=gst + totalprice
            else:
                print('sorry! you entered item is not available')
        else:
            print('you entered wrong number')
        inp1 = input('can i bill the items yes or no')
        if inp1 == 'yes':
            pass
            if finalamount != 0:
                print(25*'=', 'd-mart', 25*'=')
                print(28*' ', 'electronic-city')
                print('name:', name, 30*' ', 'Date', datetime.now())
                print(75*'-')
                for i in range(len(pricelist)):
                    print(i,8*' ', 8*' ', ilist[i],3*' ',8*' ', qlist[i],5*' ', plist[i])
                print(75*' ')
                print(50*' ','TotalAmount:', 'RS', totalprice)
                print('gst amount', 50*' ', 'RS', gst)
                print(75*'-')
                print(50*' ', 'FinalAmount:', 'RS', finalamount)
                print(75*'-')
                print(50*' ', 'Thanks for visiting')
                print(75*'-')
