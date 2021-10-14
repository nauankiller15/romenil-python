import unittest

class Patologia:

    def __init__(self, hipertensao, diabetes, metabolismo_lento, hipotireoidismo, retencao_liquida, insonia, constipacao, 
        colesterol_elevado, ansiedade, gordura_no_figado, anemia):

        self.hipertensao = hipertensao
        self.diabetes = diabetes
        self.metabolismo_lento = metabolismo_lento
        self.hipotireoidismo = hipotireoidismo
        self.retencao_liquida = retencao_liquida
        self.insonia = insonia
        self.constipacao = constipacao
        self.colesterol_elevado = colesterol_elevado
        self.ansiedade = ansiedade
        self.gordura_no_figado = gordura_no_figado
        self.anemia = anemia

class Alergia:

    def __init__(self, lactose, frutos_do_mar, ovo, soja, amendoim):

        self.lactose = lactose
        self.frutos_do_mar = frutos_do_mar
        self.ovo = ovo
        self.soja = soja
        self.amendoim = amendoim
        
   
class EstiloDeVida:

    def __init__(self, vegano, vegetariano):

        self.vegano = vegano
        self.vegetariano = vegetariano
    