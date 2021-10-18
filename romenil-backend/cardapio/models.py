from django.db.models import Model
from django.db.models.fields import CharField, IntegerField, TextField

class Cardapio(Model):

    PRINCIPAL_CHOICES = (
        ('DI', 'Diabetes'),
        ('HI', 'Hipertensao'),
        ('NP', 'Nenhuma Patologia principal'),
    )

    SECUNDARIO_CHOICES = (
        ('ML', 'Metabolismo Lento'),
        ('CO', 'Constipação'),
        ('IS', 'Insonia'),
        ('CE', 'Colesterol Elevado'),
        ('AN', 'Ansiedade'),
        ('RL', 'Retensão Liquida'),
        ('NP', 'Nenhuma Patologia secundária'),
    )

    REFEICAO_CHOICES = (
        (1, 'Café da manhã'),
        (2, 'Refeição 2'),
        (3, 'Almoço'),
        (4, 'Refeição 4'),
        (5, 'Janta'),
        (6, 'Refeição 6'),
    )

    principal = CharField(max_length=2, choices=PRINCIPAL_CHOICES)
    secundaria = CharField(max_length=2, choices=SECUNDARIO_CHOICES)
    refeicao = IntegerField(choices=REFEICAO_CHOICES)
    ordem = IntegerField()
    prato = TextField()

    def __str__(self):
        return f'{self.principal}{self.secundaria} - {self.refeicao} - {self.ordem}'

    class Meta:
        ordering = ['-principal', '-secundaria', '-refeicao', '-ordem', '-id']