#!/bin/bash

#Папка, в которую копируем
BACKUP_DIR="/tmp"

# Запускаем бекап
xtrabackup --backup --target-dir=$BACKUP_DIR
