#  so = int (input ())
# if so % 3 == 0:
#     print (so ,"chia het cho 3",end = "")
# else :
#     print (so ,"chia 3 du",so % 3,end = "")



# so = int (input ())
# j = int (input ())
# to = 0
# for i in range (so,j + 1):

#     if i % 2 == 0:
#         to += i

# print (to)
# j = int (input ())
# i = int (input ())
# for j in range (1,j + 1):
#     for i in range (1,i + 1):
#         print ("*",end = '')
#     print(" ")


# i = int (input ())
# for a in range (1,11) :
#     print (str(i)+"x"+ str(a)+ "="+str(i * a),end = '')


# i = int (input ())
# for j in range (1,i + 1):
#     for k in range (1,j + 1):
#         print ("*",end = '')
#     print ("")


i = int (input())
to = 0
for j in range (1,i + 1):
    if j % 3 == 0:
        to += j

print (to)