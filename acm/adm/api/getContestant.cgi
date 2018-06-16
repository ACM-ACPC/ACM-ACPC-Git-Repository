#!/bin/bash
echo "Content-type: text/html"
echo ""
N=`cat /acm/adm/etc/contestantmac|wc -l`
echo "N=$N"
