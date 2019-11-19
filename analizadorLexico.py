import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = [
	'INICIAR',
	'PROCESO',
	'MIENTRAS',
	'PARA',
	'VAR',
	'SI',
	'SINO_SI',
	'SINO',
	'IMPRIMIR',
	'LEER'
]

tokens = reservadas+['ID','NUMERO','CADENA','MAS','MENOS','MULT','DIV',
		'DIF','ASIG','NEG','LT','LTE','GT','GTE', 'IGUAL', 'INC', 'DIS',
		'I_PAR', 'D_PAR','COMA','PUNTO_COMA',
		'I_LL','D_LL', 'Y', 'O'
		]

t_ignore = '\t '
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULT = r'\*'
t_DIV = r'/'
t_DIF = r'<>'
t_ASIG = r'<-'
t_NEG = r'~'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_I_PAR = r'\('
t_D_PAR = r'\)'
t_COMA = r','
t_PUNTO_COMA = r';'
t_I_LL = r'{'
t_D_LL = r'}'
t_IGUAL = r'=='
t_INC = r'\+\+'
t_DIS = r'\-\-'
t_Y = r'\^\^'
t_O = r'//'

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		#reservadas.get(t.value,'ID')
		t.type = t.value

	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

#dsfjksdlgjklsdgjsdgslxcvjlk-,.
def t_COMMENT(t):
	r'\#.*'
	pass

def t_CADENA(t):
	r'\"[a-zA-Z0-9_\s\-\+\.]*\"'
	return t

def t_NUMERO(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print ("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)

analizador = lex.lex()