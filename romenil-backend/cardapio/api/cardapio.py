from cardapio.models import Cardapio

'''
LEGENDA PATOLOGIAS:
# Patologias principais
PDI: Diabetes
PHI: Hipertensao
PNP: Nenhuma Patologia principal

# Patologias secundárias
ML: Metabolismo Lento
CO: Constipação
IN: Insonia
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

    cardapios = Cardapio.objects.all()

    # diabetes
    if diabetes:
        cardapios = cardapios.filter(principal='DI')
    elif hipertensao:
        cardapios = cardapios.filter(principal='HI')
    else:
        cardapios = cardapios.filter(principal='NP')

    if metabolismo_lento:
        cardapios = cardapios.filter(secundaria='ML')
    elif constipacao:
        cardapios = cardapios.filter(secundaria='CO')
    elif insonia:
        cardapios = cardapios.filter(secundaria='IN')
    elif colesterol_elevado:
        cardapios = cardapios.filter(secundaria='CE')
    elif ansiedade:
        cardapios = cardapios.filter(secundaria='AN')
    elif retencao_liquida:
        # retenção liquida não conta se tiver diabetes ou hipertensão
        if diabetes or hipertensao:
            cardapios = cardapios.filter(secundaria='NP')
        else:
            cardapios = cardapios.filter(secundaria='RL')
    else:
        cardapios = cardapios.filter(secundaria='NP')

    return cardapios