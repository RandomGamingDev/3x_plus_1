while True:
    number = int(input("Input your number: "))
    i = 0;
    while number != 1:
        if number % 2:
            number*=3
            number+=1
        else:
            number/=2
        i+=1
        print(f"{i}: {number}")
    print(f"It took {i} steps to get to 1")
