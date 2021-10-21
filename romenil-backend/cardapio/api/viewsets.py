from datetime import datetime, timedelta, timezone

from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.template.loader import render_to_string

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from cardapio.api.serializers import CardapioSerializer
from cardapio.models import Cardapio

from formulario.models import Formulario

from .cardapio import gerar_cardapio


class CardapioViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):  

        usuario = request.user.usuario_set.last()
        formulario = usuario.formulario_set.last()
        dados = None
        pronto = False

        if Formulario:
            if formulario.modificado_em < datetime.now(timezone.utc) - timedelta(hours=2):
                cardapios = gerar_cardapio(formulario)
                dados = CardapioSerializer(cardapios, many=True).data
                pronto = True

        return Response({'pronto': pronto, 'dados': dados})

class CardapioEmailViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        usuario = request.user.usuario_set.last()
        formulario = usuario.formulario_set.last()
        dados = None
        pronto = False

        if Formulario:
            if formulario.modificado_em < datetime.now(timezone.utc) - timedelta(hours=2):
                cardapios = gerar_cardapio(formulario)
                pronto = True

                desjejum = cardapios.filter(refeicao=0).values_list('prato')
                cafeManha = cardapios.filter(refeicao=1).values_list('prato')
                refeicao2 = cardapios.filter(refeicao=2).values_list('prato')
                almoco = cardapios.filter(refeicao=3).values_list('prato')
                refeicao4 = cardapios.filter(refeicao=4).values_list('prato')
                janta = cardapios.filter(refeicao=5).values_list('prato')
                refeicao6 = cardapios.filter(refeicao=6).values_list('prato')
             
        cardapio = render_to_string('cardapio/cardapio.html',{
            'pronto': pronto, 
            'conta': request.user,
            'desjejum': desjejum[0],
            'cafeManha': cafeManha[0],
            'refeicao2': refeicao2[0],
            'almoco': almoco[0],
            'refeicao4': refeicao4[0],
            'janta': janta[0],
            'refeicao6': refeicao6[0]
        })  
        print(cardapio)

        subject = u"Cardápio"
        from_email = u'naoresponda@romenilalencar.com.br'
        msg = EmailMultiAlternatives(subject, cardapio, from_email,        
                                    [request.user.email])
        msg.attach_alternative(cardapio, "text/html")
        msg.send()

        print('enviado')
       
        status_code = status.HTTP_200_OK
        
        return Response(status=status_code)



