# a = int (input ("nhập số kẹo :"))
# b = int (input ("nhập số em bé :"))
# if a % b == 0 :
#     print ("có")
# else :
#     print ("không")

print ("nhập chiều cao 3 bạn :")
an = int (input ("An :"))
minh = int (input ("Minh :"))
lan = int (input ("Lan :"))
max = an 
if an < minh :
    max = minh
if lan > minh :
    max = lan

if  an == minh & minh == lan &  lan == an :
    print ("3 bạn cao bằng nhau")
elif max == an :
    print ("Bạn cao nhất là An")
elif max == lan :
    print ("Bạn cao nhất là Lan")
elif max == minh :
    print ("Bạn cao nhất là Minh")