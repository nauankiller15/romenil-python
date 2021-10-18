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
        'prato': '',
    },

    # Refeição 2 - Diabetes - Metabolismo Lento
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '',
    },

    # Almoço - Diabetes - Metabolismo Lento
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '',
    },

    # Refeição 4 - Diabetes - Metabolismo Lento
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '',
    },

    # Janta - Diabetes - Metabolismo Lento
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '',
    },

    # Refeição 6 - Diabetes - Metabolismo Lento
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': 'teste2',
    },
]

print('inserindo dados')
alterados = 0
inseridos = 0
cardapios = Cardapio.objects.all()
for cardapio in (DINP, DIML):
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