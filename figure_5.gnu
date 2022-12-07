set term png
set output "figure_5.png"
set terminal png size 512,512

set key outside spacing 1.5
set key width 1
set key center top
set key horizontal

set logscale x
set format x "10^{%T}"
set xrange[1:1e4]
set xtics 1,1e2,1e4

set yrange [0:1]

set xlabel "t"
set ylabel "<|M|>"

plot "data_4.dat" u 1:2 with lines lw 2 lc rgb "red" title "FSMC",\
     "data_5.dat" u 1:2 with lines lw 2 lc rgb "dark-red" title "CTMC"
