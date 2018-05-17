rule WebShell
{
    strings:
        $reg1 = "<?php" nocase
    condition:
        any of them
}

