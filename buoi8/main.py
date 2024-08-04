gamename = ["mario","minecraft","eldenrings"]
gameprice = [20,30,50]
money = 1000
giagame = []
giohang = []

while True :
    print ("1. các game trong giỏ hàng (shop)")
    print ("2. xem giỏ hàng")
    print ("3. thêm game vòa giỏ hàng")
    print ("4. thêm game vào cửa hàng (shop)")
    print ("5. bỏ game ra khỏi cửa hàng (shop)")
    print ("6. bỏ game ra khỏi giỏ hàng")
    print ("7. sửa giá iphone (shop)")
    print ("8. xóa hết giỏ hàng")
    print ("9. thanh toán")
    n = int(input ("nhập lựa chọn :"))
    if n == 1:
        for i in range (len (gamename)):
            print(gamename[i],"-",gameprice [i],"$")
        x = input()
    elif n == 2:
        print ("gio hang cua ban:")
        for i in range (len (giohang)):
            print (giohang [i])
        x = input ()
    elif n == 3:
        for i in range (len (gamename)):
            print(gamename[i],"-",gameprice [i],"$")
        n = int(input ("nhập game bạn muốn mua bắt đầu từ 0:"))
        giohang.append(gamename [n])
        giagame.append(gameprice [n])
        print ("đã thêm vào giỏ hàng",gamename [n])
        x = input ()
    elif n == 4:
        for i in range (len (gamename)):
            print(gamename[i],"-",gameprice [i],"$")
        newgame = input ("nhập tên game muốn bán")
        newprice = int (input ("nhập giá tiền game mới"))
        gamename.append (newgame)
        gameprice.append (newprice)
        print ("đã thêm ",newgame,"với mức giá",newprice)
    elif n == 5:
        for i in range (len (gamename)):
            print(gamename[i],"-",gameprice [i],"$")
        vitrixoa = int (input ("nhập game muốn xóa ( bắt đầu tại 0):"))
        print ("đã xóa game", gamename [vitrixoa],"khỏi cửa hàng")
        gamename.pop (vitrixoa)
        gameprice.pop (vitrixoa)
        x = input
    elif n == 6:
        for i in range (len (gamename)):
            print(gamename[i],"-",gameprice [i],"$")
        vitrixoa = int (input ("nhập game muốn xóa khỏi giỏ hàng ( bắt đầu tại 0):"))
        print ("đã xóa game", gamename [vitrixoa],"khỏi giỏ hàng")
        giohang.pop (vitrixoa)
        giagame.pop (vitrixoa)
        x = input
    elif n == 7:
        for i in range (len (gamename)):
            print(gamename[i],"-",gameprice [i],"$")
        vitrisua = int (input ("nhập game muốn đổi giá ( bắt đầu tại 0):"))
        newprice =int (input ("nhập giá mới của" + gamename [vitrisua]))
        gameprice = [vitrisua] = newprice
        print ("đã sữa giá")
        x = input
    elif n == 8:
        luachon = input ("bạn có muốn xóa hết giỏ hàng không (y/n)")
        if (luachon == 'y' or luachon == 'Y'):
            giohang.clear()
            print ("đã xóa hết giỏ hàng")
            x = input()
    elif n == 9:
        pay = 0
        for gamepay in giagame:
            pay += gamepay
        money -= pay
        print ("các game bạn đã mua",giohang,"voi tong tien la",pay)
        print ("sô tiền còn lại:",money)
        giohang.clear()
        x = input()
