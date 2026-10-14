import sqlite3

def iniciar_banco():
    return sqlite3.connect('monitor.db')

def criar_tabela():
    conn = iniciar_banco()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, ping BOOLEAN, http BOOLEAN, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')
    cursor.execute('CREATE TABLE IF NOT EXISTS dispositivos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, host TEXT, url TEXT)')
    conn.commit()
    conn.close()

def salvar_log(nome, ping, http):
    conn = iniciar_banco()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO logs (nome, ping, http) VALUES (?, ?, ?)', (nome, ping, http))
    conn.commit()
    conn.close()

def listar_dispositivos():
    conn = iniciar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT nome, host, url FROM dispositivos')
    dados = cursor.fetchall()
    conn.close()
    return dados

def adicionar_dispositivo(nome, host, url):
    conn = iniciar_banco()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO dispositivos (nome, host, url) VALUES (?, ?, ?)', (nome, host, url))
    conn.commit()
    conn.close()
