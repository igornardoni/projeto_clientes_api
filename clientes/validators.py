from clientes.serializers import ClienteSerializer
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve ter 11 dígitos')
        return cpf


    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError('O nome deve ser composto apenas por caracteres '
                                              'alfabéticos')
        return nome


    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError('O RG deve ter 9 dígitos')
        return rg


    def validate_celular(self, celular):
        if len(celular) != 11:
            raise serializers.ValidationError('O celular deve ter 11 dígitos. (xxXXXXXXXXX) - '
                                              'DDD + número')
        return celular
