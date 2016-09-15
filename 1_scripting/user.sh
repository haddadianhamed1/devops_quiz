#!/bin/bash
number=$(users | tr ' ' '\n' | sort -u | wc -l)
echo $number

dc=10
dw=5

while [[ $# -gt 1 ]]
do
key="$1"

case $key in
        -c)
          case "$2" in
            "") critical=10 ; shift 2 ;;
            *) critical=$2 ; shift 2;;
          esac ;;
        -w)
          case "$2" in
            "") warning = 5; shift 2 ;;
            *) warning=$2 ;shift 2 ;;
          esac;;
esac
shift
done
echo "-c was trigered , parameter $critical"
echo $number
echo $critical
if [ $number -ge $critical ]
then
        echo " we are critical"
        exit 2
elif [ $number -ge $warning ] && [ $number -lt $critical ]
then
        echo " we are wrning"
        exit 1
elif [ $number -lt $warning ]
then
        echo " we are ok"
        exit 0
else
        echo "unkown"
        exit 3
fi
