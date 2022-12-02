img1 = open("Figure_1.png", "rb").read()
img2 = open("Figure_2.png", "rb").read()

if img1 == img2:
    print("item = Margo soap")
    print("price = 120")
else:
    print("No data found")
