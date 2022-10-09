message = input()
blacklist = ["male", "female", "Hindu", " Muslim", "Christian", "BMP", "Awami league"]
brandName = {"bmw": 0, "toyota": 0}
xLevel = []
yLevel = []
x = xLevel
y = yLevel
message1 = message
message1 = message1.split(" ")
# print(message1)  # to check the list
for i in message1:  # this splits the whole text
    # print(i)
    if i in blacklist:
        # print(i)
        index = message1.index(i)
        # print(type(index))
        message1[index] = "*" * len(i)
        # print(message1[index])
    for brand in brandName:
        # print(brand)
        if brand in message1:
            # print(brand)
            brandName[brand] += 1
            x.append(brandName[brand])
            # print(f"This is x value {x}")
            y.append(brand)
            # print(f"this is y value {y}")
message = " ".join(message1)
# print(message)
print(xLevel)
print(yLevel)
