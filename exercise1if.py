copies = int(input("Enter number of copies :"))

if copies <= 99:
    price = 0.30
elif 100 <= copies <= 499:
    price = 0.28
elif 500 <= copies <= 749:
    price = 0.27
elif 750 <= copies <= 1000:
    price = 0.26
else:
    price = 0.25

print("Price per copy is : R" + str(price))

totalCost = price * copies
print("Total cost is : R" + str(totalCost))
