from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    @staticmethod
    def validate_cpf(cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve ter 11 dígitos')
        return cpf

    @staticmethod
    def validate_nome(nome):
        if not nome.isalpha():
            raise serializers.ValidationError('O nome deve ser composto apenas por caracteres '
                                              'alfabéticos')
        return nome

    @staticmethod
    def validate_rg(rg):
        if len(rg) != 9:
            raise serializers.ValidationError('O RG deve ter 9 dígitos')
        return rg

    @staticmethod
    def validate_celular(celular):
        if len(celular) != 11:
            raise serializers.ValidationError('O celular deve ter 11 dígitos. (xxXXXXXXXXX) - '
                                              'DDD + número')
        return celular



