from conta.models import Usuario
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User

from rest_framework import serializers

from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings

from validators.usuario import cpf_or_cnpj_valid


class UserSerializer(serializers.ModelSerializer):
    
    PLATAFORMAS = {'hotmart','eduzz'}
    
    cpf_ou_cnpj = serializers.CharField(max_length=18, validators=[cpf_or_cnpj_valid])
    celular = serializers.CharField(max_length=14)  
    plataforma = serializers.ChoiceField(choices=PLATAFORMAS)  


    class Meta:
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
            'cpf_ou_cnpj': {'write_only': True},
            'celular': {'write_only': True}, 
            'plataforma': {'write_only': True}
        }
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'cpf_ou_cnpj', 'celular', 'plataforma']

    def get_cpf_ou_cnpj(self, obj):
        return 'dadada'

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'], 
            last_name = validated_data['last_name'], 
            email = validated_data['email'], 
        )

        user.set_password(validated_data['password']) 
        user.save()

        Usuario.objects.create(
            usuario = user,
            cpf_ou_cnpj = validated_data['cpf_ou_cnpj'],
            celular = validated_data['celular'],
            plataforma =  validated_data['plataforma']
        )

        return user


User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'email_ou_cpf'

    def validate(self, attrs):

        password = attrs.get("password")
        user_obj = User.objects.filter(email=attrs.get("email_ou_cpf")).first() or User.objects.filter(username=attrs.get("email_ou_cpf")).first()
        if user_obj is not None:
            credentials = {
                'username':user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                if user:
                    if not user.is_active:
                        msg = 'A conta do usuário está desabilitada.'
                        raise serializers.ValidationError(msg)

                    payload = jwt_payload_handler(user)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = 'Não foi possível fazer login com as credenciais fornecidas.'
                    raise serializers.ValidationError(msg)

            else:
                msg = f'Deve incluir "{self.username_field}" e "senha".'
                raise serializers.ValidationError(msg)

        else:
            msg = 'Conta com este CPF ou email não existe'
            raise serializers.ValidationError(msg)