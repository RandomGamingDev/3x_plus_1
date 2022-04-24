while True:
    number = int(input("Input your number: "))
    i = 1;
    while number != 1:
        if number % 2:
            number*=3
            number+=1
        else:
            number/=2
        print(f"{i}: {number}")
        i+=1
    print(f"It took {i} steps to get to 1")