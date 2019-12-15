#! python
# -*- coding:utf-8 -*-
import os
import zipfile
opcion=-1
registro=[]
f=open("registro.log","w")
import getpass 
#Establecemos un valor inicial de opción diferente de 5 para que inicie el bucle
#Hacemos definiciones de funciones, que usaremos más tarde
def leertamano():
	size=int(input("\nIntroduzca dicho tamaño en bytes: "))
	return size
def escogeopcion():
	try:
		opcion=-1
		while opcion<1 or opcion>5:
			opcion=int(input("Selecciona una opción del 1-5, no se cerrará el programa hasta que se escoja la opción 5: "))
	except:
		print("Escoja entre uno y cinco")
	return opcion
#Establecemos un try, dentro del cual colocaremos el bucle por si se da una excepción
try:		
	#Establecemos un bucle para que, si no se selecciona la opción de salir, el usuario pueda usar varias opciones
	while opcion!=5:
		#Mostramos el menú en pantalla
		print("\n 1.Mostrar archivos superiores en tamaño a uno especificado\n\n","2.Borrar archivos superiores en tamaño a uno especificado\n\n","3.Comprimir un fichero o carpeta especificados\n\n","4.Borrar los archivos temporales del navegador\n\n", "5.Salir del programa\n")
		#Pedimos al usuario que introduzca la opción que desea
		opcion=escogeopcion()
		if opcion==1:
			size=leertamano() #Pedimos al usuario que introduzca el tamaño deseado en bytes
			listfiles1=os.listdir(".")
			for file in listfiles1:
				filesize=int(os.stat(file).st_size)
				if filesize>=size:
					print(file)
					registro.append("Se ha mostrado con éxito "+file+"\n")
			#Comparando el tamaño pedido con una lista de todos los archivos y directorios de la carpeta, le decimos al ordenador que muestre en pantalla los nombres de los deseados
			
		if opcion==2:
			size2=leertamano()
			listfiles2=os.listdir(".")
			for file in listfiles2:
				filesize2=int(os.stat(file).st_size)
				if filesize2>=size2:
					os.remove(file)
					print("Se ha borrado con éxito el archivo "+file)
					registro.append("Se ha borrado con éxito "+file+"\n")
			#Comparando el tamaño pedido con una lista de todos los archivos y directorios de la carpeta, le decimos al ordenador que borre los deseados
		
		if opcion==3:
			archivo=input("\nIntroduzca el nombre del fichero o carpeta a comprimir: ")
			listfiles3=os.listdir(".")
			for file in listfiles3:
				if archivo==file:
					compressedfile = "comprimido.zip"
					comprimido = zipfile.ZipFile (compressedfile, "w", zipfile.ZIP_DEFLATED)
					comprimido.write (archivo)
					comprimido.close()
					registro.append("Se ha comprimido con éxito "+archivo+"\n")
					print("\nSe ha comprimido con éxito")
			#Comparando el nombre pedido con una lista de todos los archivos y directorios de la carpeta, le decimos al ordenador que comprima el deseado
		if opcion==4:
			#Le pedimos al usuario confirmación para iniciar la acción
			confirmacion=0
			while confirmacion!=1:
				confirmacion=int(input("\nCierre el navegador antes de utilizar esta opción, cuando esté preparado escriba 1: " ))
			#Le pedimos al ordenador el usuario para generar una ruta
			user=getpass.getuser()
			a="C:\\Users\\"
			b="\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache"
			#Borramos la caché de Google
			if confirmacion==1:
				try:
					#Ensamblamos la ruta del directorio en el que trabajaremos y entramos en ella
					os.chdir(a+user+b)
					chromelist=os.listdir(".")
					for file in chromelist:
						os.remove(file)
					print("\n¡Se ha borrado la caché con éxito!")
					registro.append("Se ha borrado la caché con éxito"+"\n")
				except:
					print("\nNo se ha podido borrar la caché porque el navegador sigue abierto")
except:
	print("\nError 404 not found") #Cuando se de una excepción en cualquier elemento dentro del try, se le avisará al usuario con un mensaje
for accion in registro:
	f.write(accion)
f.close()