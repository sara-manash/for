# eded daxil edirik
number = int(input("Ededi daxil edin: "))


# eded menfi olsa
if number < 0:
    print("Menfi ededlerin faktoriali yoxdur.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    print(f"{number}! = {factorial}")