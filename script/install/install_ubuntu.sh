sudo apt update && sudo apt upgrade

sudo apt install -y git python-pip python3-pip
sudo apt install -y htop
sudo pip install -U pip setuptools

# cuckoo
sudo apt-get install python python-pip python-dev libffi-dev libssl-dev
sudo apt-get install python-virtualenv python-setuptools
sudo apt-get install libjpeg-dev zlib1g-dev swig
sudo apt-get install tcpdump apparmor-utils
sudo apt-get install swig
sudo aa-disable /usr/sbin/tcpdump

virtualenv venv
. venv/bin/activate
pip install -U pip setuptools
pip install -U cuckoo

# yara
sudo apt install -y automake libtool make gcc
sudo apt install -y flex bison

git clone https://github.com/VirusTotal/yara.git
cd yara
./configure --enable-cuckoo --enable-magic --enable-dotnet
make
sudo make install

sudo pip install -U scikit-learn numpy scipy matplotlib
sudo pip install -U magic pandas
sudo pip3 install --user numpy scipy
sudo pip3 install -U scikit-learn matplotlib pandas

git clone https://github.com/faizann24/Fwaf-Machine-Learning-driven-Web-Application-Firewall
mv Fwaf-Machine-Learning-driven-Web-Application-Firewall Fwaf
git clone https://github.com/zoufutai/APT-Detect-via-Full-Traffic

# site

sudo pip install -U pymysql
