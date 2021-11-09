from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from permissoes.models import Cargo


class CargoSerializer(ModelSerializer):

    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    email = SerializerMethodField()

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

    class Meta:
        model = Cargo
        fields = '__all__'