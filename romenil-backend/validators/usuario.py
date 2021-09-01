from django.core.exceptions import ValidationError
from re import match

def cpf_pattern(cpf):

   pattern = r"^(\d{3}.){2}\d{3}-\d{2}$"

   return bool(match(pattern, cpf))


def cpf_is_valid(input_cpf:str):
    """
    Validador de CPF
    """
    
    padrao = cpf_pattern(input_cpf)
    
    if padrao:
        cpf = input_cpf.replace('-', '').replace('.', '')

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

    raise ValidationError({'CPF': 'CPF inválido'})