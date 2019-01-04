# Ubuntu

## Other Programs
* [tmux](tmux.md)


## Packages needed
```bash
sudo apt-get update
sudo apt-get install emacs25
sudo apt-get install git
sudo apt-get install python
sudo apt-get install xdg-utils
sudo apt-get install curl
sudo apt-get install unzip
sudo apt install python-pip
```

## Packages nice to have
```bash
sudo apt-get install g++
sudo apt install npm
sudo apt-get install tmux
# for netstat
sudo apt install net-tools
# if you want an openssh server running locally
sudo apt install openssh-server
# to measure network performance
sudo apt install iperf
```

## Install Apps
* [Chrome](https://askubuntu.com/questions/510056/how-to-install-google-chrome)
* [Intellij IDEA](https://www.jetbrains.com/idea/download/#section=linux)

# Commands
* `watch`: to execute a program periodically and show its output fullscreen
* `tmux`: run multiple terminals at the same time, switch between them easily
* `pidof`: find the process id(s) of the given program
* `paste`: merge multiple lines into a single file
* `netstat`: print network connections, routing tables, interface stats, multicast memberships
* `lsof`: list open files
* `systemctl`: to start/stop services
* `iperf`: to measure network performance
* `nc`: to create TCP and UDP connections and servers
* `last`: to show a listing of last logged in users
* `lastb`: to show a listing of failed logged in users

## Command Examples
* To communicate with nc
```bash
# create the server on port 12345
nc -l 12345
# now create a client to that server
nc localhost 12345
# type something and the server will receive that command as you type
```

* To copy file quickly using nc
```bash
# remote server
nc -l 12345 > copy.file
# local machine
nc REMOTE_SERVER 12345 < local.file
```

* To view a listing of last logged in users
```bash
last
```

* To view a list of failed login attempts
```bash
sudo lastb
```

* To measure network performance
```bash
# start the server
iperf -s
# on the client run iperf
iperf -c <ip_address_of_server>
# to also find the maximum transfer size (MTU)
iperf -mc <ip_address_of_server>
```



* To list opened ports and services
```bash
netstat -tnp
```

* To list open network connections
```bash
lsof -i
```

* To list open files
```bash
lsof
```

* To setup openssh server
```bash
sudo apt update
sudo apt install -y openssh-server
sudo systemctl status ssh.service
# to change the settings
sudo emacs /etc/ssh/sshd_config
# after changes you need to restart to apply the changes
sudo systemctl restart ssh.service
# to remove the openssh-server
sudo systemctl stop ssh.service
sudo apt-get purge openssh-server
```

* To make a file immutable
```bash
chattr +i file.path
```

* To create and mount a loopback file system
```bash
dd if=/dev/zero of=loopback.img bs=1G count=1
mkfs.ext4 loopback.img
sudo mkdir /mnt/loopback
sudo mount -o loop loopback.img /mnt/loopback
# when done
sudo umount /mnt/loopback
```

* To create an iso image from a directory
```bash
mkisofs -V "Label" -o image.iso source_dir/
sudo mkdir /mnt/image
sudo mount -o loop image.so /mnt/image
# when done
sudo umount /mnt/image
```


* to list all available services
```bash
service --status-all
systemctl -l --type service --all
systemctl -r --type service --all
/etc/init.d
```

* merge multiple lines into a single line
```bash
# 3 lines into a single line
cat ../data/population.csv | cut -d ',' -f1,2,3 | paste - - -
# 2 lines into a single line
cat ../data/population.csv | cut -d ',' -f1,2,3 | paste - -
```

* watch command can be a life saver
```bash
# see the top 5 processes every 4 seconds
watch -n 4 "ps aux | sort -nrk 3,3 | head -n 5"
```

* pidof by default displays one or more pids of a given program
```bash
pidof commandName
# to display just one pid
pidof -s commandName
```

* Tell tail to die when a process dies
```bash
PID=$(pidof httpd)
tail -f log.file --pid $PID
```

* To see version info
```bash
cat /etc/*-release
more /proc/version
uname -a
```

* To set the ip address of an interface
```bash
ifconfig wlan0 192.168.0.70
# to set the subnet mask too
ifconfig wlan0 192.168.0.70 netmask 255.255.252.0
# to get a new one from the dhcp server
dhclient wlan0
```

* Where DNS info is located
```bash
cat /etc/resolv.conf
# to add new servers edit the file or
sudo echo nameserver <IP_ADDRESS> >> /etc/resolv.conf
```

* To list the ip addresses of a domain
```bash
host test.com
nslookup test.com
```

* To add a symbolic name to a given IP address
```bash
# /etc/hosts
127.0.0.1  localhost
```

* To display routing table information
```bash
route
```

* To add a default gateway
```bash
route add default gw IP_ADDRESS INTERFACE_NAME
```

* To send a single packet in ping
```bash
ping www.test.com -c 1
```

* To see path to a host and see response time
```bash
mtr www.test.com
```

## Recipes
### [network_map.sh](network_map.sh)
* To view available hosts in a given network
* Using ping to check if a machine is up or down

### [ps_cpu_usage.sh](ps_cpu_usage.sh)
* To observe process cpu usage over a configured time

## Important Files
* `/etc/resolv.conf`
Where DNS servers are listed

* `/etc/mtab`
Where mounted file systems are listed
