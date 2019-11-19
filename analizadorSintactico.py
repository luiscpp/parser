import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from sys import stdin
from mainwindow_ui import *

errorValue = None


precedence = (
	('right', 'INICIAR'),
	('right', 'PROCESO'),
	('right', 'SI'),
	('right', 'SINO'),
	('right', 'SINO_SI'),
	('right', 'MIENTRAS'),
	('right', 'PARA'),
	('right', 'VAR'),
	('right', 'ASIG'),
	('right', 'ID'),
	('left', 'IMPRIMIR'),
	('right', 'LEER'),
	('left','NEG'),
	('left','LT','LTE','GT','GTE', 'IGUAL'),
	('left','MAS','MENOS'),
	('left','MULT','DIV'),
	('left','INC','DIS'),
	('left','Y'),
	('left','O'),
	('right','DIF', 'IGUAL'),
	('left','I_PAR','D_PAR'),
	('left','I_LL','D_LL')
	)

def p_block(p):
	'''block : INICIAR PROCESO I_PAR D_PAR I_LL lineascodigos D_LL'''
	print("block")

def p_lineascodigos(p):
	'''lineascodigos : lineacodigo
		| '''
	print("lineascodigo")

def p_lineacodigo(p):
	'''lineacodigo : lineacodigo linea
		| linea'''
	print("lineacodigo")

def p_linea(p):
	'''linea : imprimir PUNTO_COMA
		| leer PUNTO_COMA
		| crearvariable PUNTO_COMA
		| cambiarvalor PUNTO_COMA
		| incrementardisminuir PUNTO_COMA
		| ciclocondicion'''
	print("linea")

def p_cambiarvalor(p):
	'''cambiarvalor : ID ASIG cambiovalor'''
	print("cambiarvalor")

def p_cambiovalor(p):
	'''cambiovalor : ID
			| NUMERO
			| aritmetica'''
	print("cambiovalor")

def p_operacionasignacion(p):
	'''operacionasignacion : aritmetica'''
	print("operacionasignacion")

def p_incrementardisminuir(p):
	'''incrementardisminuir : ID tipoincrementardisminuir'''
	print("incrementardisminuir")

def p_tipoincrementardisminuir(p):
	'''tipoincrementardisminuir : INC
			| DIS'''
	print("tipoincrementardisminuir")
	
def p_imprimir(p):
	'''imprimir : IMPRIMIR I_PAR tipoimprimir D_PAR '''
	print("imprimir")

def p_leer(p):
	'''leer : LEER I_PAR tipoimprimir D_PAR '''
	print("leer")

def p_aritmetica(p):
	'''aritmetica : operacioncomun'''
	print("aritmetica")

def p_asignarvalor(p):
	'''asignarvalor : ASIG NUMERO
			| ASIG ID'''
	print("asignarvalor")

def p_operacioncomun(p):
	'''operacioncomun : operando operador operando
			| operando operador operando operador operacioncomun
			| operando'''
	print("operacioncomun")

def p_operador(p):
	'''operador : MAS
			| MENOS
			| MULT
			| DIV
			| DIF
			| IGUAL'''
	print("operador")

def p_operando(p):
	'''operando : NUMERO
			| ID'''
	print("operando")

def p_tipoimprimir(p):
	'''tipoimprimir : ID
			| CADENA
			| NUMERO
			| CADENA MAS tipoimprimir
			| ID MAS tipoimprimir
			| NUMERO MAS imprimir'''
	print("tipoimprimir")

def p_crearvariable(p):
	'''crearvariable : VAR ID
			| VAR ID asignarvalor
			| VAR ID asignarvalor COMA otravariable
			| VAR ID COMA otravariable'''
	print("crearvariable")

def p_otravariable(p):
	'''otravariable : ID
			| ID COMA otravariable
			| ID asignarvalor
			| ID asignarvalor COMA otravariable'''
	print("otravariable")

def p_ciclocondicion(p):
	'''ciclocondicion : condicional
			| mientras
			| ciclofor'''
	print("ciclocondicion")

def p_mientras(p):
	'''mientras : MIENTRAS condicion I_LL lineacodigo D_LL'''
	print("mientras")

def p_condicional(p):
	'''condicional : condicionsi
			| condicionsi condicionno
			| condicionsi condicionsino condicionno'''
	print("condicional")

def p_condicionsi(p):
	'''condicionsi : SI I_PAR condicion D_PAR I_LL lineacodigo D_LL '''
	print("condicionsi")

def p_condicionsino(p):
	'''condicionsino : SINO_SI I_PAR condicion D_PAR I_LL lineacodigo D_LL
			| SINO_SI I_PAR condicion D_PAR I_LL lineacodigo D_LL condicionsino'''
	print("condicionsino")

def p_condicionno(p):
	'''condicionno : SINO I_LL lineacodigo D_LL '''
	print("condicionno")

def p_conectorlogico(p):
	'''conectorlogico : Y
			| O'''
	print("conectorlogico")

def p_tipocondicion(p):
	'''tipocondicion : LT
			| LTE
			| GT
			| GTE
			| IGUAL
			| DIF'''
	print("tipocondicion")

def p_tipoconector(p):
	'''tipoconector : conectorlogico
			| tipocondicion'''
	print("tipoconector")

def p_condicion(p):
	'''condicion : operando tipoconector operando
			| operando tipoconector operando tipoconector condicion
			| NEG operando tipoconector condicion
			| NEG operando
			| operando
			| operando tipoconector condicion'''
	print("condicion")

def p_incrementofor(p):
	'''incrementofor : cambiarvalor
			| incrementardisminuir'''
	print("incrementofor")

def p_iniciofor(p):
	'''iniciofor : VAR ID asignarvalor
			| ID asignarvalor'''
	print("iniciofor")

def p_ciclofor(p):
	'''ciclofor : PARA I_PAR iniciofor PUNTO_COMA condicion PUNTO_COMA incrementofor D_PAR I_LL lineacodigo D_LL
			| ID
			| ciclofor'''
	print("ciclofor")

def p_error(p):
	print ("Error de sintaxis ", p)
	global errorValue
	errorValue = p
	print("Illegal character '%s'" % p.value)
	#t.lexer.skip(1)
	print "Error en la linea "+str(p.lineno)

def error():
	global errorValue
	if errorValue is not None:
		print "ERROR"
		return str(('\ndescripcion del error: no se reconoce %s' % (errorValue.value)))
	else:
		return str(("\nCompilacion exitosa!\nErrores: 0"))

class AnalizadorSintactico(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.validar.clicked.connect(self.validar)	

    def validar(self):
		global errorValue
		cadena = self.ui.entrada.toPlainText()
		parser = yacc.yacc()
		parser.parse(cadena)
		self.ui.salida.setPlainText(error())
		print("Error values:", errorValue)
		errorValue = None


		

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = AnalizadorSintactico()
    window.show()
    sys.exit(app.exec_())