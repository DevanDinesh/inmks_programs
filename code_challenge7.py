def student(price):
    price=price-(price*10)/100
    return price

def student2(price1):
    price1=price1-(price1*5)/100
    return price1
price=int(input("Enter the price:"))
print(student2(student(price)))