from conta.models import Usuario
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import serializers

from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings


class UsuarioSerializer(serializers.ModelSerializer):

    ativo = serializers.SerializerMethodField()

    def get_ativo(self, obj):
        return obj.ativo
    
    class Meta:
        model = Usuario        
        fields = '__all__'
        
    
class ContaSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        if User.objects.filter(username=validated_data['email']).last():
            raise serializers.ValidationError({'Email': 'Este Email já está cadastrado!'})

        user = User.objects.create(
            username = validated_data['email'], 
            first_name = validated_data['first_name'], 
            last_name = validated_data['last_name'], 
            email = validated_data['email'], 
        )

        user.set_password(validated_data['password']) 
        user.save()
        
        return user
    
    perfil = serializers.SerializerMethodField()

    def get_perfil(self, obj):
        if obj.is_staff:
            return 'desenvolvedor'
       
        cargo = obj.cargo_set.last()
        if cargo:
            return cargo.cargo
        else:
            return 'usuario'

    class Meta:
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
        }
        fields = ['id', 'first_name', 'last_name', 'password', 'email', 'perfil']

class AtualizarContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class MudarSenhaSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)



# ========= login ==========================
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

class CustomJWTSerializer(JSONWebTokenSerializer):

    username_field = 'email_cpf_cnpj'

    def validate(self, attrs):

        password = attrs.get("password")
        username = attrs.get("email_cpf_cnpj")
        
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None: 
            usuario = Usuario.objects.filter(cpf_ou_cnpj=username).first()
            if usuario is not None:
                user_obj = usuario.user

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
                        raise serializers.ValidationError({'login': msg})

                    payload = jwt_payload_handler(user)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = 'Não foi possível fazer login com as credenciais fornecidas.'
                    raise serializers.ValidationError({'login': msg})

            else:
                msg = f'Deve incluir "{self.username_field}" e "senha".'
                raise serializers.ValidationError({'login': msg})

        else:
            msg = 'Conta com este CPF ou email não existe'
            raise serializers.ValidationError({'login': msg})