leng_a = int(input("Enter length a: "))

width_a = int(input("Enter width a: "))


if leng_a < 5 or leng_a > 12:
    print("Please enter the length within 5-12")
    if leng_a < 5:
        print("The length is too small")
    else:
        print("The length is too big")
elif width_a < 0 or width_a > 20:
    print('The width is out of bounds')
    if width_a < 0:
        print('The width is too small')
    else:
        print("The width is too big")
else:
    print("Rectangle A area = ", format(leng_a * width_a, '.3f'), 'sq.m')
