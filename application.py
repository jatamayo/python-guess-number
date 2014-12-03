#-*- coding: utf-8 -*-
import random
print u"BIENVENIDO AL JUEGO DE ADIVINANZA"
print u"El juego consiste en adivinar un número oculto en el rango del 0 al 20"
print u"las condiciones son:"
print u"1) Tiene 5 vidas para adivinar el número oculto"
print u"2) El valor ingresado debe de ser un número"
#generacion de numero aleatorio random.ranint
oculto=random.randint(0,20)
intentos= 0
vidas =5
# while permite que el usuario realize la operacin 5 veces
while intentos <5:
    print ""
    print "Tienes %s vidas"%(vidas)
    numero=raw_input(u"Ingrese el numero a adivinar")
    try:    
        numero.isdigit() ==True
        numero=int(numero)
        if numero == oculto:
            print "Gano"
            break
        elif numero < oculto:
            print u"El número ingresado es menor"
        elif numero > oculto:
            print u"El número ingresado es mayor"
	if vidas==1:
	    print ""
	    print u"Se terminarón tus vidas"
	else:
	    print ""
    except:
        print u"lo siento no es número"
    intentos = intentos +1
    vidas=vidas-1

