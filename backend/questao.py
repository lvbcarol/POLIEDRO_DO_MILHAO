import sqlite3

# Função para inserir uma nova questão, agora com a resposta correta
def inserir_questao(id_questao, enunciado, alternativaA, alternativaB, alternativaC, alternativaD, resposta_correta, dica, valor, nivel_dificuldade):
    conn = sqlite3.connect('quizDB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO questoes (
            id_questao, enunciado, alternativaA, alternativaB, alternativaC,
            alternativaD, resposta_correta, dica, valor, nivel_dificuldade
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (id_questao, enunciado, alternativaA, alternativaB, alternativaC, alternativaD, resposta_correta, dica, valor, nivel_dificuldade))
    conn.commit()
    conn.close()

# Função para buscar todas as questões, incluindo a resposta correta
def buscar_todas_questoes():
    conn = sqlite3.connect('quizDB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questoes")
    questoes = cursor.fetchall()
    conn.close()
    return questoes

# Função para buscar uma questão específica por ID, incluindo a resposta correta
def buscar_questao_por_id(id_questao):
    conn = sqlite3.connect('quizDB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questoes WHERE ID_questao = ?", (id_questao,))
    questao = cursor.fetchone()
    conn.close()
    return questao

# Função para atualizar uma questão existente
def atualizar_questao(id_questao, novo_enunciado, novaA, novaB, novaC, novaD, nova_resposta, nova_dica, novo_valor, novo_nivel):
    conn = sqlite3.connect('quizDB.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE questoes
        SET enunciado = ?, alternativaA = ?, alternativaB = ?, alternativaC = ?, alternativaD = ?,
            resposta_correta = ?, dica = ?, valor = ?, nivel_dificuldade = ?
        WHERE ID_questao = ?
    """, (novo_enunciado, novaA, novaB, novaC, novaD, nova_resposta, nova_dica, novo_valor, novo_nivel, id_questao))
    conn.commit()
    conn.close()
