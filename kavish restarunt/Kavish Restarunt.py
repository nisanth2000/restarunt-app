#Kavish Restarunt
#
menu={
    'chicken_ roll':100,
    'chicken_momos':100,
    'pizza':150,
    'sweet pizza':100,
    'chicken pizza':200,
    'burger':80,
}
print("welcome to Kavish Restarunt")
print("chicken roll: Rs100\nchicken momos: Rs100\npizza: Rs150\nsweet pizza: Rs100\nchicken pizza: Rs200\nburger: Rs80")

order_total = 0
            
item_1=input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1}is not available yet!")
another_order = input("Do you want to add another item?(yes/no)")
if another_order =="yes":
    item_2 = input("Enter the name of another item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2}is not available yet!")



print(f"The total amount of items to is {order_total}")
    
                

          


