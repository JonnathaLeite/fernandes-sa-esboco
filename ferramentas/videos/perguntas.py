"""Perguntas frequentes respondidas em vídeo.

Cada pergunta tem: tema, título, resposta escrita (para a página),
três telas do vídeo (título curto, texto) e um link oficial opcional.
Depois de editar, rode `python ferramentas/videos/gerar_videos.py` para refazer os vídeos
e atualize o texto correspondente na seção #duvidas do index.html.
"""

TEMAS = {
    "aposentadoria": ("Aposentadoria", "arquitetura.webp"),
    "beneficios": ("Benefícios", "documentos.webp"),
    "inss": ("Meu INSS", "servicos.webp"),
}

PERGUNTAS = [
    {
        "slug": "tempo-de-contribuicao",
        "tema": "aposentadoria",
        "pergunta": "Quanto tempo preciso contribuir para me aposentar?",
        "resposta": [
            "Depende da modalidade e de quando você começou a contribuir. Na regra geral criada pela reforma de 2019, a idade mínima é de 62 anos para mulheres e 65 para homens.",
            "O tempo mínimo de contribuição é de 15 anos para mulheres e de 20 anos para homens, ou 15 anos para os homens que já contribuíam antes da reforma. Trabalhadores rurais, professores e quem já era segurado antes de 13/11/2019 podem ter regras próprias ou de transição.",
        ],
        "telas": [
            ("A regra geral", "Desde a reforma de 2019, a regra geral pede 62 anos de idade para mulheres e 65 para homens."),
            ("Tempo mínimo", "Mulheres precisam de 15 anos de contribuição. Homens, de 20 anos, ou 15 se já contribuíam antes da reforma."),
            ("Regras próprias", "Trabalhadores rurais, professores e quem já contribuía antes de 2019 podem ter regras próprias ou de transição."),
        ],
        "link": ("Simular aposentadoria no Meu INSS", "https://www.gov.br/pt-br/servicos/simular-aposentadoria"),
    },
    {
        "slug": "antes-de-pedir",
        "tema": "aposentadoria",
        "pergunta": "O que preciso conferir antes de pedir a aposentadoria?",
        "resposta": [
            "Identifique a modalidade e confira se você cumpre os requisitos de idade, carência ou tempo de contribuição.",
            "Revise vínculos, salários e contribuições no CNIS e reúna os comprovantes dos períodos que precisam ser demonstrados, inclusive os de atividade rural, quando for o caso.",
        ],
        "telas": [
            ("Revise o CNIS", "Confira se o extrato tem todos os vínculos, salários e contribuições que você espera encontrar."),
            ("Simule no Meu INSS", "A opção Simular Aposentadoria mostra uma estimativa com base nos dados que o INSS já tem."),
            ("Separe os documentos", "Reúna carteira de trabalho, carnês e comprovantes dos períodos que faltam ou estão errados no sistema."),
        ],
        "link": ("Leia: o que mudou nas regras de transição em 2026", "blog/regras-de-transicao-2026.html"),
    },
    {
        "slug": "contribuir-mais",
        "tema": "aposentadoria",
        "pergunta": "Se eu contribuir com um valor maior, vou receber mais?",
        "resposta": [
            "Pode receber, mas depende do conjunto das contribuições. Na regra geral, o valor parte da média de todos os salários de contribuição desde julho de 1994.",
            "O benefício corresponde a 60% dessa média, mais 2% para cada ano que passar de 20 anos de contribuição (15 anos para mulheres), e fica sempre entre o salário mínimo e o teto do INSS. Antes de aumentar a contribuição, vale simular o impacto real.",
        ],
        "telas": [
            ("Como é o cálculo", "O valor parte da média de todos os salários de contribuição desde julho de 1994."),
            ("O percentual", "Na regra geral, são 60% da média, mais 2% por ano que passar de 20 anos de contribuição (15 para mulheres)."),
            ("Os limites", "O valor fica entre o salário mínimo e o teto do INSS. Simule antes de aumentar a contribuição."),
        ],
        "link": ("Regras de cálculo na Emenda Constitucional 103", "https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc103.htm"),
    },
    {
        "slug": "carencia",
        "tema": "aposentadoria",
        "pergunta": "Qual é a diferença entre carência e tempo de contribuição?",
        "resposta": [
            "Carência é o número mínimo de contribuições mensais que alguns benefícios exigem. Na aposentadoria por idade, por exemplo, são 180 contribuições.",
            "Tempo de contribuição é a soma dos períodos reconhecidos pelo INSS. Um mesmo período pode contar como tempo de contribuição e ter tratamento diferente para a carência, por isso vale analisar o histórico com cuidado.",
        ],
        "telas": [
            ("Carência", "É o número mínimo de contribuições mensais que alguns benefícios exigem. Na aposentadoria por idade, são 180."),
            ("Tempo de contribuição", "É a soma de todos os períodos que o INSS reconhece para fins de aposentadoria."),
            ("Nem sempre são iguais", "Alguns períodos contam como tempo, mas não como carência. Por isso é importante analisar o histórico."),
        ],
        "link": None,
    },
    {
        "slug": "doencas-incapacidade",
        "tema": "beneficios",
        "pergunta": "Quais doenças dão direito a benefício por incapacidade?",
        "resposta": [
            "Não existe uma lista fechada. O que garante o benefício é a incapacidade para o trabalho ou para a atividade habitual, comprovada na perícia do INSS.",
            "Também é preciso ter qualidade de segurado e, em regra, 12 contribuições de carência. Acidentes de qualquer natureza e algumas doenças graves previstas em lei dispensam a carência.",
        ],
        "telas": [
            ("Não é a doença em si", "O que garante o benefício é a incapacidade para o trabalho, comprovada na perícia do INSS."),
            ("Outros requisitos", "Também é preciso ter qualidade de segurado e, em regra, 12 contribuições de carência."),
            ("Quando não há carência", "Acidentes de qualquer natureza e algumas doenças graves previstas em lei dispensam a carência."),
        ],
        "link": ("Requisitos do benefício por incapacidade no INSS", "https://www.gov.br/inss/pt-br/direitos-e-deveres/beneficios-por-incapacidade/auxilio-por-incapacidade-temporaria"),
    },
    {
        "slug": "acumular-beneficios",
        "tema": "beneficios",
        "pergunta": "Posso receber mais de um benefício ao mesmo tempo?",
        "resposta": [
            "Depende da combinação. Aposentadoria e pensão por morte podem ser recebidas juntas: o benefício mais vantajoso é pago por inteiro e o outro, com redução por faixas.",
            "Algumas combinações são proibidas. O auxílio-acidente não se acumula com aposentadoria, e o BPC, em regra, não se acumula com outro benefício da seguridade social.",
        ],
        "telas": [
            ("Depende da combinação", "Alguns benefícios podem ser recebidos juntos. Outros são proibidos por lei."),
            ("Aposentadoria e pensão", "Podem ser recebidas juntas: a mais vantajosa é paga por inteiro e a outra, com redução por faixas."),
            ("Combinações proibidas", "Auxílio-acidente não se acumula com aposentadoria. O BPC, em regra, não se acumula com outro benefício."),
        ],
        "link": ("Regras de acumulação no INSS", "https://www.gov.br/inss/pt-br/noticias/conheca-os-beneficios-que-podem-ser-acumulados"),
    },
    {
        "slug": "bpc",
        "tema": "beneficios",
        "pergunta": "O BPC é uma aposentadoria?",
        "resposta": [
            "Não. O Benefício de Prestação Continuada (BPC/LOAS) é assistencial e não exige contribuições ao INSS. Ele é destinado a pessoas a partir de 65 anos e a pessoas com deficiência, em família de baixa renda.",
            "Em regra, a renda familiar por pessoa deve ser de até 1/4 do salário mínimo, e a inscrição no CadÚnico precisa estar atualizada. O BPC não paga 13º salário e não gera pensão por morte.",
        ],
        "telas": [
            ("Não é aposentadoria", "O BPC/LOAS é um benefício assistencial e não exige contribuições ao INSS."),
            ("Quem pode receber", "Pessoas a partir de 65 anos e pessoas com deficiência de qualquer idade, em família de baixa renda."),
            ("Diferenças importantes", "O BPC não paga 13º e não gera pensão por morte. O CadÚnico precisa estar atualizado."),
        ],
        "link": ("Critérios do BPC no gov.br", "https://www.gov.br/mds/pt-br/acoes-e-programas/suas/beneficios-assistenciais/beneficio-assistencial-ao-idoso-e-a-pessoa-com-deficiencia-bpc"),
    },
    {
        "slug": "conferir-cnis",
        "tema": "inss",
        "pergunta": "Como conferir se o meu CNIS está correto?",
        "resposta": [
            "O CNIS reúne os vínculos, salários e contribuições registrados no INSS. Baixe o extrato no Meu INSS e compare cada período com a carteira de trabalho, os contracheques e os comprovantes de pagamento.",
            "Se faltar um vínculo ou um valor estiver diferente, anote o período e reúna os documentos que comprovam a informação.",
        ],
        "telas": [
            ("Baixe o extrato", "No Meu INSS, busque Extrato de Contribuição (CNIS) e salve uma cópia."),
            ("Confira cada período", "Compare vínculos e datas com a carteira de trabalho. Confira também salários e recolhimentos."),
            ("Separe os comprovantes", "Se faltar vínculo ou pagamento, anote o período e reúna os documentos que comprovam a informação."),
        ],
        "link": ("Conheça o serviço de revisão e planejamento", "servicos.html#revisoes"),
    },
    {
        "slug": "acompanhar-pedido",
        "tema": "inss",
        "pergunta": "Como acompanhar meu pedido no INSS?",
        "resposta": [
            "Entre no site ou no aplicativo Meu INSS com sua conta gov.br e abra a opção Consultar Pedidos.",
            "Ali você vê o andamento, as exigências e o prazo para respondê-las. Quando sair a decisão, leia a comunicação para entender o resultado e o motivo.",
        ],
        "telas": [
            ("Abra Consultar Pedidos", "Entre no Meu INSS com sua conta gov.br e abra os detalhes do seu requerimento."),
            ("Leia as exigências", "Se o INSS pedir algum documento, confira exatamente o que foi solicitado e o prazo para responder."),
            ("Consulte a decisão", "Quando sair a decisão, abra a comunicação para ler o resultado e o motivo."),
        ],
        "link": ("Acessar o Meu INSS", "https://meu.inss.gov.br/"),
    },
    {
        "slug": "pedido-negado",
        "tema": "inss",
        "pergunta": "O que fazer se o INSS negar meu pedido?",
        "resposta": [
            "Leia a carta de decisão no Meu INSS para entender exatamente o motivo da negativa.",
            "Se discordar, é possível recorrer ao Conselho de Recursos da Previdência Social no prazo de 30 dias contados da ciência da decisão. Dependendo do caso, também é possível fazer um novo pedido com mais documentos ou buscar a Justiça Federal.",
        ],
        "telas": [
            ("Leia o motivo", "Abra a carta de decisão no Meu INSS e veja exatamente por que o pedido foi negado."),
            ("Atenção ao prazo", "O recurso ao Conselho de Recursos da Previdência Social deve ser feito em até 30 dias da ciência da decisão."),
            ("Outros caminhos", "Conforme o caso, cabe um novo pedido com mais documentos ou uma ação na Justiça Federal."),
        ],
        "link": ("Serviço oficial de recurso ao INSS", "https://www.gov.br/pt-br/servicos/apresentar-recurso-ordinario-inicial"),
    },
]
