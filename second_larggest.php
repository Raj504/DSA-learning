<?php

function second_largest($s) {
    $digits = [];

    for($i=0; $i<strlen($s); $i++){
        if(is_numeric($s[$i])){
            $digits[] = (int)$s[$i];
        }
    }

    $digits = array_values(array_unique($digits));

    if(count($digits) < 2){
        return -1; 
    }

    if($digits[0] > $digits[1]) {
        $first = $digits[0];
        $second = $digits[1];
    } else{
        $first = $digits[1];
        $second = $digits[0];
    }

    for($i=2; $i<count($digits); $i++){
        if ($digits[$i] > $first) {
            $second = $first;       
            $first  = $digits[$i];  
        } elseif ($digits[$i] > $second) {
            $second = $digits[$i];  
        }
    }
    return $second;

}

$s = "dfa12321afd";
echo second_largest($s);