from cardapio.models import Cardapio


print("Iniciando")

# TODOS OS CARDÁPIOS DE DIABETES

DINP = [

    # Café da Manhã - Diabetes - Nenhuma Patologia Secundaria #
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

    # Refeição 2 - Diabetes - Nenhuma Patologia Secundaria #
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

    # Almoço - Diabetes - Nenhuma Patologia Secundaria #
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

    # Refeição 4 - Diabetes - Nenhuma Patologia Secundaria #
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

    # Janta - Diabetes - Nenhuma Patologia Secundaria #
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
    
    # Refeição 6 - Diabetes - Nenhuma Patologia Secundaria #
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
        'prato': '•	DESJEJUM SHOT METABOLISMO - Limão espremido (Unidade: 1)',
    },
    {
        'refeicao': 1,
        'principal': 'DI',
        'secundaria': 'ML',
        'ordem': 2,
        'prato': '• Gengibre (Colher de chá ralado (5g): 1)',
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
        'ordem': 3,
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
        'ordem': 1,
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
        'prato': '•	Castanha de caju (Unidade: 4) ou Castanha do Pará sem sal (Unidade (4g): 2) ',
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
        'prato': '•	Ovo de galinha(mexido ou cozido) (3 Unidades) Ou Atum (120g)',
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
        'prato': '•	Almoço - Diabetes - Retenção liquida',
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