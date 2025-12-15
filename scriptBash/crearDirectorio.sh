#!/bin/bash

ruta=$1


echo -e "\n RUTA: $ruta"

clear
read -p "Indica el nombre para la categoria: " nombre
mkdir "$ruta/$nombre"
if [[ $? == 1 ]]; then
  exit 10
fi
clear
echo "Has credo la categoria $nombre"
exit 0

