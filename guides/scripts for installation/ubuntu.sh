sudo apt update && sudo apt -y upgrade
sudo apt-get purge xrdp
sudo apt update
sudo apt install -y xrdp
sudo apt install -y xfce4
sudo apt install -y xfce4-goodies
sudo cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak
sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini
sudo sed -i 's/max_bpp=32/#max_bpp=32\nmax_bpp=128/g' /etc/xrdp/xrdp.ini
sudo sed -i 's/xserverbpp=24/#xserverbpp=24\nxserverbpp=128/g' /etc/xrdp/xrdp.ini
echo xfce4-session > ~/.xsession
sudo sed -i '/test -x/c "# xfce"' /etx/xrdp/strtwm.sh
sudo sed -i '/exec/c "startxfce4"' /etx/xrdp/strtwm.sh
sudo sed -i 's/exec/#/' /etx/xrdp/strtwm.sh
sudo passwd root
1234
1234
sudo /etc/init.d/xrdp start
sudo /etc/init.d/xrdp start