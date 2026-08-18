<?php
function reverse_string($string) {
    $reversed = "";

    for ($i = strlen($string) - 1; $i >= 0; $i--) {
        $reversed .= $string[$i];
    }

    return $reversed;
}

echo reverse_string("Hello, World!");