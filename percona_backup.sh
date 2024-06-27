#!/bin/bash

BACKUP_DIR="/path/to/backup/directory"

xtrabackup --backup --target-dir=$BACKUP_DIR
