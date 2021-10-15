'''

LEGENDA PATOLOGIAS:
# Patologias principais
PDI: Diabetes
PHI: Hipertensao
PNP: Nenhuma Patologia principal

# Patologias secundárias
ML: Metabolismo Lento
CO: Constipação
IS: Insonia
CE: Colesterol Elevado
AN: Ansiedade
RL: Retensão Liquida
NP: Nenhuma Patologia secundária
'''

def gerar_cardapio(patologia):

    diabetes = patologia.diabetes
    hipertensao = patologia.hipertensao
    metabolismo_lento = patologia.metabolismo_lento
    constipacao = patologia.constipacao
    insonia = patologia.insonia
    colesterol_elevado = patologia.colesterol_elevado
    ansiedade = patologia.ansiedade
    retencao_liquida = patologia.retencao_liquida

    cardapio = ''

    # diabetes
    if diabetes:
        cardapio += 'PDI'
    elif hipertensao:
        cardapio += 'PHI'
    else:
        cardapio += 'PNP'

    if metabolismo_lento:
        cardapio += 'SML'
    elif constipacao:
        cardapio += 'SCO'
    elif insonia:
        cardapio += 'SIN'
    elif colesterol_elevado:
        cardapio += 'SCE'
    elif ansiedade:
        cardapio += 'SAN'
    elif retencao_liquida:
        cardapio += 'SRL'
    else:
        cardapio += 'SNP'

    return cardapio