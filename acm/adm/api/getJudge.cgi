#!/bin/bash
echo "Content-type: text/html"
echo ""
N=`cat /acm/adm/etc/judgesmac|wc -l`
echo "N=$N"
