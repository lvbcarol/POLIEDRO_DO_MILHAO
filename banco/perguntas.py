
questions = [
    "1. Em uma campanha de vacinação, a prefeitura explicou que a vacina contra a gripe não causa a gripe, mas sim estimula o organismo a produzir defesas. Com base nessa informação, é correto afirmar que:",
    "2. Um aluno comprou um livro por R$ 40,00 e recebeu 10% de desconto. Qual foi o valor pago?",
    "3. Durante a Revolução Industrial, uma grande mudança na organização do trabalho foi:",
    "4. A cidade de São Paulo sofre com enchentes. Um dos fatores principais é:",
    "5. O sódio (Na) tende a formar íons positivos, como o Na⁺. Isso se relaciona à propriedade periódica chamada:",
    "6. O poema de Gregório de Matos reflete o Barroco ao expressar:",
    "7. Um carro anda a 72 km/h. Qual sua velocidade em m/s?",
    "8. Segundo Durkheim, a anomia surge quando:",
    "9. *'Despite the challenges of remote learning, many students reported an improvement in their time management and self-discipline skills.'* O trecho indica que os estudantes:",
    "10. A pintura 'Guernica', de Picasso, representa:",
    "11. Com R₀ = 2,5, quantas pessoas serão infectadas após 4 ciclos, começando com 1 pessoa, se todas contaminam outras?"
]

answers = [
    ["A) A vacina contém anticorpos que combatem diretamente o vírus.",
     "B) A vacina impede que o vírus entre no corpo.",
     "C) A vacina contém vírus atenuados ou fragmentados, que ativam o sistema imunológico.",
     "D) A vacina altera o DNA para impedir a infecção."],
     
    ["A) R$ 36,00",
     "B) R$ 38,00",
     "C) R$ 34,00",
     "D) R$ 30,00"],
     
    ["A) aumento da produção artesanal.",
     "B) surgimento do trabalho assalariado nas fábricas.",
     "C) diminuição da exploração dos trabalhadores.",
     "D) abolição da escravidão mundial."],
     
    ["A) excesso de vegetação nativa.",
     "B) urbanização sem planejamento e impermeabilização do solo.",
     "C) presença de rios navegáveis.",
     "D) áreas agrícolas na periferia."],
     
    ["A) Afinidade eletrônica",
     "B) Energia de ionização",
     "C) Eletronegatividade",
     "D) Raio atômico"],
     
    ["A) amor platônico e idealização da natureza.",
     "B) conflito espiritual e dualismo entre corpo e alma.",
     "C) racionalismo e objetividade.",
     "D) crítica à monarquia absolutista."],
     
    ["A) 25 m/s",
     "B) 18 m/s",
     "C) 20 m/s",
     "D) 15 m/s"],
     
    ["A) as normas sociais se enfraquecem durante crises.",
     "B) o Estado proíbe manifestações culturais.",
     "C) há excesso de controle institucional.",
     "D) há aumento da solidariedade mecânica."],
     
    ["A) aprenderam a lidar melhor com o tempo.",
     "B) não gostaram do ensino remoto.",
     "C) não conseguiram se organizar.",
     "D) desejam o retorno imediato às aulas presenciais."],
     
    ["A) a violência e o sofrimento causados pela guerra.",
     "B) o ideal clássico da beleza europeia.",
     "C) a crítica ao capitalismo moderno.",
     "D) a valorização da arte religiosa."],
     
    ["A) 625",
     "B) 244,14",
     "C) 976,56",
     "D) 312,5"]
]

correct_answers = [
    "C", "A", "B", "B", "B", "B", "C", "A", "A", "A", "C"
]

tips = [
    "Dica: Vacinas ensinam o corpo a se defender, sem causar a doença.",
    "Dica: 10% de 40 = 4. Subtraia do total.",
    "Dica: O trabalho mudou com as máquinas e as fábricas.",
    "Dica: O asfalto e o cimento impedem a água de infiltrar no solo.",
    "Dica: Essa energia é necessária para remover um elétron do átomo.",
    "Dica: O Barroco expressa tensões internas e religiosas.",
    "Dica: Divida a velocidade por 3,6 para converter km/h em m/s.",
    "Dica: Pense em momentos de caos social ou falta de referência.",
    "Dica: 'Despite' = 'apesar de'.",
    "Dica: A obra retrata o bombardeio de uma cidade espanhola.",
    "Dica: Use progressão geométrica: 1 × (2,5)^4."
]

def check_answer(question_index, user_answer):
    return user_answer.upper() == correct_answers[question_index]

def display_question_and_answers(question_index):
    print(questions[question_index])
    for answer in answers[question_index]:
        print(answer)
    print("Dica:", tips[question_index])
