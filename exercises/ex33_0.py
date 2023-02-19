def printNum(i, step):
    end = 6
    numbers = []
    while i < end:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + step
        print("Numbes now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

printNum(0, 2)
