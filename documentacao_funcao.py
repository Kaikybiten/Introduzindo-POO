def soma(x: int | float, y: int | float, z: int | float | None = None):
    if z is None:
        return x + y
    return x + y + z

"""
    Na função está documentado que:

    x deve ser do tipo inteiro ou flutuante

    y deve ser do tipo inteiro ou flutuante

    e z deve ser do tipo inteiro ou flutuante ou None
"""