
def height_of_christmas_tree(n):
    x = 0
    y = 0
    while x <= n:
        print(" "*(n-y) + "*"*(2*x-1))
        x +=1
        y +=1
    print(" "*(n-1) + "*")
    print(" "*(n-1) + "*")
    print(" "*(round(n/2)) + "_"*(n))
    print(" "*(n-8) + "Merry Christmas!")


height_of_christmas_tree(int(input("How tall would you like your tree? ")))
