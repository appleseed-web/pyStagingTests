#!/bin/bash

baseurl="$1"
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )



cd $parent_path/spider

rm ./donefile
touch ./donefile
echo $baseurl > ./todofile
./spider.sh



cd $parent_path/pageSpeedTest
rm $parent_path/pageSpeedTest/out
$parent_path/pageSpeedTest/testWebsites.sh > $parent_path/pageSpeedTest/out


cd $parent_path/w3cTest
rm $parent_path/w3cTest/out
$parent_path/w3cTest/testWebsites.sh > $parent_path/w3cTest/out


cd $parent_path/altTest
rm $parent_path/altTest/out
$parent_path/altTest/testWebsites.sh > $parent_path/altTest/out




cd $parent_path

cp spider/fof fourOhFour.txt
rm spider/fof
echo "" > report.txt
echo "" >> report.txt
echo "PAGESPEED TEST" >> report.txt
echo "" >> report.txt
echo "" >> report.txt
cat pageSpeedTest/out  >> report.txt

echo "" >> report.txt
echo "" >> report.txt
echo "W3C TEST" >> report.txt
echo "" >> report.txt
echo "" >> report.txt
cat w3cTest/out  >> report.txt


echo "" >> report.txt
echo "" >> report.txt
echo "MISSING ALT TEST" >> report.txt
echo "" >> report.txt
echo "" >> report.txt
cat altTest/out  >> report.txt
