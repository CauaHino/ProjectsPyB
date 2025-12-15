#!/bin/bash

ruta=$1
categoria=$2
clear
read -p "Indica la categoria que quieres modificar: "
read -p "Indica el nuevo nombre de la categoria: " nombre
mv $ruta/$categoria "$ruta/$nombre"
if [[ $? == 1 ]]; then
  echo "No fue posible actualizar la categoria"
  exit 10
fi
clear
echo "Categoria actualizada para $nombre"
exit 0