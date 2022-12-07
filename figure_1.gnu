set term png
set output "figure_1.png"
set terminal png size 512,512

file = "data_1.dat"

set size square 

set xrange [0.5:L+0.5]
set yrange [0.5:L+0.5]

unset xtics
unset ytics
unset border

plot file u 2:($3 ==-1 ? $1 : 1/0) with points pt 5 ps 70/L lc rgb "sandybrown" notitle,\
     file u 2:($3 == 1 ? $1 : 1/0) with points pt 5 ps 70/L lc rgb "royalblue" notitle