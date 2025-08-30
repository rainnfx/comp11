def checkout(price):
    total = price * 1.12
    print(f"It will cost ${total}")
    
print("What will you buy?")
print("[a] Salt - $1.40")
print("[b] Pepper = $2.20")

choice = input("Choice: ")

if choice == "a":
    checkout(1.40)
elif choice == "b":
    checkout(2.20)
else:
    print("Sorry! We don't have that item at the moment.")
