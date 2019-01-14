# Ubuntu

## Other Programs
* [tmux](tmux.md)

## Recipes
### [network_map.sh](network_map.sh)
* To view available hosts in a given network
* Using ping to check if a machine is up or down

### [ps_cpu_usage.sh](ps_cpu_usage.sh)
* To observe process cpu usage over a configured time

## Important Files
* `/etc/resolv.conf`
Where DNS servers are listed

* `/proc/partitions`
Where disk partitions are described

* `/etc/mtab`
Where mounted file systems are listed

* Log file locations
  - `/var/log/boot.log` : boot log info
  - `/var/log/httpd` : apache web server log
  - `/var/log/messages`: post boost kernel info
  - `/var/log/auth.log`, `/var/log/secure`: user authentication log
  - `/var/log/dmesg`: system boot up messages
  - `/var/log/mail.log`, `/var/log/maillog`: mail server log
  - `/var/log/Xorg.0.log`: X server log

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
# for inotifywait
sudo apt install inotify-tools
# for sqlite3
sudo apt-get install sqlite3 libsqlite3-dev
# for mysql
sudo apt-get install mysql-server
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
* `inotifywait`: to shows changes to files using inotify
* `logrotate`: to rotate the logs
* `fsck`: to check and repair a linux file system
* `hdparm`: get/set SATA/IDE device parameters
* `whereis`: location of the command, as well as the manual page
* `whatis`: one line description of the command
* `pgrep`: look up pid based on name
* `killall`: kill by process name
* `fdisk`: manipulates disk partition table
* `lswh`: list hardware
* `dmidecode`: DMI table decoder
* `crontab`: to view/modify crontab jobs
* `lsb_release`: to print distribution-specific information
* `useradd`: to add a new user
* `deluser`: to remove a user
* `chsh`: to change user shell
* `usermod`: to lock/unlock a user
* `chage`: modify password expiration
* `addgroup`: to add a new group
* `delgroup`: to delete a group
* `tcpdump`: to dump traffic on a network
* `ngrep`: to find a pattern to watch on network traffic
* `ip`: to show/change routing and network interfaces
* `strace`: to show system calls
* `ltrace`: similar to strace, but for user level library calls (for dynamically linked ones)
* `service`: to run and view init scripts
* `ss`: to investigate sockets
* `dstat`: to generate system usage stats
* `pidstat`: to report resource usage per process
* `sysctl`: change kernel parameters online
* `nice`: to run a program with modified scheduling priority
* `renice`: to change the priority of running processes
* `top`: display linux processes

## Command Examples
* top command displays real-time view of a running system
```bash
%Cpu(s):  5.0 us,  2.7 sy,  0.0 ni, 92.2 id,  0.0 wa,  0.2 hi,  0.0 si,  0.0 st
# us: user processes
# sy: kernel processes
# ni: niced user processes
# wa: waiting for IO completion
# hi: hardware interrupts
# si: software interrupts
# st: time stolen for this VM by the hypervisor
```

```bash
# PID: pid of the process
# USER: user name of the process
# PR: priority of the process
# NI: nice value of the process
# VIRT: virtual memory used by the process
# RES: physical memory used by the process
# SHR: shared memory
# S: status of the process
# %CPU: percentage of CPU
# %MEM: percentage of RAM
# TIME+: total time of activity of this process
# COMMAND: name of the process
```

* To display the ps tree
```bash
pstree
```

* To install X.509 security certificate trusted by browsers
```bash
# uses Let's Encrypt free certificate authority (letsencrypt.org)
wget https://dl.eff.org/certbot-auto
chmod a+x certbot-auto
./certbot-auto
```

* To install linux container (lxc)
```bash
# on ubuntu
apt-get install lxc1
# on debian
apt-get install lxc
# red-hat
yum install epel-release
yum install perl libvirt debootstrap
yum install lxc lxc-templates tunctl bridge-utils
```

* `lxc` commands
Priviliged containers are easier to create (created by root), because they don't require uid and gid
mapping.
```bash
lxc-create
lxc-ls
lxc-start
lxc-stop
lxc-attach
lxc-console
lxc-info
```

* To createa a privileged container. The easiest way is to download a
prebuilt distro in a privileged container.
```bash
lxc-create -n NAME -t TYPE
# if TYPE is download, then you can download a pre-built one from internet
```

* To change the priority of a running process
```bash
renice 11 PID_OF_PROCESS
```

* To change kernel parameters, you can edit `/etc/sysctl.conf`,
but it is better to test them with `sysctl` tool before editing the file
because you can ruin the kernel with bad values.
```bash
# list all parameters and their values
sysctl -a
# to list the value of a particular parameter
sysctl vm.swappiness
```

* To report various stats per process
```bash
# pidstat -d: IO
# pidstat -r: page faults and memory utilization
# pidstat -u: cpu utilization
# pidstat -w: task switches
```

* To get an idea about general system stats
```bash
dstat
# you can identify the top resource user
# -top-cpu: cpu usage
# -top-io: io usage (network io mostly)
# -top-bio: disk usage
# -top-mem: memory usage
# -top-latency: process with the highest latency
```

* To display the status of tcp sockets
```bash
ss -t
# to display sockets on listen mode
ss -l
# to display udp sockets on listen mode too
ss -ul
# then you can use lsof to investigate the processes using that port
# lsof -i :989
```


* To see the status of all services
```bash
service --status-all
```

* To stop mysql service
```bash
sudo service mysql stop
```

* To disable a service
```bash
sudo systemctl disable SERVICE_NAME
```

* Where to locate service
```bash
# /etc/init.d
# systemctl
# systemd suite
```

* To report routes
```bash
ip route
```

* To get the next hop to a particular ip address
```bash
ip route get 8.8.8.8
```

* To watch traffic on port 80 and report any packet that includes the string "Bash"
```bash
ngrep -q -c 64 Bash port 80
# -q is for printing headers and payload only
# -c is number of columns to use for payload data
```

* To analyze and capture packets with tcpdump
```bash
# capture only 50 packets, without -c it will capture untill killed
tcpdump -w /tmp/tcpdump.raw -c 50
# display packets for a given port (e.g. http)
tcpdump -r /tmp/tcpdump.raw port http
# to see the content too, in addition to headers
tcpdump -X -r /tmp/tcpdump.raw port http
```

* To list password related info for a user
```bash
chage -l userName
# a user can change his/her own settings
```

* To lock or unlock a user
```bash
# lock
usermod -L userName
# unlock
usermod -U userName
```

* To add a new user
```bash
useradd userName -p password -m
# -m to create the home directory too
```

* To change user shell
```bash
csh userName -s /bin/csh
```

* To delete a user
```bash
deluser userName --remove-all-files
```

* To display distribution specific info
```bash
lsb_release -a
```

* To extract detailed information on the hardware
```bash
sudo lswh
```

* To view crontab for the current user
```bash
crontab -l
```

* To remove crontab
```bash
crontab -r
```

* To check if cron is running
```bash
sudo systemctl status cron
```

* To dump SMBIOS (DMI) table contents
```bash
sudo dmidecode
```

* To display disk partitions
```bash
sudo fdisk -l
```

* You can use the following options with `-o` of ps
   * `pcpu`: percentage of CPU
   * `pid`: process id
   * `ppid`: parent process id
   * `pmem`: percentage of memory
   * `comm`: executable filename
   * `cmd`: simple command
   * `user`: user name
   * `nice`: priority
   * `time`: cumulative CPU time
   * `etime`: elapsed time since the process started
   * `tty`: associated tty device
   * `euid`: effective uid
   * `stat`: process state

* To get the pid of bash process ran by root
```bash
pgrep -u root bash
# to get the number of processes
pgrep -c bash
```

* To see the pid of a command
```bash
ps -C bash -o pid=
```

* To see the top 5 CPU consuming processes
```bash
ps -eo comm,pcpu --sort -pcpu | head -5
```

* To see threads
```bash
ps -Lf
```

* To get basic information about your device
```bash
hdparm -I /dev/sda1
# to test the disk performance
hdparm -t /dev/sda1
```

* To check all systems defined in `/etc/fstab`
```bash
fsck -A
# to automatically fix errors
fsck -a /dev/sda1
```

* To output changes to a directory
```bash
inotifywait -m -r -e create,move,open /path  -q
# -m to stay active and continous monitoring
# -r for recursive watch
# -e for list of events to watch
#    access,modify,attrib,move,create,open,close,delete
# -q for quiter messaging
```

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

* to highlight the differences in the output of watch
```bash
watch -d 'commands'
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

* To configure the syslogd so that it saves to a particular file (local0 to local7)
```bash
cat /etc/rsyslog.d/local7.config
# local7.* /var/log/local7
logger -p local7 "Message"
```

* To rotate logs and configure rotation
```bash
# /etc/logrotate.d
more dpkg
/var/log/dpkg.log {
        monthly
        rotate 12
        compress
        delaycompress
        missingok
        notifempty
        create 644 root root
}
```

  - `missingok`: ignores if the log file is missing
  - `notifempty`: only rotate if the log file is not empty
  - `size 30k`: limits the size of the log file
  - `compress`: compresses the older files with gzip
  - `weekly`: interval of rotations
  - `rotate 3`: number of old copies to keep
  - `create 644 root root`: mode, user and the group of the archived log files

* To detect failed login attempts
```bash
more /var/log/auth.log # or /var/log/secure.log
grep "Failed pass" /var/log/auth.log
```

* Important directories
```bash
# /bin: commands used by a regular user
# /boot: files required for the os startup
# /dev: device driver files
# /etc: config files and startup scripts
# /home: home folder of all users
# /lib: library files
# /media: external media, such as USB pen drive
# /opt: optional packages
# /proc: info about kernel and every process running
# /root: admin's home folder
# /sbin: admin commands
# /usr: secondary programs, libraries, and documentation
# /var: variable data, such as logs
# /sys: creates sys files
```

* Types of processes
```bash
# orphan: parent process is terminated
# zombie: child process is terminated, but parent
#         is sleeping or is suspended, child is zombie
# daemon: running in the background
```

* To list all processes including system processes
```bash
ps -ef
# those processes within [] are kernel threads
```