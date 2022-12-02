import sqlite3

con = sqlite3.connect('image.db')
cursor = con.cursor()
data = 'pop'

# cursor.execute("create table image (image BLOB, info varchar(30))")
with open("C:\\Users\\ompra\\Pictures\\wallpaper\\Prince-Of-Persia-3.jpg", 'rb') as image:
    img = image.read()
    # print(img)

# used for inserting the data in the table
# cursor.execute("insert into image values(?, ?)", (img, data))

# now retrieving the data from the table

c = cursor.execute("select * from image ")
for i in c:
    # print(i)
    pic = i[0]
with open("writing image.png", 'wb') as w:
    w.write(pic)

con.commit()

cursor.close()
con.close()
