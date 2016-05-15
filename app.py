# -*- coding: UTF-8 -*-

import re

def cadastrar(nomes):
	print 'Digite o nome:'
	nome = raw_input();
	nomes.append(nome)

def listar(nomes):
	print 'Listando nomes:'
	for nome in nomes:
		print nome

def remover(nomes):
	print 'Qual nome você gostaria de remover?'
	nome_a_ser_removido = raw_input()
	nomes.remove(nome_a_ser_removido)

def alterar(nomes):
	print 'Qual nome você gostaria de alterar?'
	nome_atual = raw_input()
	if (nome_atual in nomes):
		print 'Informe o novo nome:'
		novo_nome = raw_input()
		index_nome = nomes.index(nome_atual)
		nomes[index_nome] = novo_nome
	else:
		print 'Desculpe, mas não encontramos o nome %s' % (nome_atual)


def procurar(nomes):
	print 'Digite o nome a ser procurado:'
	nome_procurado = raw_input()
	
	if (nome_procurado in nomes):
		print 'Encontramos %s na posição %s' % (nome_procurado, nomes.index(nome_procurado))
	else:
		print 'Desculpe, mas não conseguimos encontrar %s' % (nome_procurado)

def procurar_regex(nomes):
	print 'Digite a expressão regular'
	regex = raw_input()
	nomes_concatenados = ' '.join(nomes)
	resultados = re.findall(regex, nomes_concatenados)
	print 'Encontramos os seguintes resultados:'
	print resultados

def menu():
	nomes = []
	escolha = ''
	while(escolha != '0'):
		print 'Digite 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para procurar, 6 para procurar com regex e 0 para terminar'
		escolha = raw_input();

		if (escolha == '1'):
			cadastrar(nomes)

		if (escolha == '2'):
			listar(nomes)

		if (escolha == '3'):
			remover(nomes)

		if (escolha == '4'):
			alterar(nomes)

		if (escolha == '5'):
			procurar(nomes)

		if (escolha == '6'):
			procurar_regex(nomes)

menu()