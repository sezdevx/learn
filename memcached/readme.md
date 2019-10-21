# How to install to ubuntu
```
# just make sure everything is fresh
sudo apt update
sudo apt upgrade

# install memcached
sudo apt install memcached

# edit the config file if necessary
sudo vim /etc/memcached.conf

sudo service memcached start
# or sudo systemctl start memcached

# install client tools
sudo apt install libmemcached-tools
# verify memcached service connection
```