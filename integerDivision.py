while True:
    try:
        a = int(input("Enter first integer: "))
        b = int(input("Enter second integer: "))
        c = a/b
    except ValueError:
        print("Input is not an integer")
    except ZeroDivisionError:
        print("Second input can't be zero.")
    else:
        print(c)
        print("Operation Successful")
    finally:
        print("Operation Completed")
        