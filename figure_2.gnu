set term png
set output "figure_2.png"
set terminal png size 512,512

set key outside spacing 1.5
set key width 1
set key center top
set key horiz

set xlabel "t"
set ylabel "M"

set logscale x
set format x "10^{%T}"
set xrange[1:1e4]
set xtics 1,1e2,1e4

set yrange [-1-0.25:1+0.25]

plot "data_2.dat" i 3 u 1:2 with lines lw 2 lc rgb "red" title "FSMC",\
     "data_3.dat" i 5 u 1:2 with lines lw 2 lc rgb "dark-red" title "CTMC"
