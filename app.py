

import ast
import operator

OPERATIONS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def calculer(expression):
    arbre = ast.parse(expression, mode="eval").body

    def evaluer(noeud):
        if isinstance(noeud, ast.Constant) and type(noeud.value) in (int, float):
            return noeud.value

        if isinstance(noeud, ast.BinOp) and type(noeud.op) in OPERATIONS:
            gauche = evaluer(noeud.left)
            droite = evaluer(noeud.right)

            if isinstance(noeud.op, ast.Div) and droite == 0:
                raise ValueError("Division par zéro")

            return OPERATIONS[type(noeud.op)](gauche, droite)

        raise ValueError("Expression non autorisée")

    return evaluer(arbre)


def get_message():
    user_input = input("Entrez une expression : ")

    try:
        result = calculer(user_input)
        return f"Résultat : {result}"
    except (ValueError, SyntaxError, ZeroDivisionError, OverflowError):
        return "Erreur : expression invalide ou non autorisée."


if __name__ == "__main__":
    print(get_message())
