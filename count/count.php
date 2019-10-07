<?php
require_once("./conf.php");
$filename = $FILE;

$count = file_get_contents($filename);
$count = intval($count);
$count++;
file_put_contents($filename, $count);

$len = strlen($count);
header("Content-Type: image/png");
$img = @imagecreate($len * 7, 10);
$bg = imagecolorallocate($img, 255, 255, 255);
$txt = imagecolorallocate($img, 0, 0, 0);
imagestring($img, 2, 2, -2, $count, $txt);
imagepng($img);
imagedestroy($img);
