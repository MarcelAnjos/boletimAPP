def calc_media(notas=[]):
    media= sum(notas) / len(notas)
    notas = notas.append(media)
    if media <=0:
        return print("ERRO: Valores incorretos!")
    if media >10:
        media = 10
    return media