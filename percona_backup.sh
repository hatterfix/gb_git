#!/bin/bash

#Папка, в которую копируем
BACKUP_DIR="/path/to/backup/directory"

xtrabackup --backup --target-dir=$BACKUP_DIR
