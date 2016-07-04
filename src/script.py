#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# Atributos
grado = ''
curso = 0
semestre = 0
turno = ''
grupo = ''
dia = ''
hora_inicio = 0
hora_fin = 0
asignatura = ''
salir = 0

print ""
print " ---------------------------------------------------------- "
print "|   Bienvenido al Programa de Introduccion de Horarios     |"
print " ---------------------------------------------------------- "
print ""

open("salidaTemp.txt",'w').close()
open("salida.json",'w').close()

temp = open("salidaTemp.txt",'r+')
out = open("salida.json",'w')

while salir == 0:

	print " ---------------------------------------------------------- "
	print "|               Situacion Actual del Sistema               |"
	print " ---------------------------------------------------------- "
	print ""
	print "\tGrado: " + str(grado)
	print "\tCurso: " + str(curso)
	print "\tSemestre: " + str(semestre)
	print "\tTurno: " + str(turno)
	print "\tGrupo: " + str(grupo)
	print "\tDia: " + str(dia)
	print ""
	print " ---------------------------------------------------------- "
	print "|                Elija una Accion a Realizar               |"
	print " ---------------------------------------------------------- "
	print "|        1: Cambiar Grado        2: Cambiar Curso          |"
	print "|        3: Cambiar Semestre     4: Cambiar Turno          |"
	print "|        5: Cambiar Grupo        6: Cambiar Dia            |"
	print "|        7: Introducir Horario   0: Salir                  |"	
	print " ---------------------------------------------------------- "
	print ""
	print "Escriba una opcion: "

	accion = int(input())

	if accion == 0:

		print ""
		print " ---------------------------------------------------------- "
		print "|                Generamos el Fichero JSON                 |"
		print " ---------------------------------------------------------- "
		print ""

		out.write("{ \"horarios\":[\n");

		temp.seek(0, os.SEEK_SET)
		linea = temp.readline()

		while linea:

			linea = linea.replace("horario(", "")
			linea = linea.replace(")", "")
			lista = linea.split(',')

			out.write("\t{ ")
			out.write("\"grado\":\"" + str(grado) + "\", ")
			out.write("\"curso\":" + str(curso) + ", ")
			out.write("\"semestre\":" + str(semestre) + ", ")
			out.write("\"turno\":\"" + str(turno) + "\", ")
			out.write("\"grupo\":\"" + str(grupo) + "\", ")
			out.write("\"dia\":\"" + str(dia) + "\", ")
			out.write("\"hora_inicio\":" + str(hora_inicio) + ", ")
			out.write("\"hora_fin\":" + str(hora_fin) + ", ")
			out.write("\"asignatura\":\"" + str(asignatura) + "\"")
			out.write("},\n")

			linea = temp.readline()

		out.seek(-2, os.SEEK_END)
		out.write("\n] }\n");

		temp.close()
		out.close()

		salir = 1

		print " ---------------------------------------------------------- "
		print "|                   Fin de la Ejercucion                   |"
		print " ---------------------------------------------------------- "
		print ""
	if accion == 1:
		print "Escriba el grado, Formato: 'grado'"
		grado = str(input())
		print ""
	if accion == 2:
		print "Escriba el curso, Formato: curso"
		curso = int(input())
		print ""
	if accion == 3:
		print "Escriba el semestre, Formato: curso"
		semestre = int(input())
		print ""
	if accion == 4:
		print "Escriba el turno, Formato: 'turno'"
		turno = str(input())
		print ""
	if accion == 5:
		print "Escriba el grupo, Formato: 'grupo'"
		grupo = str(input())
		print ""
	if accion == 6:
		print "Escriba el dia, Formato: 'dia'"
		dia = str(input())
		print ""
	if accion == 7:
		print "Escriba la hora de comienzo, Formato: hora_inicio"
		hora_inicio = str(input())
		print "Escriba la hora de finalizacion, Formato: hora_fin"
		hora_fin = str(input())
		print "Escriba la asignatura, Formato: 'asignatura'"
		asignatura = str(input())
		print ""
		aux = "horario(" + str(grado) + "," + str(curso) + "," + str(semestre) + ","
		aux += str(turno) + "," + str(grupo) + "," + str(dia) + ","
		aux += str(hora_inicio) + "," + str(hora_fin) + "," + str(asignatura) + ")"
		print "Se va a guardar este horario:\n" + aux
		print ""
		print "¿Es correcto?: 0: Si o 1: No"
		accion = int(input())
		if accion == 0:
			temp.write(aux + "\n")
		else:
			1+1
	else: 
		1+1