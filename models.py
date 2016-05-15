# -*- coding: UTF-8 -*-

class Perfil(object):
	'Classe padrão para perfis de usuários'

	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0

	def imprimir(self):
		print 'Nome: %s, Telefone: %s, Empresa: %s, Curtidas: %s' % (self.nome, self.telefone, self.empresa, self.__curtidas)

	def obter_curtidas(self):
		return self.__curtidas

	def curtir(self):
		self.__curtidas += 1


class Data(object):
	'Classe para representar uma Data(sem hora) e imprimir uma data formatada.'

	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def imprime(self):
		print '%s/%s/%s' % (self.dia, self.mes, self.ano)


class Pessoa(object):
	'Classe padrão para pessoas'

	def __init__(self, nome, peso, altura):
		self.nome = nome
		self.peso = peso
		self.altura = altura
		self.imc = peso / (altura * altura)

	def imprime_imc(self):
		print 'Imc de %s: %s' % (self.nome, self.imc)