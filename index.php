<html>
   <head>
      <title>MegaSensor</title>      
   </head>
   
   <body>
      <h1>MegaSensors Reading</h1>
<?php
$myfile = fopen("read", "r") or die("Unable to open file!");
$readings= fread($myfile,filesize("read"));
fclose($myfile);
$readings=substr("$readings", 1,-1);
$readings=explode(",", $readings);
if ($readings[3]=="1") {
	$readings[3]="Magnetic Field Detected";
} else {
	$readings[3]="NO Magnetic Field Detected";

}
if ($readings[4]=="1") {
	$readings[4]="Motion Detected";
} else {
	$readings[4]="NO Motion Detected";

}
echo "<p>";
echo "Joystick axis x      : $readings[0]<br>";
echo "Joystick axis y      : $readings[1]<br>";
echo "Light intensity      : $readings[2]<br>";
echo "Magnetic Field Sensor: $readings[3]<br>";
echo "Motion Sensor        : $readings[4]<br>";
echo "Ultrasonic Sensor    : $readings[5]cm<br>";
echo "<p/>";
      ?> 
   </body>
</html>