from cardapio.models import Cardapio

# RODAR SCRIPTS
# python manage.py shell
# import cardapio_inicial

'''
LEGENDA PATOLOGIAS:
# Patologias principais
DI: Diabetes
HI: Hipertensao
NP: Nenhuma Patologia principal

# Patologias secundárias
ML: Metabolismo Lento
CO: Constipação
IN: Insonia
CE: Colesterol Elevado
AN: Ansiedade
RL: Retensão Liquida
CL: Celíaco
NP: Nenhuma Patologia secundária

# Codigo Completo
DIML: Diabetes e Metabolismo Lento
DICO: Diabetes e Constipação
DIIN: Diabetes e Insonia
DICE: Diabetes e Colesterol Elevado
DIAN: Diabetes e Ansiedade
DIRL: Diabetes e Retensão Liquida
DINP: Diabetes e Nenhuma Patologia secundária

HIML: Hipertensão e Metabolismo Lento
HICO: Hipertensão e Constipação
HIIN: Hipertensão e Insonia
HICE: Hipertensão e Colesterol Elevado
HIAN: Hipertensão e Ansiedade
HIRL: Hipertensão e Retensão Liquida
HINP: Hipertensão e Nenhuma Patologia secundária

NPML: Nenhuma Patologia Principal e Metabolismo Lento
NPCO: Nenhuma Patologia Principal e Constipação
NPIN: Nenhuma Patologia Principal e Insonia
NPCE: Nenhuma Patologia Principal e Colesterol Elevado
NPAN: Nenhuma Patologia Principal e Ansiedade
NPRL: Nenhuma Patologia Principal e Retensão Liquida
NPCL: Nenhuma Patologia Principal e Celíaco
NPNP: Nenhuma Patologia Principal e Nenhuma Patologia secundária

'''

print("Iniciando")

# TODOS OS CARDÁPIOS DE DIABETES

DINP = [

    # Café da Manhã - Diabetes - Nenhuma Patologia Secundaria #
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '• Iogurte desnatado (Copo Americano: 1)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '• Pão integral (Fatia: 2) Ou Raizes ( Banana da terra - 1 pedaço - 50g/ Batata doce - 1 pedaço 60g/ Aipim -1 pedaço - 70g)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 3,
        'prato': '• Ovo de galinha ( Forma de cozinhar - pode ser mexido ou cozido) (Unidade: 2)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 4,
        'prato': '• Queijo minas frescal (Fatia (30g): 1)',
    },

    # Refeição 2 - Diabetes - Nenhuma Patologia Secundaria #
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '•  Maçã (Unidade: 1)',
    },
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '• Chá de canela + gengibre (200ml)',
    },

    # Almoço - Diabetes - Nenhuma Patologia Secundaria #
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '• Salada ou verdura cozida, ou folhas em geral (Á VONTADE )',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '• Peixe não especificado (inteiro, em posta, em filé, etc.) Assado(a) (File: 1)',
    },

    # Refeição 4 - Diabetes - Nenhuma Patologia Secundaria #
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '• Iogurte desnatado (Copo Americano: 1) ',
    },
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '• Granola (Colher de sopa (13g): 1) ou Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - Quaker® (Colher de sopa (15g): 1) ou Semente de chia (Colher de sopa: 5) ou Psylium (Grama: 10) ou Semente de chia (Colher de sopa: 5)',
    },

    # Janta - Diabetes - Nenhuma Patologia Secundaria #
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '• Ovo de galinha (3 Unidades)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '• Tomate (2 Colher de sopa cheia em cubos (15g), Orégano seco (1 Colher de café (037g), Orégano seco (1 Colher de café (037g) , Manjericão fresco (5 folhas (3g)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 3,
        'prato': '• Queijo minas frescal (Fatia (30g): 1)',
    },
    
    # Refeição 6 - Diabetes - Nenhuma Patologia Secundaria #
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '• Leite de vaca desnatado (Copo Americano: 1)',
    },
]


DIML = [

    # Desjejum - Diabetes - Metabolismo Lento
    {
        'refeicao': 0,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Curcuma ( 2 colheres de chá cheios) ',
    },
    {
        'refeicao': 0,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	GENGIBRE EM PÓ ( 2 COLHERES DE CHÁ)',
    },
    {
        'refeicao': 0,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '⦁	Pimenta Caiena (meia colher de chá)',
    },
    {
        'refeicao': 0,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 4,
        'prato': '⦁	Água morna (200ml)',
    },

    # Café da Manhã - Diabetes - Metabolismo Lento
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': 'Maçã (Unidade: 1) Ou Pera ( 1 und ) Ou Banana ( 1 und)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Chá de canela + gengibre ( 200ml)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '⦁	Batata doce (70g) Ou aipim (60 g) Ou Inhame (70g)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 4,
        'prato': '⦁	Ovos de galinha ( mexidos ou cozidos ) -3 unds',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 5,
        'prato': '⦁	Queijo (minas ou cotagge) – 1 fatia',
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
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Á VONTADE )',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Peito de frango (100g) Ou Peixe (Tilápia ou merluza) - 130g',
    },

    # Refeição 4 - Diabetes - Metabolismo Lento
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Iogurte desnatado ( baixa gordura)  (Copo Americano: 1)',
    },
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Granola (Colher de sopa (13g): 1) ou Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - Quaker® (Colher de sopa (15g): 1) ou Semente de chia (Colher de sopa: 5) ou Psylium (Grama: 10) ou Semente de chia (Colher de sopa: 5)',
    },

    # Janta - Diabetes - Metabolismo Lento
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Ovo de galinha (3 Unidades)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Tomate (2 Colher de sopa cheia em cubos (15g), Orégano seco (1 Colher de café (037g), Orégano seco (1 Colher de café (037g) , Manjericão fresco (5 folhas (3g)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '⦁	Queijo minas frescal (Fatia (30g): 1)',
    },

    # Refeição 6 - Diabetes - Metabolismo Lento
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Leite de vaca desnatado (Copo Americano: 1)',
    },
]

DICO = [

    # Café da Manhã - Diabetes - Constipação
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Mamão ( 300g) Ou Abcaxi ( 2 fatias )Ou Melão ( 200g)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁	Ovo de galinha ( Forma de cozinhar - pode ser mexido ou cozido) (Unidade: 2)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 3,
        'prato': '⦁	Queijo minas frescal (Fatia (30g): 1)',
    },
    
    # Refeição 2 - Diabetes - Constipação
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Yogurt integral ( 100 ml)',
    },
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁	Castanha de caju ( 15 unidades)',
    },

    # Almoço - Diabetes - Constipação
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Á VONTADE)',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Á VONTADE)',
    },

    # Refeição 4 - Diabetes - Constipação
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Iogurte desnatado (Copo Americano: 1)',
    },
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁	Granola (Colher de sopa (13g): 1) ou Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - Quaker® (Colher de sopa (15g): 1) ou Semente de chia (Colher de sopa: 5) ou Psylium (Grama: 10) ou Semente de chia (Colher de sopa: 5)',
    },

    # Janta - Diabetes - Constipação
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Ovo de galinha ( MEXIDO OU COZIDO)  (3 Unidade)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁	Tomate (2 Colher de sopa cheia em cubos (15g), Orégano seco (1 Colher de café (037g), Orégano seco (1 Colher de café (037g) , Manjericão fresco (5 folhas (3g)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Queijo minas frescal (Fatia (30g): 1)',
    },

    # Refeição 6 - Diabetes - Constipação
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Chá de sene + Camomila (Infusão) – 5gr de cada folha – para 300 ml de água',
    },
]

DIIN = [

    # Desjejum - Diabetes - Insonia
    {
        'refeicao': 0,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Chá de canela (200ml)',
    },

    # Café da Manhã - Diabetes - Insonia
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': 'Pão integral (Fatia: 1) ou Aipim Cozido(a) (Grama: 50) ou Cuscuz, de milho, cozido com sal (Grama: 55) ou Batata, doce, cozida (Grama: 80) ou Tapioca de goma (Grama: 20) ou Inhame (cozido) (Grama: 55)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': 'Ovo de galinha Cozido(a) (Unidade: 2) ou Queijo minas frescal (Grama: 60) ou Peito de galinha ou frango Assado(a) (Grama: 80) ou Carne moída Cozido(a) (Grama: 65) ou Atum em conserva (Grama: 70)',
    },

    # Refeição 2 - Diabetes - Insonia
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Castanha de caju (Unidade: 4) ou Castanha do Pará sem sal (Unidade (4g): 2)',
    },

    # Almoço - Diabetes - Insonia
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': 'Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 3,
        'prato': 'Feijão, carioca, cozido (Colher De Sopa Cheia: 3) ou Lentilha cozida (grãos) (Colher de sopa (24g): 1) ou Grão de bico (cozido) (Colher de sopa (24g): 1)',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 4,
        'prato': 'Arroz integral (cozido) (Colher de arroz cheia (63g): 2) ou Macarrão Cozido(a) (Grama: 60) ou Macarrão, de arroz, cozido (Grama: 90)',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 5,
        'prato': '⦁	Quinoa (colher de sopa 2)',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 6,
        'prato': '⦁	Brócolis (Grama: 50)',
    },

    # Refeição 4 - Diabetes - Insonia
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - (Colher de sopa (15g): 1)',
    },
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': 'Maçã (Unidade: 1)',
    },

    # Janta - Diabetes - Insonia
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': 'Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 3,
        'prato': 'Batata doce cozida sem sal (Grama: 70) ou Cuscuz, de milho, cozido com sal (Grama: 50) ou Inhame (cozido) (Grama: 60) ou Banana da terra (Grama: 40) ou Pão integral (Fatia: 1)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 4,
        'prato': '⦁	Brócolis (Grama: 50)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 5,
        'prato': '⦁	chocolate amargo (Tablete: 1)',
    },

    # Refeição 6 - Diabetes - Insonia
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	CHÁ DE CAMOMILA + MULUNGU + PASSIFLORA 3-5 COLHERES DE CADA EM 500ML DE ÁGUA 30/40MIN ANTES DE DORMIR',
    },
]

DICE = [

    # Desjejum - Diabetes - Colesterol Elevado
    {
        'refeicao': 0,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Chá de canela (200ml)',
    },

    # Café da Manhã - Diabetes - Colesterol Elevado
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '• Pão integral (Fatia: 1) ou Aipim Cozido(a) (Grama: 50) ou Cuscuz, de milho, cozido com sal(Grama: 55) ou Batata, doce, cozida (Grama: 80) ou Tapioca de goma (Grama: 20) ou Inhame(cozido) (Grama: 55)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': '• Ovo de galinha Cozido(a) (Unidade: 2) ou Queijo minas frescal (Grama: 60) ou Peito de galinha ou frango Assado(a) (Grama: 80) ou Carne moída Cozido(a) (Grama: 65) ou Atum em conserva (Grama: 70)',
    },

    # Refeição 2 - Diabetes - Colesterol Elevado
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '• Castanha de caju (Unidade: 4) ou Castanha do Pará sem sal (Unidade (4g): 2) ',
    },

    # Almoço - Diabetes - Colesterol Elevado
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': 'Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 3,
        'prato': 'Feijão, carioca, cozido (Colher De Sopa Cheia: 3) ou Lentilha cozida (grãos) (Colher de sopa(24g): 1) ou Grão de bico (cozido) (Colher de sopa (24g): 1)',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 4,
        'prato': 'Arroz integral (cozido) (Colher de arroz cheia (63g): 2) ou Macarrão Cozido(a) (Grama: 60) ou Macarrão, de arroz, cozido (Grama: 90)',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 5,
        'prato': '⦁	Quinoa (colher de sopa 2)',
    },

    # Refeição 4 - Diabetes - Colesterol Elevado
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - (Colher de sopa (15g): 1)',
    },
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': 'Maçã (Unidade: 1)',
    },

    # Janta - Diabetes - Colesterol Elevado
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': '• Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 3,
        'prato': '• Batata doce cozida sem sal (Grama: 70) ou Cuscuz, de milho, cozido com sal (Grama: 50) ou Inhame (cozido) (Grama: 60) ou Banana da terra (Grama: 40) ou Pão integral (Fatia: 1)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 4,
        'prato': '⦁	Brócolis (Grama: 50)',
    },

    # Refeição 6 - Diabetes - Colesterol Elevado
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Banana, prata, crua (Unidade Pequena: 1) ou Maçã (Unidade: 1) ou pera (Unidade: 1) ou Mamão papaia (Grama: 210) ou Morango (Unidade média (12g): 25) ou Amora (Unidade: 50)',
    },
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': 'Chá de carqueja (200ml) ou chá de sálvia (200ml) ou chá de insulina vegetal (200ml)',
    },
]

DIAN = [

    # Café da Manhã - Diabetes - Ansiedade
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Mingau de aveia ( PREPARAR COM 200ML DE LEITE DESNATADO + 30 GRAMAS DE AVEIA EM FLOCOS + 1 COLHER DE SOPA DE CANELA EM PÓ) ',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	OVO DE GALINHA ( 1UND)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 3,
        'prato': '⦁	Chá de Mulungu ( 100ml) com 5gr de folha',
    },

    # Refeição 2 - Diabetes - Ansiedade
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	 Banana ( 1 und)  Ou Uvas ( 15 unds ) Ou Pera ( 1 und)',
    },
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	Mix de oleagenosas ( 1 colher de sopa)',
    },

    # Almoço - Diabetes - Ansiedade
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Á VONTADE )',
    },
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	Peito de frango ( 150g) Ou Carne bovina(2x na semana) ( 130g)',
    },

    # Refeição 4 - Diabetes - Ansiedade
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Iogurte desnatado (Copo Americano: 1)',
    },
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	Iogurte desnatado (Copo Americano: 1)',
    },

    # Janta - Diabetes - Ansiedade
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '• Ovo de galinha(mexido ou cozido) (3 Unidades) Ou Atum (120g)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	Tomate (2 Colher de sopa cheia em cubos (15g), Orégano seco (1 Colher de café (037g), Orégano seco (1 Colher de café (037g) , Manjericão fresco (5 folhas (3g)',
    },
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 3,
        'prato': '⦁	Queijo minas frescal (Fatia (30g): 1)',
    },


    # Refeição 6 - Diabetes - Ansiedade
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	CHÁ DE CAMOMILA + CAPIM SANTO ( 200ML + 3GR DE CADA ERVA)',
    },
]

DIRL = [

    # Café da Manhã - Diabetes - Retenção liquida
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '• Café da Manhã - Diabetes - Retenção liquida',
    },

    # Refeição 2 - Diabetes - Retenção liquida
    {
        'refeicao': 2,
        'principal': 'DI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '• Refeição 2 - Diabetes - Retenção liquida',
    },

    # Almoço - Diabetes - Retenção liquida
    {
        'refeicao': 3,
        'principal': 'DI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '• Almoço - Diabetes - Retenção liquida',
    },

    # Refeição 4 - Diabetes - Retenção liquida
    {
        'refeicao': 4,
        'principal': 'DI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '• Refeição 2 - Diabetes - Retenção liquida',
    },

    # Janta - Diabetes - Retenção liquida
    {
        'refeicao': 5,
        'principal': 'DI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '• Janta - Diabetes - Retenção liquida',
    },

    # Refeição 6 - Diabetes - Retenção liquida
    {
        'refeicao': 6,
        'principal': 'DI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '• Refeição 6 - Diabetes - Retenção liquida',
    },
]

# TODOS CARDAPIOS DE HIPERTENSÃO

HINP = [

    # Café da Manhã - Hipertensão - Nenhuma Patologia Secundaria #
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 150) ou Queijo branco ( 2 fatias ) ou Atum (Grama: 120)',
    },
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': 'Batata doce cozida sem sal (Grama: 55) ou Cuscuz (Grama: 45) ou Inhame (cozido) (Grama: 50) ou Banana da terra Cozido(a) (Grama: 65)',
    },
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 3,
        'prato': 'Mamão (1 fatia)',
    },
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 4,
        'prato': 'Aveia em flocos (Colher De Sopa: 1)',
    },

    # Refeição 2 - Hipertensão - Nenhuma Patologia Secundaria #
    {
        'refeicao': 2,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '⦁	Banana, prata, crua (Unidade Pequena: 1) ou Maçã (Unidade: 1) ou Uva itália (un: 15) ou Amora (Unidade: 50) ou Mamão, Papaia, cru (Grama: 210) ou Goiaba (Grama: 160) ou pera (Unidade: 1)',
    },
    {
        'refeicao': 2,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': 'Canela em pó (Colher de sopa (13g): 1)',
    },

    # Almoço - Hipertensão - Nenhuma Patologia Secundaria #
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': 'Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 3,
        'prato': 'Feijão, carioca, cozido (Colher De Sopa Cheia: 3) ou Lentilha cozida (grãos) (Colher de sopa (24g): 1) ou Grão de bico (cozido) (Colher de sopa (24g): 1)',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 4,
        'prato': 'Arroz integral (cozido) (Colher de arroz cheia (63g): 2) ou Macarrão Cozido(a) (Grama: 60) ou Macarrão, de arroz, cozido (Grama: 90)',
    },

    # Refeição 4 - Hipertensão - Nenhuma Patologia Secundaria #
    {
        'refeicao': 4,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '⦁	chá de cavalinha (200ml: 1)',
    },
   

    # Janta - Hipertensão - Nenhuma Patologia Secundaria #
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': 'Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 3,
        'prato': 'Batata doce cozida sem sal (Grama: 70) ou Cuscuz, de milho, cozido com sal (Grama: 50) ou Inhame (cozido) (Grama: 60) ou Banana da terra (Grama: 40) ou Pão integral (Fatia: 1)',
    },
    
    # Refeição 6 - Hipertensão - Nenhuma Patologia Secundaria #
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '⦁	Água (Copo médio (200ml): 1)',
    },
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': 'Chá, erva, camomila, ebulição (Grama: 2)',
    },
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 3,
        'prato': '⦁	Maracujá (Unidade média (45g): 1)',
    },
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'NP',
        'ordem': 4,
        'prato': '⦁	Mel (Colher de chá (7g): 1) ⦁ Obs: Prepare o chá, despejando água fervida sobre a camomila. Deixe tampado por cerca de dez minutos e coe. Bata no liquidificador com a polpa do maracujá, o mel (ou agave) e gelo à vontade. Sirva em seguida.',
    },
]

HIML = [

    # Desjejum - Hipertensão - Metabolismo Lento
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Limão espremido (Unidade: 1)',
    },
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Gengibre (Colher de chá ralado (5g): 1)',
    },
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '• Própolis (gotas: 15)',
    },
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 4,
        'prato': '• Cúrcuma (Colher de chá (2,05g): 1)',
    },
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 5,
        'prato': '• Pimenta caiena (Pitada (0,70g): 1)',
    },
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 6,
        'prato': '⦁	Água (Copo médio (200ml): 1)',
    },

    # Café da Manhã - Hipertensão - Metabolismo Lento
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Pão integral (Fatia: 1) ou Cuscuz, de milho, cozido com sal (Grama: 55) ou Batata, doce, cozida (Grama: 80) ou Banana (ouro, prata, d´água, da terra, etc.) Cozido(a) (Grama: 70) ou Inhame (cozido) (Grama: 55) ou Aipim Cozido(a) (Grama: 50) ou Tapioca de goma (Grama: 20)',
    },
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Ovo de galinha Cozido(a) (Unidade: 2) ou Queijo minas frescal (Grama: 60) ou Peito de galinha ou frango Assado(a) (Grama: 80) ou Carne moída Cozido(a) (Grama: 65) ou Atum em conserva (Grama: 70)',
    },
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '⦁	chá de sene (200ml: 1)',
    },
    

    # Refeição 2 - Hipertensão - Metabolismo Lento
    {
        'refeicao': 2,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Banana, prata, crua (Unidade Pequena: 1) ou Maçã (Unidade: 1) ou Uva itália (un: 15) ou Mamão, Papaia, cru (Grama: 210) ou Abacaxi (Grama: 170) ou Goiaba (Grama: 160)',
    },
    {
        'refeicao': 2,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Chá verde (Copo pequeno cheio (165ml): 1)',
    },
    {
        'refeicao': 2,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '⦁	Castanha de caju (Unidade: 6) ou Castanha do Pará sem sal (Unidade (4g): 3)',
    },

    # Almoço - Hipertensão - Metabolismo Lento
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '⦁	Feijão, carioca, cozido (Colher De Sopa Cheia: 3) ou Lentilha cozida (grãos) (Colher de sopa (24g): 1)',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 4,
        'prato': '⦁	Arroz integral (cozido) (Colher de arroz cheia (63g): 2) ou Macarrão Cozido(a) (Grama: 60) ou Macarrão, de arroz, cozido (Grama: 90)',
    },

    # Refeição 4 - Hipertensão - Metabolismo Lento
    {
        'refeicao': 4,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Iogurte desnatado (Copo Americano: 1)',
    },
    

    # Janta - Hipertensão - Metabolismo Lento
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '⦁	Pão integral (Fatia: 1) ou Batata doce cozida sem sal (Grama: 60) ou Aipim Cozido(a) (Grama: 55) ou Banana da terra (Grama: 70)',
    },

    # Refeição 6 - Hipertensão - Metabolismo Lento
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Clara de ovo de galinha (Unidade (34g): 1)',
    },
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Banana, prata, crua (Unidade Pequena: 1) ou Maçã (Unidade: 1) ou pera (Unidade: 1) ou Mamão papaia (Grama: 210) ou Morango (Unidade média (12g): 25) ou Amora (Unidade: 50)',
    },
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '⦁	chá de cavalinha (200ml: 1)',
    },
]

HICO = [

    # Desjejum - Hipertensão - Constipação
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Laranja (Unidade pequena (90g): 1)',
    },
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁	Mamão (Fatia: 1)',
    },
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 3,
        'prato': '⦁	Água (Copo médio (200ml): 1)',
    },

    # Café da Manhã - Hipertensão - Constipação
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Pão integral (Fatia: 1) ou Aipim Cozido(a) (Grama: 50) ou Cuscuz, de milho, cozido com sal (Grama: 55) ou Batata, doce, cozida (Grama: 80) ou Tapioca de goma (Grama: 20) ou Inhame (cozido) (Grama: 55)',
    },
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁	Ovo de galinha Cozido(a) (Unidade: 2) ou Queijo minas frescal (Grama: 60) ou Peito de galinha ou frango Assado(a) (Grama: 80) ou Carne moída Cozido(a) (Grama: 65)',
    },
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 3,
        'prato': '⦁	chá de sene (200ml: 1)',
    },
    
    # Refeição 2 - Hipertensão - Constipação
    {
        'refeicao': 2,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Psylium (Grama: 10) ou Aveia em flocos finos (Colher de sopa (15g): 1)',
    },
    {
        'refeicao': 2,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁	Banana, prata, crua (Unidade Pequena: 1) ou Maçã (Unidade: 1) ou Tangerina (Grama: 160) ou Mamão, Papaia, cru (Grama: 210) ou Melancia (Grama: 250) ou Goiaba (Grama: 160) ou pera (Unidade: 1)',
    },

    # Almoço - Hipertensão - Constipação
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 3,
        'prato': '⦁	Arroz integral (cozido) (Colher de arroz cheia (63g): 2) ou Macarrão, de arroz, cozido (Grama: 90) ou Macarrão Cozido(a) (Grama: 60)',
    },

    # Refeição 4 - Hipertensão - Constipação
    {
        'refeicao': 4,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Iogurte desnatado (Copo Americano: 1)',
    },
    {
        'refeicao': 4,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁	Psylium (Grama: 10) ou Aveia em flocos (Colher De Cha: 2)',
    },

    # Janta - Hipertensão - Constipação
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 3,
        'prato': '⦁	Pão integral (Fatia: 1) ou Batata doce cozida sem sal (Grama: 60) ou Aipim Cozido(a) (Grama: 55) ou Banana da terra (Grama: 70)',
    },

    # Refeição 6 - Hipertensão - Constipação
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁	Aveia em flocos (Colher De Cha: 2)',
    },
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁	Banana, prata, crua (Unidade Pequena: 1) ou Mamão papaia (Grama: 210)',
    },
]

HIIN = [

    # Desjejum - Hipertensão - Insonia
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Chá de cavalinha (200ml)',
    },

    # Café da Manhã - Hipertensão - Insonia
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': 'Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Atum (cru) (Grama: 120) ou Soja (cozida) (Grama: 140) ou Queijo minas frescal (Fatia (30g): 2)',
    },
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': 'Batata doce cozida sem sal (Grama: 55) ou Cuscuz (Grama: 45) ou Inhame (cozido) (Grama: 50) ou Banana da terra Cozido(a) (Grama: 65)',
    },

    # Refeição 2 - Hipertensão - Insonia
    {
        'refeicao': 2,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Castanha de caju (Unidade: 4) ou Castanha do Pará sem sal (Unidade (4g): 2)',
    },

    # Almoço - Hipertensão - Insonia
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': 'Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 3,
        'prato': 'Feijão, carioca, cozido (Colher De Sopa Cheia: 3) ou Lentilha cozida (grãos) (Colher de sopa (24g): 1) ou Grão de bico (cozido) (Colher de sopa (24g): 1)',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 4,
        'prato': 'Arroz integral (cozido) (Colher de arroz cheia (63g): 2) ou Macarrão Cozido(a) (Grama: 60) ou Macarrão, de arroz, cozido (Grama: 90)',
    },
    

    # Refeição 4 - Hipertensão - Insonia
    {
        'refeicao': 4,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - (Colher de sopa (15g): 1)',
    },
    {
        'refeicao': 4,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': 'Iogurte desnatado (Copo Americano: 1)',
    },

    # Janta - Hipertensão - Insonia
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': '• Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 3,
        'prato': 'Batata doce cozida sem sal (Grama: 70) ou Cuscuz, de milho, cozido com sal (Grama: 50) ou Inhame (cozido) (Grama: 60) ou Banana da terra (Grama: 40) ou Pão integral (Fatia: 1',
    },
    
    
    # Refeição 6 - Hipertensão - Insonia
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	CHÁ DE CAMOMILA + MULUNGU + PASSIFLORA 3-5 COLHERES DE CADA EM 500ML DE ÁGUA 30/40MIN ANTES DE DORMIR',
    },
]

HICE = [

    # Desjejum - Hipertensão - Colesterol Elevado
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': 'Água (Copo médio (200ml): 1)',
    },
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': 'Propolis (gotas: 15)',
    },
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 3,
        'prato': 'Gengibre em pó (colher de café: 2)',
    },
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 4,
        'prato': 'Alcachofra (cozida) (Colher de sopa cheia (20g): 1)',
    },
    {
        'refeicao': 0,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 5,
        'prato': 'Canela em pó (Colher de sobremesa (7,3g): 1',
    },

    # Café da Manhã - Hipertensão - Colesterol Elevado
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': 'Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Atum (cru) (Grama: 120) ou Soja (cozida) (Grama: 140) ou Queijo minas frescal (Fatia (30g): 2)',
    },
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': 'Batata doce cozida sem sal (Grama: 55) ou Cuscuz (Grama: 45) ou Inhame (cozido) (Grama: 50) ou Banana da terra Cozido(a) (Grama: 65)',
    },

    # Refeição 2 - Hipertensão - Colesterol Elevado
    {
        'refeicao': 2,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Castanha de caju (Unidade: 4) ou Castanha do Pará sem sal (Unidade (4g): 2)',
    },

    # Almoço - Hipertensão - Colesterol Elevado
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': 'Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 3,
        'prato': 'Feijão, carioca, cozido (Colher De Sopa Cheia: 3) ou Lentilha cozida (grãos) (Colher de sopa (24g): 1) ou Grão de bico (cozido) (Colher de sopa (24g): 1)',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 4,
        'prato': 'Arroz integral (cozido) (Colher de arroz cheia (63g): 2) ou Macarrão Cozido(a) (Grama: 60) ou Macarrão, de arroz, cozido (Grama: 90)',
    },
    
    # Refeição 4 - Hipertensão - Colesterol Elevado
    {
        'refeicao': 4,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - (Colher de sopa (15g): 1)',
    },
    {
        'refeicao': 4,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': 'Iogurte desnatado (Copo Americano: 1)',
    },

    # Janta - Hipertensão - Colesterol Elevado
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': 'Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 3,
        'prato': 'Batata doce cozida sem sal (Grama: 70) ou Cuscuz, de milho, cozido com sal (Grama: 50) ou Inhame (cozido) (Grama: 60) ou Banana da terra (Grama: 40) ou Pão integral (Fatia: 1)',
    },
    
    # Refeição 6 - Hipertensão - Colesterol Elevado
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Água (Copo médio (200ml): 1)',
    },
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': 'Chá, erva, camomila, ebulição (Grama: 2)',
    },
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'CE',
        'ordem': 3,
        'prato': '⦁	Maracujá (Unidade média (45g): 1) ⦁	Obs: Prepare o chá, despejando água fervida sobre a camomila. Deixe tampado por cerca de dez minutos e coe. Bata no liquidificador com a polpa do maracujá, gelo à vontade. Sirva em seguida.',
    },
]

HIAN = [

    # Café da Manhã - Hipertensão - Ansiedade
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Pão integral (Fatia: 1) ou Aipim Cozido(a) (Grama: 50) ou Cuscuz, de milho, cozido com sal (Grama: 55) ou Batata, doce, cozida (Grama: 80) ou Tapioca de goma (Grama: 20) ou Inhame (cozido) (Grama: 55)',
    },
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	Ovo de galinha Cozido(a) (Unidade: 2) ou Queijo minas frescal (Grama: 60) ou Peito de galinha ou frango Assado(a) (Grama: 80) ou Carne moída Cozido(a) (Grama: 65)',
    },
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 3,
        'prato': '⦁	chocolate amargo (Tablete: 1)',
    },

    # Refeição 2 - Hipertensão - Ansiedade
    {
        'refeicao': 2,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Psylium (Grama: 10) ou Aveia em flocos finos (Colher de sopa (15g): 1)',
    },
    {
        'refeicao': 2,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	Banana, prata, crua (Unidade Pequena: 1) ou Maçã (Unidade: 1) ou Tangerina (Grama: 160) ou Mamão, Papaia, cru (Grama: 210) ou Melancia (Grama: 250) ou Goiaba (Grama: 160) ou pera (Unidade: 1)',
    },
    {
        'refeicao': 2,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 3,
        'prato': '⦁	chá de sene (200ml: 1)',
    },

    # Almoço - Hipertensão - Ansiedade
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 3,
        'prato': '⦁	Arroz integral (cozido) (Colher de arroz cheia (63g): 2) ou Macarrão, de arroz, cozido (Grama: 90) ou Macarrão Cozido(a) (Grama: 60)',
    },
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 4,
        'prato': '⦁	Feijão, carioca, cozido (Colher De Sopa Cheia: 3) ou Lentilha cozida (grãos) (Colher de sopa (24g): 1)',
    },

    # Refeição 4 - Hipertensão - Ansiedade
    {
        'refeicao': 4,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Banana, prata, crua (Unidade Pequena: 1) ou Uva itália (un: 15) ou Manga (Grama: 130) ou Amora (Unidade: 50) ou Morango (Unidade média (12g): 20) ou Tangerina (Grama: 160) ou Melancia (Grama: 250) ou pera (Unidade: 1)',
    },
    {
        'refeicao': 4,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	chocolate amargo (Tablete: 1)',
    },
    {
        'refeicao': 4,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 3,
        'prato': '⦁	chá de cavalinha (200ml: 1)',
    },

    # Janta - Hipertensão - Ansiedade
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 3,
        'prato': '⦁	Pão integral (Fatia: 1) ou Batata doce cozida sem sal (Grama: 60) ou Aipim Cozido(a) (Grama: 55) ou Banana da terra (Grama: 70)',
    },


    # Refeição 6 - Hipertensão - Ansiedade
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Água (Copo médio (200ml): 1)',
    },
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	Chá, erva, camomila, ebulição',
    },
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'AN',
        'ordem': 3,
        'prato': '⦁	Maracujá (Unidade média (45g): 1)',
    },
]

HIRL = [

    # Café da Manhã - Hipertensão - Retenção liquida
    {
        'refeicao': 1,
        'principal': 'HI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '',
    },

    # Refeição 2 - Hipertensão - Retenção liquida
    {
        'refeicao': 2,
        'principal': 'HI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '',
    },

    # Almoço - Hipertensão - Retenção liquida
    {
        'refeicao': 3,
        'principal': 'HI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '',
    },

    # Refeição 4 - Hipertensão - Retenção liquida
    {
        'refeicao': 4,
        'principal': 'HI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '',
    },

    # Janta - Hipertensão - Retenção liquida
    {
        'refeicao': 5,
        'principal': 'HI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '',
    },

    # Refeição 6 - Hipertensão - Retenção liquida
    {
        'refeicao': 6,
        'principal': 'HI',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '',
    },
]

# TODOS CARDAPIOS SEM PATOLOGIA PRIMARIA

NPNP = [

    # Desjejum - Nenhuma Patologia Primaria - Nenhuma Patologia Secundaria #
    {
        'refeicao': 0,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '• Chá verde 400ml',
    },

    # Café da Manhã - Nenhuma Patologia Primaria - Nenhuma Patologia Secundaria #
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '• Pão integral (Fatia: 1) ou Aipim Cozido(a) (Grama: 50) ou Cuscuz, de milho, cozido com sal (Grama: 55) ou Batata, doce, cozida (Grama: 80) ou Tapioca de goma (Grama: 20) ou Inhame (cozido) (Grama: 55)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '• Ovo de galinha Cozido(a) (Unidade: 2) ou Queijo minas frescal (Grama: 60) ou Peito de galinha ou frango Assado(a) (Grama: 80) ou Carne moída Cozido(a) (Grama: 65) ou Atum em conserva (Grama: 70)',
    },

    # Refeição 2 - Nenhuma Patologia Primaria - Nenhuma Patologia Secundaria #
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '• Granola (Colher de sopa (13g): 1) ou Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - Quaker® (Colher de sopa (15g): 1) ou Psylium (Grama: 10) ou Semente de chia (Colher de sopa: 5)',
    },
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '• Banana, prata, crua (Unidade Pequena: 1) ou Maçã (Unidade: 1) ou Mamão, Papaia, cru (Grama: 210) ou pera (Unidade: 1) ou Abacate (Grama: 55) ou Tangerina (Grama: 160) ou Uva itália (un: 15) ou Morango (Unidade média (12g): 20) ou Abacaxi (Grama: 170) ou Goiaba (Grama: 160) ou Melancia (Grama: 250) ou Kiwi (Grama: 145) ou Manga (Grama: 130) ou Amora (Unidade: 50)',
    },

    # Almoço - Nenhuma Patologia Primaria - Nenhuma Patologia Secundaria #
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '• Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '• Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 3,
        'prato': '• Feijão, carioca, cozido (Colher De Sopa Cheia: 4) ou Grão de bico (cozido) (Colher de sopa (24g): 2)',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 4,
        'prato': '• Arroz integral (cozido) (Colher de arroz cheia (63g): 4) ou Lentilha cozida (grãos) (Colher de sopa (24g): 7) ou Macarrão (cozido) (Colher de servir (56g): 2) ou Macarrão, de arroz cozido (Grama: 180)',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 5,
        'prato': '• Tangerina (Unidade: 1) ou Kiwi (Unidade: 1) ou Laranja (Unidade: 1)',
    },

    # Refeição 4 - Nenhuma Patologia Primaria - Nenhuma Patologia Secundaria #
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '• Granola (Colher de sopa (13g): 1) ou Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - Quaker® (Colher de sopa (15g): 1) ou Psylium (Grama: 10) ou Semente de chia (Colher de sopa: 5)',
    },
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '• Iogurte desnatado (Copo Americano: 1)',
    },
   

    # Janta - Nenhuma Patologia Primaria - Nenhuma Patologia Secundaria #
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '• Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '• Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 3,
        'prato': '• Batata doce cozida sem sal (Grama: 70) ou Cuscuz, de milho, cozido com sal (Grama: 50) ou Inhame (cozido) (Grama: 60) ou Pão integral (Fatia: 1)',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 4,
        'prato': '• Brócolis (Grama: 50)',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 5,
        'prato': '• chocolate amargo (Tablete: 1)',
    },
    
    # Refeição 6 - Nenhuma Patologia Primaria - Nenhuma Patologia Secundaria #
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 1,
        'prato': '• Clara de ovo de galinha (Unidade (34g): 1)',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 2,
        'prato': '• Banana, prata, crua (Unidade Pequena: 1) ou Maçã (Unidade: 1) ou pera (Unidade: 1) ou Mamão papaia (Grama: 210) ou Morango (Unidade média (12g): 25) ou Amora (Unidade: 50)',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'NP',
        'ordem': 3,
        'prato': '• chá de cavalinha (200ml: 1)',
    },
]

NPML = [

    # Desjejum - Nenhuma Patologia Primaria - Metabolismo Lento
    {
        'refeicao': 0,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Limão espremido (Unidade: 1)',
    },
    {
        'refeicao': 0,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Gengibre (Colher de chá ralado (5g): 1)',
    },
    {
        'refeicao': 0,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '⦁	Própolis (gotas: 15)',
    },
    {
        'refeicao': 0,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 4,
        'prato': '⦁	Cúrcuma (Colher de chá (2,05g): 1)',
    },
    {
        'refeicao': 0,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 5,
        'prato': '⦁	Pimenta caiena (Pitada (0,70g): 1)',
    },
    {
        'refeicao': 0,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 6,
        'prato': '⦁	Água (Copo médio (200ml): 1)',
    },
    

    # Café da Manhã - Nenhuma Patologia Primaria - Metabolismo Lento
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': 'Batata, doce, cozida (Grama: 80) ou Inhame (cozido) (Grama: 55) ou Aipim Cozido(a) (Grama: 50)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Ovo de galinha Cozido(a) (Unidade: 2) ou Queijo minas frescal (Grama: 60) ou Peito de galinha ou frango Assado(a) (Grama: 80) ou Carne moída Cozido(a) (Grama: 65) ou Atum em conserva (Grama: 70)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '⦁	Chá verde (Copo pequeno cheio (165ml): 1)',
    },
    

    # Refeição 2 - Nenhuma Patologia Primaria - Metabolismo Lento
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Banana, prata, crua (Unidade Pequena: 1) ou Maçã (Unidade: 1)',
    },
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Clara de ovo de galinha (Unidade (34g): 2)',
    },
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '⦁	Castanha de caju (Unidade: 6) ou Castanha do Pará sem sal (Unidade (4g): 3)',
    },

    # Almoço - Nenhuma Patologia Primaria - Metabolismo Lento
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 200) ou Patinho Assado(a) (Grama: 175) ou Carne moída (Grama: 160) ou Salmão, filé, com pele, fresco, grelhado (Grama: 150) ou Merluza, filé, assado (Grama: 280)',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '⦁	Feijão, carioca, cozido (Colher De Sopa Cheia: 3) ou Lentilha cozida (grãos) (Colher de sopa (24g): 1)',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 4,
        'prato': '⦁	Arroz integral (cozido) (Colher de arroz cheia (63g): 2) ou Macarrão Cozido(a) (Grama: 60) ou Macarrão, de arroz, cozido (Grama: 90)',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 5,
        'prato': '⦁	Arroz integral (cozido) (Colher de arroz cheia (63g): 2) ou Macarrão Cozido(a) (Grama: 60) ou Macarrão, de arroz, cozido (Grama: 90)',
    },

    # Refeição 4 - Nenhuma Patologia Primaria - Metabolismo Lento
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Granola (Colher de sopa (13g): 1) ou Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - Quaker® (Colher de sopa (15g): 1) ou Psylium (Grama: 10) ou Semente de chia (Colher de sopa: 5)',
    },
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Iogurte desnatado (Copo Americano: 1)',
    },
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 3,
        'prato': '⦁	OMEGA 3 (1 COMPRIMIDO)',
    },

    # Janta - Nenhuma Patologia Primaria - Metabolismo Lento
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    

    # Refeição 6 - Nenhuma Patologia Primaria - Metabolismo Lento
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'ML',
        'ordem': 1,
        'prato': '⦁	CHÁ DE CAMOMILA + MULUNGU + PASSIFLORA 3-5 COLHERES DE CADA EM 500ML DE ÁGUA 30/40MIN ANTES DE DORMIR',
    },
]

NPCO = [

    # Café da Manhã - Nenhuma Patologia Primaria - Constipação
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁ 50 gramas de banana-da-terra, cozida',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁ 1 xicara de café com 1 colher de chá de óleo de coco',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 3,
        'prato': '⦁ 1 fatia de mamão',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 4,
        'prato': '⦁ 1 unidades grandes de ovo, galinha, inteiro, cozido, mexido (61 g)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 5,
        'prato': '⦁ Chá de sene em infusão com 200ml de água',
    },
    
    # Refeição 2 - Nenhuma Patologia Primaria - Constipação
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁ 1 colher de sobremesa rasa de PSYLLIUM',
    },
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁ 1 fatias de mamão Papaia cru (170 g) ou 1 unidade média de pera, cru (178 g) ',
    },

    # Almoço - Nenhuma Patologia Primaria - Constipação
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁ 2 salada de legumes( Brocollis / cenoura/ beterraba )- cerca de 200gramas',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁ 150 gramas de peito de frango, sem pele, grelhado',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 3,
        'prato': '⦁ SALADA DE FOLHAS A VONTADE (ALFACE / COUVE / ACELGA)',
    },

    # Refeição 4 - Nenhuma Patologia Primaria - Constipação
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁ 1 colheres de sobremesa rasas de aveia em flocos crua (5 g) ou 1 colheres de sopa de semente de linhaça (10 g)',
    },
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁ 20 unidades grandes de morango (400 g) ou 1 unidade média de goiaba (170 g)',
    },

    # Janta - Nenhuma Patologia Primaria - Constipação
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁ 35 gramas de banana-da-terra, cozida',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁ 110 gramas de peito de frango, sem pele, cozido',
    },
    
    # Refeição 6 - Nenhuma Patologia Primaria - Constipação
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 1,
        'prato': '⦁ 1 fatia de mamão Papaia cru (170 g)',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 2,
        'prato': '⦁ 1 colheres de sobremesa rasas de aveia em flocos crua (10 g)',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'CO',
        'ordem': 3,
        'prato': '⦁ GLUTAMINA ( 1 COLHER DE SOPA ) – MARCAS – Vitafor/ max titanium',
    },
]

NPIN = [

    # Café da Manhã - Nenhuma Patologia Primaria - Insônia
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Chá de carqueja (200ml)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': '⦁	Mamão(3 fatias)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 3,
        'prato': '⦁	Ovo de galinha ( 1 und)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 4,
        'prato': '⦁	Queijo branco( 1 FATIA) ',
    },
    
    # Refeição 2 - Nenhuma Patologia Primaria - Insônia
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	PSILLIUM (10 GR) Ou SEMENTE DE CHIA ( 2 colheres)',
    },
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': '⦁	Bananas ( 2 unidades)',
    },

    # Almoço - Nenhuma Patologia Primaria - Insônia
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Á VONTADE )',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 3,
        'prato': '⦁	Feijão, carioca, cozido (Colher De Sopa Cheia: 3) ou Lentilha cozida (grãos) (Colher de sopa (24g): 1)',
    },

    # Refeição 4 - Nenhuma Patologia Primaria - Insônia
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Iogurte desnatado (Copo Americano: 1)',
    },
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': '⦁	Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - Quaker® (Colher de sopa (15g): 1) ou Semente de chia (Colher de sopa: 5) ou Psylium (Grama: 10) ou Semente de chia (Colher de sopa: 5)',
    },

    # Janta - Nenhuma Patologia Primaria - Insônia
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	Pão integral (Fatia: 2) ou Cuscuz, de milho, cozido com sal (Grama: 110) ou Batata, doce, cozida (Grama: 160) ou Banana (ouro, prata, d´água, da terra, etc.) Cozido(a) (Grama: 140)',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': '⦁	Ovo de galinha Cozido(a) (Unidade: 2) ou Peito de galinha ou frango Assado(a) (Grama: 80) ou Salmão, filé, com pele, fresco, grelhado (Grama: 60) ou Queijo minas frescal (Grama: 60) ou Atum em conserva (Grama: 70) ou Merluza, filé, assado (Grama: 110)',
    },
    
    # Refeição 6 - Nenhuma Patologia Primaria - Insônia
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 1,
        'prato': '⦁	CHÁ DE CAMOMILA + MULUNGU + PASSIFLORA 3-5 INLHERES DE CADA EM 500ML DE ÁGUA 30/40MIN ANTES DE DORMIR',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'IN',
        'ordem': 2,
        'prato': '⦁	Propolís verde , de abelha (20 gotas)',
    },
]

NPCE = [

    # Café da Manhã - Nenhuma Patologia Primaria - Colesterol Elevado
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Leite de vaca, desnatado, UHT (1 Copo Cheio (200ml))',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': '⦁	Banana (1 Unidade média (75g)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 3,
        'prato': '⦁	Aveia em flocos (3 Colher De Sopa) Ou Semente de chia ( 2 colheres de sopa)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 4,
        'prato': '⦁	Clara de ovo de galinha (Unidade (34g): 5) Ou Atum ( 100g)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 5,
        'prato': '⦁	Maçã (1 Unidade) ⦁	Obs: Leite + Banana + Aveia = Batida de Banana',
    },

    # Refeição 2 - Nenhuma Patologia Primaria - Colesterol Elevado
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Melão (1 Fatia média (90g) Ou Melancia ( 1 fatia) Ou Tangerina ( 1 und ) Ou Kiwi ( 1 und)',
    },

    # Almoço - Nenhuma Patologia Primaria - Colesterol Elevado
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Arroz integral (cozido) (Meia Escumadeira média cheia (59g))',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': '⦁	Frango em pedaços Cozido(a) (1 Escumadeira)',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 3,
        'prato': '⦁	FOLHAS VERDES ESCURAS ( COUVE / REPOLHO/ ALFACE CRESPA ) – A VONTADE',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 4,
        'prato': '⦁	Abacaxi (2 Fatia pequena)',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 5,
        'prato': '⦁	Peito de galinha ou frango (Bife: 2) Ou Peixe (merluza / cavala / tilápia) - 2 bifes - 150g)',
    },

    # Refeição 4 - Nenhuma Patologia Primaria - Colesterol Elevado
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Castanha do Pará sem sal (3 Unidade (4g))',
    },
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': '⦁	Uva itália (Bago (12,4g): 1) Ou Banana (1 und) Ou Kiwi (1 und) Ou Maracujá (1 und)',
    },

    # Janta - Nenhuma Patologia Primaria - Colesterol Elevado
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Filé de frango grelhado (1 Filé pequeno (100g)',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': '⦁	Arroz integral (cozido) (3 Colher de sopa cheia (20g)',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 3,
        'prato': '⦁	Brócolis (cozido) (3 Colher de sopa picado (13,23g)',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 4,
        'prato': '⦁	Agrião (1 Prato sobremesa cheio picado (20g)',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 5,
        'prato': '⦁	Tomate (5 Fatia média (15g)',
    },

    # Refeição 6 - Nenhuma Patologia Primaria - Colesterol Elevado
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 1,
        'prato': '⦁	Água de coco (Copo médio (200ml): 1)',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 2,
        'prato': '⦁	Chá, erva, camomila, ebulição (Grama: 2)',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'CE',
        'ordem': 3,
        'prato': '⦁	Maracujá (Unidade média (45g): 1) ⦁	Obs: Prepare o chá, despejando água fervida sobre a camomila. Deixe tampado por cerca de dez minutos e coe. Bata no liquidificador com a polpa do maracujá, o mel (ou agave) e gelo à vontade. Sirva em seguida.',
    },
]

NPAN = [

    # Café da Manhã - Nenhuma Patologia Primaria - Ansiedade
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Mingau de aveia (30 g de aveia)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	Yogurt desnatado – 100ml)',
    },
    

    # Refeição 2 - Nenhuma Patologia Primaria - Ansiedade
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Granola (Colher de sopa (13g): 1) ou Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - Quaker® (Colher de sopa (15g): 1) ou Psylium (Grama: 10) ou Semente de chia (Colher de sopa: 5)',
    },
    
    # Almoço - Nenhuma Patologia Primaria - Ansiedade
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	SALADA DE FOLHAS A VONTADE',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 200) ou Patinho Assado(a) (Grama: 175) ou Carne moída (Grama: 160) ou Salmão, filé, com pele, fresco, grelhado (Grama: 150) ou Merluza, filé, assado (Grama: 280)',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 3,
        'prato': '⦁	Feijão, carioca, cozido (Colher De Sopa Cheia: 3) ou Lentilha cozida (grãos) (Colher de sopa (24g): 1)',
    },

    # Refeição 4 - Nenhuma Patologia Primaria - Ansiedade
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Banana, prata, crua (Unidade Pequena: 1) ou Uva itália (un: 15) ou Amora (Unidade: 50) ou Tangerina (Grama: 160) ou Abacaxi (Grama: 170)',
    },
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	chocolate amargo (Tablete: 1)',
    },
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 3,
        'prato': '⦁	chá de Carqueja (200ml: 1)',
    },

    # Janta - Nenhuma Patologia Primaria - Ansiedade
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Pão integral (Fatia: 2) Ou Banana (da terra .) Cozido(a) (Grama: 140) Ou Sopa de abobora (150g de abobora)',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	Ovo de galinha Cozido(a) (Unidade: 2) ou Atum em conserva (Grama: 70) ou Queijo minas frescal (Grama: 60) ou Peito de galinha ou frango Assado(a) (Grama: 80) ou Carne moída Cozido(a) (Grama: 65) ou Salmão, filé, com pele, fresco, grelhado (Grama: 60) ou Merluza (cozida) (Grama: 130) ou Patinho Assado(a) (Grama: 70)',
    },
    

    # Refeição 6 - Nenhuma Patologia Primaria - Ansiedade
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 1,
        'prato': '⦁	Água (Copo médio (200ml): 1)',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 2,
        'prato': '⦁	Chá, erva, camomila, ebulição (Grama: 2)',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'AN',
        'ordem': 3,
        'prato': '⦁	Maracujá (Unidade média (45g): 1) ⦁	Obs: Prepare o chá, despejando água fervida sobre a camomila. Deixe tampado por cerca de dez minutos e coe. Bata no liquidificador com a polpa do maracujá, o mel (ou agave) e gelo à vontade. Sirva em seguida.',
    },
]

NPRL = [

    # Café da Manhã - Nenhuma Patologia Primaria - Retenção liquida
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '⦁	Pão integral (Fatia: 1) ou Cuscuz, de milho, cozido com sal (Grama: 55) ou Batata, doce, cozida (Grama: 80) ou Banana (ouro, prata, d´água, da terra, etc.) Cozido(a) (Grama: 70) ou Inhame (cozido) (Grama: 55) ou Aipim Cozido(a) (Grama: 50) ou Tapioca de goma (Grama: 20)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 2,
        'prato': '⦁	Ovo de galinha Cozido(a) (Unidade: 2) ou Queijo minas frescal (Grama: 60) ou Peito de galinha ou frango Assado(a) (Grama: 80) ou Carne moída Cozido(a) (Grama: 65) ou Atum em conserva (Grama: 70)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 3,
        'prato': '⦁	CHÁ DE sene em infusão com 200ml de água',
    },

    # Refeição 2 - Nenhuma Patologia Primaria - Retenção liquida
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '⦁	Granola (Colher de sopa (13g): 1) ou Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - Quaker® (Colher de sopa (15g): 1) ou Psylium (Grama: 10) ou Semente de chia (Colher de sopa: 5)',
    },
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 2,
        'prato': '⦁	Maçã (Unidade: 1) ou Mamão, Papaia, cru (Grama: 210) ou pera (Unidade: 1) Tangerina (Grama: 160) ou Uva itália (un: 15) ou Morango (Unidade média (12g): 20) ou Abacaxi (Grama: 170) ou Goiaba (Grama: 160) ou Melancia (Grama: 250) ou Kiwi (Grama: 145) ou Manga (Grama: 130)',
    },

    # Almoço - Nenhuma Patologia Primaria - Retenção liquida
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 2,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },

    # Refeição 4 - Nenhuma Patologia Primaria - Retenção liquida
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '⦁	Granola (Colher de sopa (13g): 1) ou Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - Quaker® (Colher de sopa (15g): 1) ou Psylium (Grama: 10) ou Semente de chia (Colher de sopa: 5)',
    },
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 2,
        'prato': '⦁	Maçã (Unidade: 1) ou  pera (Unidade: 1) ou Tangerina (Grama: 160) ou Uva itália (un: 15) ou Morango (Unidade média (12g): 20) ou Abacaxi (Grama: 170) ou Goiaba (Grama: 160) ou Melancia (Grama: 250) ou Kiwi (Grama: 145) ou Manga (Grama: 130) ou Amora (Unidade: 50)',
    },

    # Janta - Nenhuma Patologia Primaria - Retenção liquida
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '⦁	Pão integral (Fatia: 1) ou  Batata, doce, cozida (Grama: 80)  Ou Aipim ( 50g) ',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 2,
        'prato': '⦁	Ovo de galinha Cozido(a) (Unidade: 2) ou Atum em conserva (Grama: 70) ou Queijo minas frescal (Grama: 60) ou Peito de galinha ou frango Assado(a) (Grama: 80) ou Carne moída Cozido(a) (Grama: 65) ou Salmão, filé, com pele, fresco, grelhado (Grama: 60) ou Merluza (cozida) (Grama: 130) ou Patinho Assado(a) (Grama: 70)',
    },

    # Refeição 6 - Nenhuma Patologia Primaria - Retenção liquida
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 1,
        'prato': '⦁	Clara de ovo de galinha (Unidade (34g): 1)',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 2,
        'prato': '⦁	Banana, prata, crua (Unidade Pequena: 1) ou Maçã (Unidade: 1) ou pera (Unidade: 1) ou Mamão papaia (Grama: 210) ou Morango (Unidade média (12g): 25) ou Amora (Unidade: 50)',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 3,
        'prato': '⦁	Granola (Colher de sopa (13g): 1) ou Linhaça, semente (Colher De Chá: 3) ou Aveia em flocos finos - Quaker® (Colher de sopa (15g): 1) ou Semente de chia (Colher de sopa: 5) ou Psylium (Grama: 10) ou Semente de chia (Colher de sopa: 5)',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'RL',
        'ordem': 4,
        'prato': '⦁	chá de MULUNGU COM CAMOMILA  (10 GR DE ERVA CADA)',
    },
]

NPCL = [

    # Café da Manhã - Nenhuma Patologia Primaria - Celíaco
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 1,
        'prato': 'Aipim Cozido(a) (Grama: 50) ou Batata, doce, cozida (Grama: 80) ou Banana da terra Cozido(a) (Grama: 70) ou Inhame (cozido) (Grama: 55)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 2,
        'prato': '⦁	Ovo de galinha Cozido(a) (Unidade: 2) ou Peito de galinha ou frango Assado(a) (Grama: 80) ou Carne moída Cozido(a) (Grama: 65)',
    },
    {
        'refeicao': 1,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 3,
        'prato': '⦁	chá de cavalinha (200ml: 1)',
    },

    # Refeição 2 - Nenhuma Patologia Primaria - Celíaco
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 1,
        'prato': '⦁	Granola SEM GLUTEN (Colher de sopa (13g): 1) ou Semente de chia (Colher de sopa: 5) ou Linhaça, semente (Colher De Chá: 3) ou Psylium (Grama: 10)',
    },
    {
        'refeicao': 2,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 2,
        'prato': '⦁	Banana, prata, crua (Unidade Pequena: 1) ou Maçã (Unidade: 1) ou Uva Itália (un: 15) ou Mamão, Papaia, cru (Grama: 210) ou Abacaxi (Grama: 170) ou Goiaba (Grama: 160)',
    },

    # Almoço - Nenhuma Patologia Primaria - Celíaco
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 2,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 200) ou Patinho Assado(a) (Grama: 175) ou Carne moída (Grama: 160) ou Salmão, filé, com pele, fresco, grelhado (Grama: 150) ou Merluza, filé, assado (Grama: 280)',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 3,
        'prato': '⦁	Azeite de oliva (Colher de chá (2,4ml): 1)',
    },
    {
        'refeicao': 3,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 4,
        'prato': '⦁	Tangerina (Unidade: 1)',
    },

    # Refeição 4 - Nenhuma Patologia Primaria - Celíaco
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 1,
        'prato': '⦁	Iogurte desnatado (Copo Americano: 1)',
    },
    {
        'refeicao': 4,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 2,
        'prato': '⦁	Clara de ovo de galinha (Unidade (34g): 1)',
    },

    # Janta - Nenhuma Patologia Primaria - Celíaco
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 1,
        'prato': '⦁	Salada ou verdura cozida, ou folhas em geral (Escumadeira: 2) 84g',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 2,
        'prato': '⦁	Peito de galinha ou frango Assado(a) (Grama: 150) ou Patinho Assado(a) (Grama: 130) ou Merluza, filé, assado (Grama: 210) ou Carne moída (Grama: 120) ou Salmão, filé, com pele, fresco, grelhado (Grama: 110)',
    },
    {
        'refeicao': 5,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 3,
        'prato': '⦁	Batata doce cozida sem sal (Grama: 100) ou Aipim (Grama: 80) ou Inhame (cozido) (Grama: 90) ou Banana da terra (Grama: 120)',
    },

    # Refeição 6 - Nenhuma Patologia Primaria - Celíaco
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 1,
        'prato': '⦁	Clara de ovo de galinha (Unidade (34g): 1)',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 2,
        'prato': '⦁	Banana, prata, crua (Unidade Pequena: 1) ou Maçã (Unidade: 1) ou pera (Unidade: 1) ou Mamão papaia (Grama: 210) ou Morango (Unidade média (12g): 25) ou Amora (Unidade: 50)',
    },
    {
        'refeicao': 6,
        'principal': 'NP',
        'secundaria': 'CL',
        'ordem': 3,
        'prato': '⦁	chá de cavalinha (200ml: 1)',
    },
]

print('inserindo dados')
alterados = 0
inseridos = 0
cardapios = Cardapio.objects.all()
for cardapio in (
    DINP, DIML, DICO, DIIN, DICE, DIAN, DIRL, HINP, HIML, HICO, HIIN, HICE, HIAN, HIRL, NPNP, NPML, NPCO, NPIN, NPCE, NPAN, NPRL, NPCL):
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