def validar_notas(notas):
    if not isinstance(notas, list):
        raise TypeError("As notas devem estar em uma lista")

    if len(notas) == 0:
        raise ValueError("A lista de notas está vazia")

    for nota in notas:
        if not isinstance(nota, (int, float)):
            raise ValueError(f"Valor inválido encontrado: {nota}")

        if nota < 0 or nota > 10:
            raise ValueError(f"Nota fora do intervalo permitido: {nota}")

    return True

