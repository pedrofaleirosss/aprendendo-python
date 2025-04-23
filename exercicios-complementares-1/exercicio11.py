x = int(input("Digite o valor de x: "))

if x <= 1:
    print("f(x) = 1")
elif 1 < x <= 2:
    print("f(x) = 2")
elif 2 < x <=3:
    print(f"f(x) = {x ** 2}")
else:
    print(f"f(x) = {x ** 3}")