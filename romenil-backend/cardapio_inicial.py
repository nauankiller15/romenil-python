from cardapio.models import Cardapio


print("Iniciando")
DINP = [

    # Café da Manhã - Diabetes - Nenuma Patologia Secundaria #
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '•	Iogurte desnatado (Copo Americano: 1)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '•	Pão integral (Fatia: 2) Ou Raizes ( Banana da terra - 1 pedaço - 50g/ Batata doce - 1 pedaço 60g/ Aipim -1 pedaço - 70g)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 3,
        'prato': '•	Ovo de galinha ( Forma de cozinhar - pode ser mexido ou cozido) (Unidade: 2)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 4,
        'prato': '•	Ovo de galinha ( Forma de cozinhar - pode ser mexido ou cozido) (Unidade: 2)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 5,
        'prato': '•	Queijo minas frescal (Fatia (30g): 1)',
    },

    # Refeição 2 - Diabetes - Nenuma Patologia Secundaria #
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '•	 Maçã (Unidade: 1)',
    },
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '•	Chá de canela + gengibre (200ml)',
    },

    # Almoço - Diabetes - Nenuma Patologia Secundaria #
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '•	Salada ou verdura cozida, ou folhas em geral (Á VONTADE )',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '•	Peixe não especificado (inteiro, em posta, em filé, etc.) Assado(a) (File: 1)',
    },

    # Refeição 4 - Diabetes - Nenuma Patologia Secundaria #
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '•	Iogurte desnatado (Copo Americano: 1) ',
    },
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '•	Granola (Colher de sopa (13g): 1) ou Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - Quaker® (Colher de sopa (15g): 1) ou Semente de chia (Colher de sopa: 5) ou Psylium (Grama: 10) ou Semente de chia (Colher de sopa: 5)',
    },

    # Janta - Diabetes - Nenuma Patologia Secundaria #
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '•	Ovo de galinha (3 Unidades)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '•	Tomate (2 Colher de sopa cheia em cubos (15g), Orégano seco (1 Colher de café (037g), Orégano seco (1 Colher de café (037g) , Manjericão fresco (5 folhas (3g)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 3,
        'prato': '•	Queijo minas frescal (Fatia (30g): 1)',
    },
    
    # Refeição 6 - Diabetes - Nenuma Patologia Secundaria #
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '•	Leite de vaca desnatado (Copo Americano: 1)',
    },
]


DIML = [

    # Café da Manhã - Diabetes - Metabolismo Lento
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '•	Café da Manhã - Diabetes - Metabolismo Lento',
    },

    # Refeição 2 - Diabetes - Metabolismo Lento
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '•	Refeição 2 - Diabetes - Metabolismo Lento',
    },

    # Almoço - Diabetes - Metabolismo Lento
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '•	almoço - Diabetes - Metabolismo Lento',
    },

    # Refeição 4 - Diabetes - Metabolismo Lento
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '•	Refeição 2 - Diabetes - Metabolismo Lento',
    },

    # Janta - Diabetes - Metabolismo Lento
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '•	Janta - Diabetes - Metabolismo Lento',
    },

    # Refeição 6 - Diabetes - Metabolismo Lento
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '•	Refeição 6 - Diabetes - Metabolismo Lento',
    },
]

DICO = [

    # Café da Manhã - Diabetes - Constipação
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '•	Café da Manhã - Diabetes - Constipação',
    },

    # Refeição 2 - Diabetes - Constipação
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '•	Refeição 2 - Diabetes - Constipação',
    },

    # Almoço - Diabetes - Constipação
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '•	almoço - Diabetes - Constipação',
    },

    # Refeição 4 - Diabetes - Constipação
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '•	Refeição 2 - Diabetes - Constipação',
    },

    # Janta - Diabetes - Constipação
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '•	Janta - Diabetes - Constipação',
    },

    # Refeição 6 - Diabetes - Constipação
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '•	Refeição 6 - Diabetes - Constipação',
    },
]

DIIN = [

    # Café da Manhã - Diabetes - Insonia
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '•	Café da Manhã - Diabetes - Insonia',
    },

    # Refeição 2 - Diabetes - Insonia
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '•	Refeição 2 - Diabetes - Insonia',
    },

    # Almoço - Diabetes - Insonia
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '•	almoço - Diabetes - Insonia',
    },

    # Refeição 4 - Diabetes - Insonia
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '•	Refeição 2 - Diabetes - Insonia',
    },

    # Janta - Diabetes - Insonia
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '•	Janta - Diabetes - Insonia',
    },

    # Refeição 6 - Diabetes - Insonia
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '•	Refeição 6 - Diabetes - Insonia',
    },
]

DICE = [

    # Café da Manhã - Diabetes - Colesterol Elevado
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '•	Café da Manhã - Diabetes - Colesterol Elevado',
    },

    # Refeição 2 - Diabetes - Colesterol Elevado
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '•	Refeição 2 - Diabetes - Colesterol Elevado',
    },

    # Almoço - Diabetes - Colesterol Elevado
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '•	almoço - Diabetes - Colesterol Elevado',
    },

    # Refeição 4 - Diabetes - Colesterol Elevado
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '•	Refeição 2 - Diabetes - Colesterol Elevado',
    },

    # Janta - Diabetes - Colesterol Elevado
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '•	Janta - Diabetes - Colesterol Elevado',
    },

    # Refeição 6 - Diabetes - Colesterol Elevado
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '•	Refeição 6 - Diabetes - Colesterol Elevado',
    },
]

DIAN = [

    # Café da Manhã - Diabetes - Ansiedade
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '•	Café da Manhã - Diabetes - Ansiedade',
    },

    # Refeição 2 - Diabetes - Ansiedade
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '•	Refeição 2 - Diabetes - Ansiedade',
    },

    # Almoço - Diabetes - Ansiedade
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '•	almoço - Diabetes - Ansiedade',
    },

    # Refeição 4 - Diabetes - Ansiedade
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '•	Refeição 2 - Diabetes - Ansiedade',
    },

    # Janta - Diabetes - Ansiedade
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '•	Janta - Diabetes - Ansiedade',
    },

    # Refeição 6 - Diabetes - Ansiedade
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '•	Refeição 6 - Diabetes - Ansiedade',
    },
]

DIRL = [

    # Café da Manhã - Diabetes - Retenção liquida
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '•	Café da Manhã - Diabetes - Retenção liquida',
    },

    # Refeição 2 - Diabetes - Retenção liquida
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '•	Refeição 2 - Diabetes - Retenção liquida',
    },

    # Almoço - Diabetes - Retenção liquida
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '•	almoço - Diabetes - Retenção liquida',
    },

    # Refeição 4 - Diabetes - Retenção liquida
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '•	Refeição 2 - Diabetes - Retenção liquida',
    },

    # Janta - Diabetes - Retenção liquida
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '•	Janta - Diabetes - Retenção liquida',
    },

    # Refeição 6 - Diabetes - Retenção liquida
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '•	Refeição 6 - Diabetes - Retenção liquida',
    },
]

print('inserindo dados')
alterados = 0
inseridos = 0
cardapios = Cardapio.objects.all()
for cardapio in (DINP, DIML, DICO, DIIN, DICE, DIAN, DIRL):
    for prato in cardapio:
        
        cardapio, criado = Cardapio.objects.update_or_create(
            refeicao=prato['refeicao'], 
            principal=prato['principal'], 
            secundaria=prato['secundaria'], 
            ordem=prato['ordem'],
            defaults={'prato': prato['prato']}
        )

        if criado:
            inseridos += 1
        else:
            alterados += 1

print('finalizado')
print(f'{alterados} pratos alterados e {inseridos} pratos inseridos')