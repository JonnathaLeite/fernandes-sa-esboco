"""Serviços do escritório.

Este arquivo alimenta os cards da Home e a página `servicos.html`.
O campo `video` aponta para uma pergunta de `ferramentas/videos/perguntas.py`.
"""

SERVICOS = [
    {
        "slug": "aposentadorias",
        "nome": "Aposentadorias",
        "resumo": (
            "Desde a reforma de 2019, a aposentadoria depende de idade, tempo de contribuição e, "
            "para quem já contribuía antes, de regras de transição que mudam a cada ano. Escolher "
            "a regra certa faz diferença no momento e no valor do benefício."
        ),
        "para_quem": [
            "Aposentadoria por idade e por tempo de contribuição",
            "Aposentadoria rural, inclusive de quem trabalhou em regime de economia familiar",
            "Aposentadoria especial, para atividades com exposição a agentes nocivos",
            "Aposentadoria da pessoa com deficiência",
        ],
        "como_atuamos": (
            "Analisamos o histórico de contribuições, comparamos as regras aplicáveis e reunimos as "
            "provas dos períodos que o INSS ainda não reconhece, como atividade rural ou trabalho em "
            "condições especiais."
        ),
        "video": "tempo-de-contribuicao",
    },
    {
        "slug": "bpc-loas",
        "nome": "BPC/LOAS",
        "resumo": (
            "O Benefício de Prestação Continuada garante um salário mínimo por mês a idosos a partir "
            "de 65 anos e a pessoas com deficiência em situação de baixa renda, mesmo sem "
            "contribuição ao INSS."
        ),
        "para_quem": [
            "Pessoas a partir de 65 anos em família de baixa renda",
            "Pessoas com deficiência de qualquer idade, inclusive crianças",
            "Famílias que tiveram o pedido negado ou o benefício suspenso",
        ],
        "como_atuamos": (
            "Orientamos sobre o CadÚnico, a composição da renda familiar e a avaliação da "
            "deficiência, e acompanhamos o pedido ou o recurso até a decisão."
        ),
        "video": "bpc",
    },
    {
        "slug": "incapacidade",
        "nome": "Benefícios por incapacidade",
        "resumo": (
            "Quando uma doença ou um acidente impede o trabalho, a lei prevê benefícios temporários "
            "ou permanentes. A perícia médica e a documentação são decisivas nesses casos."
        ),
        "para_quem": [
            "Auxílio por incapacidade temporária (antigo auxílio-doença)",
            "Aposentadoria por incapacidade permanente (antiga aposentadoria por invalidez)",
            "Auxílio-acidente, quando há sequela que reduz a capacidade de trabalho",
            "Segurados convocados para revisão do benefício (pente-fino)",
        ],
        "como_atuamos": (
            "Organizamos laudos e exames, preparamos o segurado para a perícia e atuamos no recurso "
            "ou na ação judicial quando o benefício é negado ou cessado."
        ),
        "video": "doencas-incapacidade",
    },
    {
        "slug": "pensao",
        "nome": "Pensão por morte",
        "resumo": (
            "A pensão por morte é devida aos dependentes de quem era segurado do INSS. A duração e o "
            "valor variam conforme a idade do dependente, o tempo de união e as contribuições de "
            "quem faleceu."
        ),
        "para_quem": [
            "Cônjuges e companheiros, inclusive em união estável",
            "Filhos menores de 21 anos ou com deficiência",
            "Pais e irmãos, quando comprovada a dependência econômica",
        ],
        "como_atuamos": (
            "Verificamos a qualidade de segurado de quem faleceu, reunimos as provas de união ou de "
            "dependência e acompanhamos o pedido junto ao INSS."
        ),
        "video": "acumular-beneficios",
    },
    {
        "slug": "revisoes",
        "nome": "Revisões e planejamento",
        "resumo": (
            "Erros no CNIS, períodos não computados e cálculos incorretos podem reduzir o valor do "
            "benefício. O planejamento ajuda a escolher o melhor momento e a regra mais adequada "
            "para pedir."
        ),
        "para_quem": [
            "Quem está perto de se aposentar e quer saber quando e como pedir",
            "Quem já recebe benefício e desconfia do valor",
            "Quem tem vínculos ou contribuições faltando no CNIS",
        ],
        "como_atuamos": (
            "Conferimos o CNIS período a período, calculamos o tempo de contribuição em cada regra e "
            "indicamos as correções necessárias antes do pedido."
        ),
        "video": "conferir-cnis",
    },
    {
        "slug": "recursos",
        "nome": "Recursos e ações judiciais",
        "resumo": (
            "Um pedido negado não encerra o assunto. Há prazo para recorrer na via administrativa e, "
            "em muitos casos, a possibilidade de levar a questão à Justiça Federal."
        ),
        "para_quem": [
            "Quem teve o benefício negado, cessado ou suspenso",
            "Quem aguarda há muito tempo uma resposta do INSS",
            "Quem precisa comprovar períodos ou condições que o INSS não reconheceu",
        ],
        "como_atuamos": (
            "Analisamos o motivo da decisão e atuamos no recurso ao Conselho de Recursos da "
            "Previdência Social ou na ação judicial, observando os prazos de cada etapa."
        ),
        "video": "pedido-negado",
    },
]
