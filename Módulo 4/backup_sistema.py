# DESAFIO EXTRA - Sistema de backup
import shutil
import os

# Criar pastas
os.makedirs("origem", exist_ok=True)
os.makedirs("backup", exist_ok=True)
with open("origem/teste.txt", "w") as f:
    f.write("Arquivo de backup")

# Copiar arquivo
shutil.copy("origem/teste.txt", "backup/teste.txt")

print("Backup realizado com sucesso!")
print("Arquivo copiado da pasta 'origem' para a pasta 'backup'")