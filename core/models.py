from django.db import models

# Create your models here.


class Trabalhador(models.Model):
    nome = models.CharField('Nome', max_length=400)
    ano = models.IntegerField('Ano')
    profissao = models.CharField('profissão',max_length=200)
    ano_contrato = models.IntegerField('Anos de contrato')
    nuit = models.IntegerField('Nuit')
    bi = models.CharField('N° de BI', max_length=50)
    salario = models.IntegerField('salario')

    def __str__(self):
        return self.nome and str(self.id)
