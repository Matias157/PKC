#!/bin/bash

certname=$1


###
### For cert8 (legacy - DBM)
###

for certDB in $(find ~/ -name "cert8.db")
do
    certdir=$(dirname ${certDB});
    echo "${certdir}"
    certutil -d dbm:${certdir} -D -n ${certname}
done


###
### For cert9 (SQL)
###

for certDB in $(find ~/ -name "cert9.db")
do
    certdir=$(dirname ${certDB});
    echo "${certdir}"
    certutil -d sql:${certdir} -D -n ${certname}
done