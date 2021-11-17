from datetime import datetime, timedelta, timezone

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from cardapio.api.serializers import CardapioSerializer

from formulario.models import Formulario

from .cardapio import gerar_cardapio


class CardapioViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):  

        usuario = request.user.usuario_set.last()
        formulario = usuario.formulario_set.last()
        completed_form = formulario is not None
        dados = None
        pronto = False

        if completed_form:
            if formulario.modificado_em < datetime.now(timezone.utc) - timedelta(hours=2):
                cardapios = gerar_cardapio(formulario)
                dados = CardapioSerializer(cardapios, many=True).data
                pronto = True

        return Response({'pronto': pronto, 'dados': dados, 'completed_form': completed_form})

class CardapioEmailViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        usuario = request.user.usuario_set.last()
        formulario = usuario.formulario_set.last()
        pronto = False

        if Formulario:
            if formulario.modificado_em < datetime.now(timezone.utc) - timedelta(hours=2):
                cardapios = gerar_cardapio(formulario)
                pronto = True

                desjejum = cardapios.filter(refeicao=0)
                cafeManha = cardapios.filter(refeicao=1)
                refeicao2 = cardapios.filter(refeicao=2)
                almoco = cardapios.filter(refeicao=3)
                refeicao4 = cardapios.filter(refeicao=4)
                janta = cardapios.filter(refeicao=5)
                refeicao6 = cardapios.filter(refeicao=6)
       
        cardapio = render_to_string('cardapio/cardapio.html',{
            'pronto': pronto, 
            'conta': request.user,
            'desjejum': desjejum,
            'cafeManha': cafeManha,
            'refeicao2': refeicao2,
            'almoco': almoco,
            'refeicao4': refeicao4,
            'janta': janta,
            'refeicao6': refeicao6
        })  

        subject = "Cardápio"
        from_email = 'Romenil Alencar <naoresponda@romenilalencar.com.br>'
        texto = cardapio
        msg = EmailMultiAlternatives(
            subject, 
            texto, 
            from_email,        
            [request.user.email]
        )
        msg.attach_alternative(cardapio, "text/html")
        msg.send()
       
        status_code = status.HTTP_200_OK
        
        return Response(status=status_code)



