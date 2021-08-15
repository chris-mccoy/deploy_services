#!/bin/bash

. admin-openrc.sh

LATEST=$(find /share/bootstrap-vz-target -name 'kali-rolling-amd64-*' -type f -printf "%C@ %p\n" | sort -rn | awk '{ print $2 }' | head -n 1)
echo Found file $LATEST to add to Glance
glance image-create --progress --min-ram 2048 --min-disk 20 --visibility public --file $LATEST --name $(basename $LATEST) --container-format bare --disk-format raw

