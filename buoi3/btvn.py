# n = int (input ("số kẹo thầy đang có:"))
# m = int (input ("số học sinh đang có:"))
# print ("số kẹo mỗi bạn nhận được:", n // m)
# print ("số kẹo còn thừa:", n % m)

s = int (input ("số giây:"))
h = s // 3600
s = s % 3600
m =  s //  60
s = s % 60
print ("chuyển đổi:",h,"giờ",m,"phút",s,"giây")