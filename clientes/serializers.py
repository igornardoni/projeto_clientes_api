from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "Número de CPF inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua números ou caracteres especiais "
                                                       "neste campo"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "Número de RG inválido"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError(
                {'celular': 'O número de celular deve seguir este modelo: 11 91234-1234.'})
        return data

