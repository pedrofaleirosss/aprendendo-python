letra = input("Digite uma letra minúscula: ")

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("A letra é vogal.")
    case _:
        print("A letra é consoante.")