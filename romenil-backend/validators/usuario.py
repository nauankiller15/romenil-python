from django.core.exceptions import ValidationError
from re import match

def cpf_pattern(cpf):

    pattern = r"^\d{11}$"
   
    return bool(match(pattern, cpf))

def cnpj_pattern(cnpj):
   pattern = r"^\d{14}$"

   return bool(match(pattern, cnpj))


def cpf_or_cnpj_valid(input:str):
    """
    Validador de CPF e CNPJ
    """
    
    padrao_cpf = cpf_pattern(input)
    
    if padrao_cpf:
        cpf = input.replace('-', '').replace('.', '')

        if len(set(list(cpf))) != 1:

            soma = 0
            for (digito, i) in zip(cpf[:10], range(10, 1, -1)):
                soma += int(digito) * i
            
            digito = ((soma * 10) % 11) % 10

            if digito == int(cpf[9]):
                soma = 0
                for (digito, i) in zip(cpf[:11], range(11, 1, -1)):
                    soma += int(digito) * i
                
                digito = ((soma * 10) % 11) % 10

                if digito == int(cpf[10]):
                    return

        raise ValidationError('CPF inválido')
    
    padrao_cnpj = cnpj_pattern(input)
    
    if padrao_cnpj:

        cnpj = input.replace('-', '').replace('.', '').replace('/', '')

        if len(set(list(cnpj))) != 1:

            soma = 0
            pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            for (digito, i) in zip(cnpj[:12], pesos[1:]):
                soma += int(digito) * i
            
            digito = ((soma * 10) % 11) % 10

            if digito == int(cnpj[12]):
                soma = 0
                for (digito, i) in zip(cnpj[:13], pesos):
                    soma += int(digito) * i
                
                digito = ((soma * 10) % 11) % 10

                if digito == int(cnpj[13]):
                    return

        raise ValidationError('CNPJ inválido')
    raise ValidationError('CPF ou CNPJ inválido')
