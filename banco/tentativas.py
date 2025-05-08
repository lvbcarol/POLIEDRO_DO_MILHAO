import sqlite3

def registrar_tentativa(id_usuario, valor_total):
    conn = sqlite3.connect('quizDB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tentativas (ID_usuario, valor_total)
        VALUES (?, ?)
    """, (id_usuario, valor_total))
    conn.commit()
    conn.close()

def buscar_tentativas_usuario(id_usuario):
    conn = sqlite3.connect('quizDB.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM tentativas WHERE ID_usuario = ?
    """, (id_usuario,))
    tentativas = cursor.fetchall()
    conn.close()
    return tentativas
