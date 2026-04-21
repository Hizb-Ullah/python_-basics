name1=(input("Enter item 1 name:"))
price1=float(input("Enter item 1 price:"))
name2=str(input("Enter item 2 name:"))
price2=float(input("Enter item 2 price:"))
name3=str(input("Enter item 3 name:"))
price3=float(input("Enter item 3 price:"))

subtotal=price1+price2+price3
tax=subtotal*0.1
total=subtotal+tax

print(f"====BILL RECIEPT====:")
print(f"Item 1 :{name1} -Rs. {price1:.2f}")
print(f"Item 2 :{name2} -Rs. {price2:.2f}")
print(f"Item 3 :{name3} -Rs. {price3:.2f}" )
print("-----------------------------------")
print(f"Subtotal :Rs. {subtotal:.2f}")
print(f"Tax (10%) :Rs.{tax:.2f}")
print("-----------------------------------")
print(f"Total : Rs.{total:.2f}")
print(f"====================END====================")