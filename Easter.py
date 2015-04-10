year = int(input())
a = (19 * (year % 19) + 15) % 30
b = (2 * (year % 4) + 4 * (year % 7) + 6 * a + 6) % 7
if a + b > 9:
    t = a + b - 9
    if (t + 13 < 31):
        print ( "the", t + 13, "of" , "April")
    else:
        print ( "the", t + 13 - 30, "of" , "May")
else:
    t = 22 + a + b + 13 - 31
    print ( "the", t, "of" , "April")
