#!/bin/bash
./tmp/process.awk $1

gnuplot -persist <<-EOFMarker
    set terminal png size 600,300
    set datafile separator "$"
    set yrange [-1:11]
    f(x) = m*x + b
    fit f(x) '$1' using 6:(sum[col=7:8] column(col)) via m,b
    set output 'fit.png'
    plot '$1' using 6:(sum[col=7:8] column(col)) title "number of closest people on board by passenger age" with points, f(x) title 'fit'
EOFMarker
