from typing import Callable


def truth_table(operator: str, f: Callable[[bool, bool], bool]):
    """
    Donne la table de vérité de l'opérateur
    """
    list_bool: list[bool] = [False, True]
    for i in list_bool:
        for j in list_bool:
            print(f"{i} {operator} {j} = {f(i, j)}")


if __name__ == "__main__":
    truth_table("&", lambda x, y: x and y)
    truth_table("|", lambda x, y: x or y)
    truth_table("^", lambda x, y: x ^ y)


def alphabetical_order(word: str):
    """
    Ecrit le mot avec les lettres dans l'ordre alphabétique
    """
    alpha_word: list[str] = []
    while word:
        i = None
        m = None
        for j, k in enumerate(word):
            if m is None or ord(k) < m:
                m = ord(k)
                i = j
        assert i is not None
        alpha_word.append(word[i])
        word = word[:i] + word[i + 1:]
    return "".join(alpha_word)


if __name__ == "__main__":
    print(alphabetical_order("qwertyuiop"))
    print(alphabetical_order("asdfghjkl"))
    print(alphabetical_order("zxcvbnm"))
