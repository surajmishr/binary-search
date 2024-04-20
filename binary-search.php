<?php

// Binary search function
function binarySearch($arr, $target) {
    $low = 0;
    $high = count($arr) - 1;

    while ($low <= $high) {
        $mid = $low + floor(($high - $low) / 2); // Calculate the midpoint

        if ($arr[$mid] == $target) {
            return $mid; // Target found, return its index
        } elseif ($arr[$mid] < $target) {
            $low = $mid + 1; // Target is in the right half
        } else {
            $high = $mid - 1; // Target is in the left half
        }
    }

    return -1; // Target not found
}

// Example usage:
$arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20];
$target = 12;
$index = binarySearch($arr, $target);
if ($index != -1) {
    echo "Target $target found at index $index\n";
} else {
    echo "Target $target not found in the array\n";
}
?>
