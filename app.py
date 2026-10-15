
import os
from dotenv import load_dotenv

load_dotenv()


def get_password():
    password = os.getenv("APP_PASSWORD")
    if not password:
        raise RuntimeError("APP_PASSWORD n'est pas configuré")
    return password


def calculate(a: float, b: float, operation: str) -> float:
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        if b == 0:
            raise ValueError("Division par zéro")
        return a / b
    raise ValueError("Opération non autorisée")


def main():
    try:
        a = float(input("Premier nombre : "))
        b = float(input("Deuxième nombre : "))
        operation = input(
            "Opération (add, subtract, multiply, divide) : "
        ).strip().lower()

        result = calculate(a, b, operation)
        print(f"Résultat : {result}")
    except ValueError as error:
        print(f"Erreur : {error}")


if __name__ == "__main__":
    main()
