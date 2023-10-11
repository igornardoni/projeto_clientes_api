from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=32, blank=False, null=False)
    cpf = models.CharField(max_length=11, unique=True, blank=False, null=False)
    rg = models.CharField(max_length=9, unique=True, blank=False, null=False)
    celular = models.CharField(max_length=13, unique=True, blank=True, null=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome



