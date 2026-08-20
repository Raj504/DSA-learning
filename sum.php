<?php
    function add_two_number($a, $b){
        $add = $a + $b;
        return $add;
    }

    $num1 = (int)readline("Enter first number: ");
    $num2 = (int)readline("Enter second number: ");
    $result = add_two_number($num1, $num2);
    echo "The sum is: " . $result;