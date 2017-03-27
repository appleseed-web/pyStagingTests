#/bin/bash


echo "Starting TESTING"
echo ""
echo ""

file="../spider/donefile"

while read p; do
	python testWebsite.py $p
done < $file
