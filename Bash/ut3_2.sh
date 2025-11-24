
# Función para crear la estructura de directorios
crear(){
	clear
	echo -e "CREAR ESTRUCTURA\n"
	# Nos movemos al inicio del directorio con ruta absoluta
	cd /home/dam78/sistemas/linux/ejercicios
	mkdir ut3_2
	cd ut3_2
	mkdir VEHICULOS BARCOS
	mkdir -p /home/dam78/sistemas/linux/ejercicios/ut3_2/VEHICULOS/2RUEDAS/BICI
	mkdir -p /home/dam78/sistemas/linux/ejercicios/ut3_2/VEHICULOS/2RUEDAS/MOTO
	mkdir -p /home/dam78/sistemas/linux/ejercicios/ut3_2/VEHICULOS/4RUEDAS/COCHE
	mkdir -p /home/dam78/sistemas/linux/ejercicios/ut3_2/VEHICULOS/4RUEDAS/FURGONETA
	mkdir -p /home/dam78/sistemas/linux/ejercicios/ut3_2/BARCOS/LANCHA
	mkdir -p /home/dam78/sistemas/linux/ejercicios/ut3_2/BARCOS/VELEROS
	mkdir -p /home/dam78/sistemas/linux/ejercicios/ut3_2/BARCOS/YATES
}



#!/bin/bash
clear
echo -e "Hola\n"

read -p "Indica tu nombre: " nombre
echo -e "\nHola $nombre\n"

while [[ true  ]]; do
	read -p "¿Deseas ejecutar el programa? [y/n]" respuesta

	if [[ $respuesta == "y" ]]; then
		echo -e "\nHas Pulsado YES"
		crear
		break
	elif [[ $respuesta == "n" ]]; then
		echo -e "\nHas Pulsado NO"
		break
	else
		echo -e "\nNo has pulsado una opción correcta\n"
		read -n1 -p "Pulsa una tecla para continuar"

	fi
done
clear
echo -e "GRACIAS POR USAR NUESTRA APLICACIÓN"
