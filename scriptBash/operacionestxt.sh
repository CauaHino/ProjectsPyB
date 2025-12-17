#!/bin/bash

clear

echo -e "Hola, gracias por entrar\n"

# Mostrar contenio de un archivo
cat archivo.txt

totalLineas=$(wc -l < archivo.txt)
echo -e "\nEl total de líneas es: $totalLineas"

# Leer un número de líneas concreto
read -p "Indica un número de línea: " linea
contenido=$(sed -n "$linea"'p' archivo.txt)
echo -e "\nEl contenido ed la linea $linea es: $contenido"

# Modificar una linea
read -p "Indica la linea que va a cambiar: " lineaMod
read -p "Indica el nuevo contenido de la linea $lineaMod: " nuevoContenido
sed -i "$lineaMod"'s/'"$contenido"'/'"$nuevoContenido"'/' archivo.txt
echo -e "La linea cambiada fue: $lineaMod"

read -p "Indica texto para añadir al final: " texto
echo "$texto" >> archivo.txt

echo -e " "

# Eliminar linea
read -p "Indica la linea que va a borrar: " lineaBorrar
sed -i "$lineaBorrar"'d' archivo.txt
cat archivo.txt

# Obtener coincidencias de busqueda
read -p "Indica la palabra a buscar: " palabra

grep -n "$palabra" archivo.txt

# Capturar el número de lineas donde aparece
linea=$(grep -n "$palabra" archivo.txt | cut -d':' -f1)