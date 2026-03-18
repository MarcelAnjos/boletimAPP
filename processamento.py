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

def calc_media(notas):
    validar_notas(notas)

    media = sum(notas) / len(notas)

    notas.append(media) 

    return media

def status(lista_alunos):
    recuperacao = []
    aprovados = []
    top_students = []
    maior_media = -1

    for nome, notas in lista_alunos:
        validar_notas(notas)
        
        media = calc_media(notas)

        if media < 7.0:
            recuperacao.append(nome)

        else:
            aprovados.append(nome)
        
        if media > maior_media:
            maior_media = media
            top_students = [nome]
        elif media == maior_media:
            top_students.append(nome)

    return recuperacao, aprovados, top_students, maior_media