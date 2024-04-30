
# https://docs.jumpserver.org/zh/v3/installation/setup_linux_standalone/requirements/#1
apt-get update
apt-get install -y wget curl tar gettext iptables

cd /opt

# download  --  https://github.com/jumpserver/installer/releases/
wget -c https://github.com/jumpserver/installer/releases/download/v3.10.7/jumpserver-installer-v3.10.7.tar.gz
tar -xzf jumpserver-installer-v3.10.7.tar.gz
cd jumpserver-installer-v3.10.7
./jmsctl.sh install

# start jumpserver:
cd jumpserver-offline-release-v3.10.7-amd64
./jmsctl.sh start

# возможно надо будет поменять конфиг, описание здесь - https://docs.jumpserver.org/zh/v3/guide/env/ :
cat /opt/jumpserver/config/config.txt
--> DOMAINS: your_ip:port

./jmsctl.sh restart

----------------------------------------------------------
# commands:
./jmsctl.sh stop
./jmsctl.sh restart
./jmsctl.sh backup
./jmsctl.sh upgrade
For more commands, you can enter ./jmsctl.sh --help to understand

# После успешной установки войдите в JumpServer через браузер
admin
admin

# Обновление - https://docs.jumpserver.org/zh/v3/installation/setup_linux_standalone/offline_upgrade/
