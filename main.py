import calculator

if __name__ == "__main__":
    a, b = 4, 2
    print(f"{a} + {b} = {calculator.addition(a,b)}")
    print(f"{a} - {b} = {calculator.subtraction(a,b)}")
    print(f"{a} * {b} = {calculator.multiplication(a,b)}")
    print(f"{a} / {b} = {calculator.divison(a,b)}")
