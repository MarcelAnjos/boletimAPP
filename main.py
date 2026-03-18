from processamento import validar_notas, calc_media, status

# 📊 Dados de entrada
alunos = [
    ("João", [7, 8, 6]),
    ("Maria", [9, 9, 10]),
    ("Pedro", [5, 6, 6]),
    ("Ana", [9, 7, 10])
]

recuperacao, aprovados, top_students, maior_media = status(alunos)

print("===== RESULTADO =====")
print("Alunos em recuperação:", recuperacao)
print("Alunos Aprovados:", aprovados)
print("Top Students:", top_students)
print("Maior média:", round(maior_media, 2))