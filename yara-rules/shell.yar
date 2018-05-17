rule WebShell
{
    strings:
<<<<<<< HEAD
        $reg1 = "<?php" wide nocase
    condition:
        any of them
        //all of them
=======
        $reg1 = "<?php" nocase
    condition:
        any of them
>>>>>>> 06aa5b8dd90849e435f1ef951ead1c284ffb2fba
}

