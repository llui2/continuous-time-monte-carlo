set term png
set output "figure_4.png"
set terminal png size 512,512

set key outside spacing 1.5
set key width 1
set key center top
set key horiz

set title "CTMC"

set logscale x
set format x "10^{%T}"
set xrange[1:1e4]
set xtics 1,1e2,1e4

set yrange [-1-0.25:1+0.25]

set xlabel "t"
set ylabel "M"

set style line 1 lc rgb 'red' lw 2
set style line 2 lc rgb 'blue' lw 2
set style line 3 lc rgb 'dark-spring-green' lw 2
set style line 4 lc rgb 'web-blue' lw 2
set style line 5 lc rgb 'dark-violet' lw 2
set style line 6 lc rgb 'coral' lw 2
set style line 7 lc rgb 'seagreen' lw 2
set style line 8 lc rgb 'gray' lw 2
set style line 9 lc rgb 'bisque' lw 2
set style line 10 lc rgb 'pink' lw 2

plot for [j=0:9] "data_3.dat" index j u 1:2 with lines ls j+1 notitle