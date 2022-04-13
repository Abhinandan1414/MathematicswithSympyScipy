'''
Gallon_to_USGallon_to_Litre.py
Unit converter from Gallon to USGallon and Litre:
1 US Gallon is 3.785 litre
1 Gallon is 4.546 litre
1 Gallon is 1.201 US Gallon
'''
def choicechart():
    print('-----------Choice Chart-------------------------------')
    print('1. Gallon to Litre')
    print('2. Litre to Gallons')
    print('3. USGallons to Litre')
    print('4. Litre to USGallons')
    print('5. Gallon to USGallon')
    print('6. USGallon to Gallon')
    print('7. Exit')
    print('------------------------------------------------------')

def gallontolitre():
    gallons = float(input('Enter the liquid volume in gallons :'))
    litres = gallons*4.546
    print('{0} Gallons is {1} Litres'.format(gallons,litres))

def litretogallon():
    litres = float(input('Enter the liquid volume in liters : '))
    gallons= litres / 4.546
    print('{0} Liters is {1} Gallons'.format(litres,gallons))

def usgallontolitre():
    usgallons = float(input('Enter the liquid volume in usgallons: '))
    litres = usgallons*3.785
    print('{0} USGallons is {1} Litres'.format(usgallons,litres))

def litretousgallon():
    liters = float(input('Enter the liquid volume in liters : '))
    usgallons= liters / 3.785
    print('{0} Liters is {1} USGallons'.format(liters,usgallons))

def usgallontogallon():
    usgallons = float(input('Enter the liquid volume in usgallons: '))
    gallons = usgallons/1.201
    print('{0} USGallons is {1} Gallons'.format(usgallons,gallons))

def gallontousgallon():
    gallons = float(input('Enter the liquid volume in gallon : '))
    usgallons= gallons * 1.201
    print('{0} Gallons is {1} USGallons'.format(gallons,usgallons))

if __name__ == '__main__':
 while True:
    choicechart()
    choice = input("Which conversion would you like to do? ")
    if choice == '1':
        gallontolitre()
    if choice == '2':
        litretogallon()
    if choice == '3':
        usgallontolitre()
    if choice == '4':
        litretousgallon()
    if choice == '5':
        gallontousgallon()
    if choice == '6':
        usgallontogallon()
    if choice == '7':
        break
