#!/bin/bash

echo "Старт создание фейковых сетей : Количество - $1, Название - $2"

num=0

while [ "$num" -lt "$1" ]; do

    sudo iw dev "$3" interface add mon"$num" type monitor
    (( num++ ))

done
