#!/bin/bash

clear
echo -e "\n🍺🍻 MANIPULAR ARCHIVOS JSON\n"

# Obtener una propriedad del JSON
nombre=$(jq -r '.nombre' ../producto.json)
precio=$(jq -r '.precio' ../producto.json)

echo -e "\n\nEl nombre que buscas es $nombre"
echo -e "El precio que buscas es: $precio€\n\n"

# Cambia el valor de un json
read -p "Dime el nuevo nombre: " nuevoNombre
jq --arg n "$nuevoNombre" '.nombre = $n' ../producto.json > ../tmp.json && mv ../tmp.json ../producto.json

read -p "Dime el nuevo precio: " nuevoPrecio
jq --arg p "$nuevoPrecio" '.precio = $p' ../producto.json > ../tmp.json && mv ../tmp.json ../producto.json