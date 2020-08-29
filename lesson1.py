select = 0
while True:
    select = int(input("Enter task number(1-6) , 7 to exit: "))
    if select == 7:
        print("Done...")
        break
    if 0 <= select > 6:
        print("Wrong enter...")
        continue
    elif select == 1:
        print("not ready")
    elif select == 2:
        secs = int(input("Enter seconds: "))
        print(f"{secs // 3600 :02} : {secs % 3600 // 60 :02} : {secs % 3600 % 60 :02}")
    elif select == 3:
        number = input("Enter number: ")
        n1 = int(number)
        n2 = int(number+number)
        n3 = int(number+number+number)
        print(f"{n1} + {n2} + {n3} = {n1 + n2 + n3}")
    elif select == 4:
        number = int(input("Enter number: "))
        maxNumber = 0
        while number > 0:
            tmp = number % 10
            if tmp > maxNumber:
                maxNumber = tmp
            number = number // 10
        print(f"Max is : {maxNumber}")
    elif select == 5:
        print("not ready")
    elif select == 6:
        a = float(input("Enter first day kilometers: "))
        b = int(input("Enter target distance: "))
        day = 1
        while True:
            print(f"{day}: {a:.2f}")
            if a > b:
                break
            a += a * 0.1
            day += 1





