#Kerwin Aguilar
#CMP131-86520
#Week-05
#lab-01
#Temperature Category
#09/30/26
temp=float(input('Enter temperature in Fahrenheit: '))
if temp <50:
    print(f'{temp} is cold')
elif 50<= temp <80:
    print(f'{temp} is warm')
elif temp >=80:
    print(f'{temp} is hot')