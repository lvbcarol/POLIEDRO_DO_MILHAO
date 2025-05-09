# editar_questao_admin.py
from questao import buscar_questao_por_id, atualizar_questao

def editar_questao():
    try:
        id_questao = int(input("Digite o ID da questão que deseja editar: "))
        questao = buscar_questao_por_id(id_questao)
        if not questao:
            print("❌ Questão não encontrada.")
            return

        print("\n📌 Questão atual:")
        print(f"Enunciado: {questao[1]}")
        print(f"A: {questao[2]}")
        print(f"B: {questao[3]}")
        print(f"C: {questao[4]}")
        print(f"D: {questao[5]}")
        print(f"Resposta correta: {questao[6]}")
        print(f"Dica: {questao[7]}")
        print(f"Valor: {questao[8]}")
        print(f"Nível: {questao[9]}")

        print("\n✏️ Digite os novos dados (pressione Enter para manter o valor atual):")

        novo_enunciado = input("Novo enunciado: ") or questao[1]
        novaA = input("Nova alternativa A: ") or questao[2]
        novaB = input("Nova alternativa B: ") or questao[3]
        novaC = input("Nova alternativa C: ") or questao[4]
        novaD = input("Nova alternativa D: ") or questao[5]
        nova_resposta = input("Nova resposta correta (A/B/C/D): ") or questao[6]
        nova_dica = input("Nova dica: ") or questao[7]
        novo_valor = input("Novo valor (pontos): ") or questao[8]
        novo_nivel = input("Novo nível de dificuldade: ") or questao[9]

        atualizar_questao(id_questao, novo_enunciado, novaA, novaB, novaC, novaD, nova_resposta, nova_dica, int(novo_valor), novo_nivel)
        print("✅ Questão atualizada com sucesso!")

    except ValueError:
        print("⚠️ Entrada inválida. Use números para o ID e o valor.")

if __name__ == "__main__":
    editar_questao()
