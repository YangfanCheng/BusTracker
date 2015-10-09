


<?php
$input=$_GET["bus"];

$output= shell_exec('python bustracker.py ' . ((int)$input). ' 2>&1');
echo $output;
//$file="hello.txt";
//$fo=fopen($file, 'w');
//fwrite($fo,"hello");
//fclose($f);

//2>&1

?>