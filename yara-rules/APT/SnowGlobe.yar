rule SnowGlobe : APT
{
    meta:
        ref1 = "https://www.welivesecurity.com/2015/06/30/dino-spying-malware-analyzed/"
        ref2 = "https://securelist.com/blog/research/69114/animals-in-the-apt-farm/"
    strings:
        $file = "SYSTEMROOT\svchost00000000-0000-0000-0000-0000-00000000.dat" nocase wide
        $file = "PROFILE_PATH\All Users\update.msi" nocase wide
        $file = "PROFILE_PATH\All Users\Application Data\update.msi" nocase wide
        $file = "$(ProgramData)\MSI\update.msi" nocase wide
        $file = "PROGRAM_FILES\Common Files\wusvcd.exe" nocase wide
        $file = "PROGRAM_FILES\Common Files\wusvcd\wusvcd.exe" nocase wide
        $directory = "SYSPATH\Microsoft\Windows Management Infrastructure" nocase wide
        $directory = "SYSTEMROOT\Microsoft\ Windows Management Infrastructure" nocase wide
        $service = "WinMI32" nocase wide
        $reg = "Software\Microsoft\WinMI" nocase wide
        $file = "SYSTEMROOT\..\ Documents and Settings\ *\Application Data\Microsoft\wmimgnt.dll" nocase wide
        $file = "SYSTEMROOT\..\ Documents and Settings\ *\Application Data\Microsoft\wmimgnt.exe" nocase wide
    condition:
        all of them
}
