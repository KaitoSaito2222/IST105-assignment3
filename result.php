<?php
    $x = escapeShellarg($_POST["x"]);
    $y = escapeShellarg($_POST["y"]);
    $z = escapeShellarg($_POST["z"]);
    
    $command = escapeshellcmd("python3 process_input.py $x $y $z");
    $output = shell_exec($command);
    
    if ($output) {
        echo $output;
    } else {
        echo "Error executing Python script";
    }
?>