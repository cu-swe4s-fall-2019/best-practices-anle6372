conda install pycodestyle

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest


run style_style pycodestyle style.py
assert_no_stderr
assert_no_stdout


run get_col_stats_style pycodestyle get_column_stats.py
assert_no_stderr
assert_no_stdout

(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt


for j in `seq 1 5`;
  do
  count=0;
  total=0;
  sum1=0;

  for i in $( awk -v var="$j" '{print $var}' data.txt )
     do
       total=$(echo $total+$i | bc )
       ((count++))
     done
  mean=$(($total / $count));

  count=0;

  for i in $( awk -v var="$j" '{print $var}' data.txt )
     do
       diff=$(echo $mean-$i | bc )
       diffsq=$((diff * diff))
       sum1=$(echo $sum1+$diffsq | bc )
       ((count++))
      done
  pre=$(($sum1 / $count))
  stdev=$(bc <<< "scale=0; sqrt($pre)")

  run random_column_mean python get_column_stats.py --file_name data.txt --column_number $(($j-1))
  assert_in_stdout $mean
  echo STDERR
  assert_no_stderr

  run random_column_stdev python get_column_stats.py --file_name data.txt --column_number $(($j-1))
  assert_in_stdout $stdev
  assert_no_stderr
  done


V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data1.txt

for j in `seq 1 5`;
  do
  count=0;
  total=0;
  sum1=0;

  for i in $( awk -v var="$j" '{print $var}' data1.txt )
     do
       total=$(echo $total+$i | bc )
       ((count++))
     done
  mean=$(($total / $count));

  count=0;

  for i in $( awk -v var="$j" '{print $var}' data1.txt )
     do
       diff=$(echo $mean-$i | bc )
       diffsq=$((diff * diff))
       sum1=$(echo $sum1+$diffsq | bc )
       ((count++))
      done
  pre=$(($sum1 / $count))
  stdev=$(bc <<< "scale=0; sqrt($pre)")

  run ones_column_mean python get_column_stats.py --file_name data1.txt --column_number $(($j-1))
  assert_in_stdout $mean
  assert_no_stderr

  run ones_column_stdev python get_column_stats.py --file_name data1.txt --column_number $(($j-1))
  assert_in_stdout $stdev
  assert_no_stderr
  done


V=1
(for i in `seq 1 100`; do
    echo -e "$V\t$V\t$V\t$V\tA";
done )> data2.txt

for j in `seq 1 5`;
  do
  run letter_column_mean python get_column_stats.py --file_name data2.txt --column_number $(($j-1))
  assert_in_stdout "File was not able to be read"
  assert_exit_code 1

  run letter_column_stdev python get_column_stats.py --file_name data2.txt --column_number $(($j-1))
  assert_in_stdout "File was not able to be read"
  assert_exit_code 1
  done



V=1
(for i in `seq 1 100`; do
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data3.txt

  for i in $( awk -v var="$j" '{print $var}' data1.txt )
     do
       total=$(echo $total+$i | bc )
       ((count++))
     done
  mean=$(($total / $count));

  count=0;

  for i in $( awk -v var="$j" '{print $var}' data1.txt )
     do
       diff=$(echo $mean-$i | bc )
       diffsq=$((diff * diff))
       sum1=$(echo $sum1+$diffsq | bc )
       ((count++))
      done
  pre=$(($sum1 / $count))
  stdev=$(bc <<< "scale=0; sqrt($pre)")

  run letter_col_number python get_column_stats.py --file_name data3.txt --column_number A
  assert_in_stdout "Column number could not be read"
  assert_exit_code 1

  run no_file python get_column_stats.py --file_name --column_number 1
  assert_in_stderr "usage:"
  assert_exit_code 2

  run no_col_number python get_column_stats.py get_column_stats.py --file_name data.txt --column_number
  assert_in_stderr "usage:"
  assert_exit_code 2

for j in `seq 1 5`;
  do
  count=0;
  total=0;
  sum1=0;

  for i in $( awk -v var="$j" '{print $var}' data3.txt )
     do
       total=$(echo $total+$i | bc )
       ((count++))
     done
  mean=$(($total / $count));

  count=0;

  for i in $( awk -v var="$j" '{print $var}' data3.txt )
     do
       diff=$(echo $mean-$i | bc )
       diffsq=$((diff * diff))
       sum1=$(echo $sum1+$diffsq | bc )
       ((count++))
      done
  pre=$(($sum1 / $count))
  stdev=$(bc <<< "scale=0; sqrt($pre)")

 run switched_data python get_column_stats.py --column_number 1 --file_name data3.txt
  assert_in_stdout $mean
  assert_in_stdout $stdev
  assert_no_stderr
 done