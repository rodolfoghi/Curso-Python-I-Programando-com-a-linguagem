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

	@classmethod
	def gerar_perfis(classe, nome_arquivo):
		arquivo = open(nome_arquivo, 'r')
		perfis = []
		
		for linha in arquivo:
			valores = linha.split(',')

			if (len(valores) is not 3):
				raise Perfil_Error('Uma linha no arquivo deve ter 3 valores')

			perfis.append(classe(*valores))
		
		arquivo.close()
		
		return perfis

class Perfil_Vip(Perfil):
	'Classe padrão para perfis de usuários vip'

	def __init__(self, nome, telefone, empresa, apelido=''):
		super(Perfil_Vip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def obter_creditos(self):
		return super(Perfil_Vip, self).obter_curtidas() * 10.0


class Perfil_Error(Exception):
	def __init__(slef, mensagem):
		self.mensagem = mensagem

	def __str__(self):
		return repr(self.mensagem)


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