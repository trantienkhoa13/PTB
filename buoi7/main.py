import random
number = random.randint(0,1000)
x = int (input ("nhap so: "))

while x != number:
    if x == -1:
        break
    if x < 0 or x > 1000:
        print ("vui long nhap so tu 0 den 1000")
        continue
    if x < number:
        print ("so can tim lon hon x")
    elif x > number:
        print ("so can tim nho hon x")
    x = int (input ("nhap so: "))

print ("ban da nhap dung")
# print ("ban da doan dung")
# username = "khoa"
# ps = "12345"

# inputus = input("nhập tên:")
# inputps = input("nhập mật khẩu:")
# while inputus != username or inputps != ps:
#     inputus = input("nhập tên:")
#     inputps = input("nhập mật khẩu:")
# print("dang nhap thanh cong")