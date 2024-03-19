# Install a Desktop Environment/GUI in Ubuntu Server

# step 1 Install the Desktop Environment
sudo apt update && apt upgrade -y
sudo apt install ubuntu-desktop
sudo apt install kde-plasma-desktop
sudo apt install ubuntu-mate-core
sudo apt install xubuntu-core

# step 2 Install and Set Up a Display Manager
sudo apt install lightdm
sudo systemctl start lightdm.service    # or sudo service ligthdm start
sudo reboot now


