pycodestyle style.py

pycodestyle get_column_stats.py

(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

python get_column_stats.py --file_name data.txt --column_number 2


V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py --file_name data.txt --column_number 2


V=1
(for i in `seq 1 100`; do
    echo -e "$V\t$V\t$V\t$V\tA";
done )> data.txt

python get_column_stats.py --file_name data.txt --column_number 2

V=1
(for i in `seq 1 100`; do
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py --file_name data.txt --column_number A

python get_column_stats.py --file_name --column_number 1

python get_column_stats.py --file_name data.txt --column_number

python get_column_stats.py --column_number 1 --file_name data.txt