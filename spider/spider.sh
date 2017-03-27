#!/bin/bash

sed -i '/^$/d' 'todofile'

while [[ -s 'todofile' ]] ; do 
	ret=$(python spider.py 2>&1)
	echo $ret
done

#sort -u fof > fof
