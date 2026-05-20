import sqlite3
from datetime import datetime

conn = sqlite3.connect('tarefas.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descricao TEXT,
        status TEXT DEFAULT 'pendente',
        data_criacao TEXT
    )
''')
conn.commit()

def adicionar_tarefa(titulo, descricao=""):
    data = datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute("INSERT INTO Tarefas (titulo, descricao, data_criacao) VALUES (?, ?, ?)",
                   (titulo, descricao, data))
    conn.commit()
    print(f"Tarefa '{titulo}' adicionada!")

def ver_tarefas(filtro="todas"):
    if filtro == "pendente":
        cursor.execute("SELECT * FROM Tarefas WHERE status = 'pendente'")
    else:
        cursor.execute("SELECT * FROM Tarefas")
    
    tarefas = cursor.fetchall()
    if not tarefas:
        print("Nenhuma tarefa encontrada!")
    else:
        for t in tarefas:
            print(f"[{t[0]}] {t[1]} - {t[3]} - {t[4]}")

def excluir_tarefa(id):
    cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id,))
    conn.commit()
    print(f"Tarefa {id} excluída!")

def concluir_tarefa(id):
    cursor.execute("UPDATE Tarefas SET status = 'concluída' WHERE id = ?", (id,))
    conn.commit()
    print(f"Tarefa {id} concluída!")

while True:
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Ver todas as tarefas")
    print("3 - Ver tarefas pendentes")
    print("4 - Concluir tarefa")
    print("5 - Excluir tarefa")
    print("6 - Sair")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        titulo = input("Título: ")
        desc = input("Descrição (opcional): ")
        adicionar_tarefa(titulo, desc)
    elif opcao == "2":
        ver_tarefas()
    elif opcao == "3":
        ver_tarefas("pendente")
    elif opcao == "4":
        id = input("ID da tarefa para concluir: ")
        concluir_tarefa(int(id))
    elif opcao == "5":
        id = input("ID da tarefa para excluir: ")
        excluir_tarefa(int(id))
    elif opcao == "6":
        print("Até logo!")
        break

conn.close()