import csv

with open("notas.csv", "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["Aluno", "Nota1", "Nota2", "Nota3"])
    writer.writerow(["João", 8.0, 7.5, 9.0])
    writer.writerow(["Maria", 6.0, 5.5, 7.0])

print("Notas salvas!")

print("\n--- Notas dos Alunos ---")
with open("notas.csv", "r", encoding="utf-8") as arquivo:
    reader = csv.reader(arquivo)
    for linha in reader:
        print(linha)