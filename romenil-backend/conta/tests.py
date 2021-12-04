from django.contrib.auth.models import User
from django.template import response
from django.test import TestCase

class UserTeste(TestCase):

    def setUp(self) -> None:
        response = self.client.post('/conta/criar-conta/', {
            'username': 'teste@teste.com',
            'first_name': 'teste',
            'last_name': 'do sistema',
            'email': 'teste@teste.com',
            'password': 'teste',
        })

        self.assertEqual(response.status_code, 201)
        return super().setUp()

    def test_criar_usuario(self):
       
        usuario = User.objects.filter(email='teste@teste.com')
        self.assertIsNotNone(usuario)

    def test_login_usuario(self):
        response = self.client.post('/conta/login/', {
            'email_cpf_cnpj': 'teste@teste.com',
            'password': 'teste',
        })

        self.assertEqual(response.status_code, 200)

    def test_mudar_senha(self):

        response = self.client.post('/conta/mudar-senha/', {
            'old_password': 'teste',
            'password1': 'teste122',
            'password2': 'teste122',
        })
