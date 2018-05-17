rule WebShell
{
    strings:
        $reg1 = "<?php" wide nocase
    condition:
        any of them
        //all of them
}

