#!/usr/bin/python

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
#print "|             CopyRight: Daniel Melero Chaves              |"
print " ---------------------------------------------------------- "
print ""

#nb = input('Choose a number: ')
#number = int(nb)

temp = open("salidaTemp.txt")
out = open("salida.json","w")

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
	#print "\tHora de Inicio: " + hora_inicio
	#print "\tHora de Fin: " + hora_fin
	#print "\tAsignatura: " + asignatura
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
	print "Escriba una Opcion: "

	accion = int(input())

	if accion == 0:
		print ""
		print " ---------------------------------------------------------- "
		print "|                Generamos el Fichero JSON                 |"
		print " ---------------------------------------------------------- "
		print ""

		out.write("{ \"horarios\":[\n");

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

		salir = 1

		print " ---------------------------------------------------------- "
		print "|                   Fin de la Ejercucion                   |"
		print " ---------------------------------------------------------- "
		print ""
	if accion == 1:
		print "Escriba el Nuevo Grado, Formato: 'grado'"
		grado = str(input())
		print ""
	if accion == 2:
		print "Escriba el Nuevo Curso, Formato: curso"
		curso = int(input())
		print ""
	if accion == 3:
		print "Escriba el Nuevo Semestre, Formato: curso"
		semestre = int(input())
		print ""
	if accion == 4:
		print "Escriba el Nuevo Turno, Formato: 'turno'"
		turno = str(input())
		print ""
	if accion == 5:
		print "Escriba el Nuevo Grupo, Formato: 'grupo'"
		grupo = str(input())
		print ""
	if accion == 6:
		print "Escriba el Nuevo Dia, Formato: 'dia'"
		dia = str(input())
		print ""
	if accion == 7:
		print "Escriba el Nuevo Dia, Formato: 'dia'"
		dia = str(input())
		print ""
	else: 
		1+1

temp.close()
out.close()