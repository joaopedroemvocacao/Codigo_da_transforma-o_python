import sqlite3
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')
conn.commit()

def inserir_cliente(nome, email):
    try:
        cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        print(f"Cliente {nome} inserido com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Este email já existe!")

def consultar_clientes():
    cursor.execute("SELECT * FROM Clientes")
    return cursor.fetchall()

def atualizar_cliente(id, novo_nome, novo_email):
    cursor.execute("UPDATE Clientes SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, id))
    conn.commit()
    print(f"Cliente {id} atualizado!")

def deletar_cliente(id):
    cursor.execute("DELETE FROM Clientes WHERE id = ?", (id,))
    conn.commit()
    print(f"Cliente {id} deletado!")

def filtrar_por_nome(letra):
    cursor.execute("SELECT * FROM Clientes WHERE nome LIKE ?", (f"{letra}%",))
    return cursor.fetchall()


inserir_cliente("Ana Silva", "ana@email.com")
inserir_cliente("Bruno Souza", "bruno@email.com")
inserir_cliente("André Lima", "andre@email.com")

print("\n--- Todos os clientes ---")
for cliente in consultar_clientes():
    print(cliente)

print("\n--- Clientes com nome começando com A ---")
for cliente in filtrar_por_nome("A"):
    print(cliente)

atualizar_cliente(2, "Bruno Oliveira", "bruno.oliveira@email.com")
deletar_cliente(3)

print("\n--- Após atualizações ---")
for cliente in consultar_clientes():
    print(cliente)

conn.close()