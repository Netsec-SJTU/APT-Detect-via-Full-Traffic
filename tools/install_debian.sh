sudo yum install -y automake libtool make gcc
sudo yum install -y flex bison

git clone https://github.com/VirusTotal/yara.git
cd yara
./build.sh
./configure --enable-cuckoo --enable-magic --enable-dotnet
make
sudo make install
