sudo apt update && sudo apt upgrade

sudo apt install -y git python-pip python3-pip
sudo apt install -y htop

# yara
sudo apt install -y automake libtool make gcc
sudo apt install -y flex bison

git clone https://github.com/VirusTotal/yara.git
cd yara
./configure --enable-cuckoo --enable-magic --enable-dotnet
make
sudo make install

sudo pip install --upgrade pip
sudo pip install -U scikit-learn numpy scipy matplotlib
sudo pip install -U magic
sudo pip3 install --user numpy scipy
sudo pip3 install -U scikit-learn matplotlib

git clone https://github.com/faizann24/Fwaf-Machine-Learning-driven-Web-Application-Firewall
mv Fwaf-Machine-Learning-driven-Web-Application-Firewall Fwaf
git clone https://github.com/zoufutai/APT-Detect-via-Full-Traffic