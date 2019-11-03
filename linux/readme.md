# Ubuntu

## Other Programs
* [tmux](tmux.md)

## Package manager
```
# install a new package
sudo apt install {package-name}
# remove a package with config files
sudo apt remove --purge {package-name}
# remove a package without config files
sudo apt remove {package-name}
# clear apt cache located at /var/cache/apt/archives
sudo apt clean
sudo apt-get clean
# delete only useless packages from /var/cache/apt/archives
sudo apt autoclean
sudo apt-get autoclean
# update the server with the latest
sudo apt update && sudo apt upgrade
# list the upgradable packages
sudo apt list --upgradable
# to upgrade a specific package
sudo apt upgrade {package-name}
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
# for gtags
sudo apt-get install global
# for bash
sudo apt install bash-completion
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
* `pkill`: kill a process with process name
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
* `htop`: ncurses based top
* `lscpu`: display cpu info
* `lshw`: display hardware info
* `dmesg`: print or control the kernel ring buffer
* `host`: DNS lookup utility
* `dig`: DNS lookup utility
* `logger`: enters messages into the system log
* `nohup`: run a command immune to hangups, with output to a non-tty
* `lsb_release`: print distribution specific information
* `do-release-upgrade`: upgrade the os to the latest release
* `ufw`: ubuntu firewall (for managing netfilter firewall)
* `strings`: print strings of printable characters in a given file
* `runlevel`: print previous and current sysv runlevel

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
# list all kernel parameters
sudo sysctl -a
# to list the value of a particular parameter
sysctl vm.swappiness
```

* To update `/etc/sysctl.conf` changes
```
# after editing and saving changes
sudo sysctl -p
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
sudo service --status-all
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

* To dump SMBIOS (DMI) table contents (Find BIOS version)
```bash
sudo dmidecode
sudo dmidecode -s bios-version
sudo dmidecode -s bios-release-date
sudo dmidecode -s system-product-name
sudo dmidecode -s system-manufacturer
sudo dmidecode --type bios
# show all info about system
sudo dmidecode -t SYSTEM
# all info about bios
sudo dmidecode -t BIOS
# all info about baseboard
sudo dmidecode -t BASEBOARD
sudo dmidecode -t Processor

# full list of strings
bios-vendor
bios-version
bios-release-date
system-manufacturer
system-product-name
system-version
system-serial-number
system-uuid
baseboard-manufacturer
baseboard-product-name
baseboard-version
baseboard-serial-number
baseboard-asset-tag
chassis-manufacturer
chassis-type
chassis-version
chassis-asset-tag
processor-family
processor-manufacturer
processor-version
processor-frequency

# list of DMI types
0 BIOS
1 System
2 Baseboard
3 Chassis
4 Processor
5 Memory Controller
6 Memory Module
7 Cache
8 Port Connector
9 System Slots
10 On Board Devices
11 OEM Strings
12 System Configuration Options
13 BIOS Language
14 Group Associations
15 System Event Log
16 Physical Memory Array
17 Memory Device
18 32-bit Memory Error
19 Memory Array Mapped Address
20 Memory Device Mapped Address
21 Built-in Pointing Device
22 Portable Battery
23 System Reset
24 Hardware Security
25 System Power Controls
26 Voltage Probe
27 Cooling Device
28 Temperature Probe
29 Electrical Current Probe
30 Out-of-band Remote Access
31 Boot Integrity Services
32 System Boot
33 64-bit Memory Error
34 Management Device
35 Management Device Component
36 Management Device Threshold Data
37 Memory Channel
38 IPMI Device
39 Power Supply
40 Additional Information
41 Onboard Device Extended Information
42 Management Controller Host Interface
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
# alternative
ps -C commandName
# alternative
pgrep -x commandName
```

* Check if a process is running
```bash
pgrep -x mysqld >/dev/null && echo "Mysql is running" || echo "Mysql is NOT running"
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
dig test.com
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

* To list cpu info
```bash
sudo lscpu
sudo lshw -c cpu
cat /proc/cpuinfo:
nproc --all: show number of processing units available
getconf _NPROCESSORS_ONLN: get the number of CPUs/cores
```

* To check if Linux is 32 or 64 bits on AMD CPUs that can run
both versions
```bash
getconf LONG_BIT
```

* To list Linux kernel parameters
```bash
cat /proc/cmdline
dmesg | grep "Command line"
```

* Bash completion
```bash
cat /etc/profile.d/bash_completion.sh
```

* Search packages
```bash
apt-cache search dns dig
```

* Upgrade a specific package that is already installed
```bash
sudo apt-get --only-upgrade install {package-name}
```

* Setup SSH public key authentication
```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# generate keys
# ssh-keygen or
ssh-keygen -t rsa 4096 -C "Key for remote servers"
# ed25519 is better
ssh-keygen -t ed25519 -C "Key for remote servers"

# to install
# for rsa
ssh-copy-id -i $HOME/.ssh/id_rsa.pub user@remote-server
# for ed25519 KEY
ssh-copy-id -i $HOME/.ssh/id_ed25519.pub user@remote-server

# to test the setup
ssh user@remote-server

# to disable the passphrase/password
eval $(ssh-agent)
ssh-add
ssh user@remote-server
```

* To switch to root
```bash
sudo -i
```

* To backup files
```bash
rsync -avr ~/.ssh user@remote-server:/path/to/encrypted/partition
```

* To change the host name
```bash
sudo hostnamectl set-hostname NEW_HOST_NAME
sudo vi /etc/hosts
sudo reboot
```

* To find your public or private IP
```bash
ip a
ip a s eth0
```

* To log a message to system log
```bash
logger "This is my message"
tail -f /var/log/syslog
```

* To print distribution specific information
```bash
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.3 LTS
Release:        18.04
Codename:       bionic
```

* To upgrade ubuntu to the latest release
```bash
sudo do-release-upgrade
# in case do-release-upgrade not found
sudo apt install ubuntu-release-upgrader-core
```

* htop options
```
htop -C: no color
htop --pid=pid1,pid2,pid3: info about specific processes given by their id
htop -u username: processes of a given user
```

* To check if you are running systemd or upstart init
```bash
sudo strings /sbin/init | grep -i systemd
sudo strings /sbin/init | grep -i upstart
```

* To check the classic init daemon config file
```bash
# most latest linux distros do not use this anymore
cat /etc/inittab
```

* To find the current run level
```bash
runlevel

# to immediately go to a particular runlevel
init 0
init 3
```

* Where are the scripts that start and stop services for a given run level
```bash
cd /etc/rc.d/rc[0|1|2|3|4|...].d
# any file that starts with S is for starting a service
# any file that starts with K is for killing a service
# any number between K, S and the service name controls the order of starting
# processes
# all the files under rc#.d directories are symbolic links to script files
# located under /etc/rc.d/init.d directory which starts and kills services
```

* List of systemd unit types
```
automount
device
mount
path
service
snapshot
socket
target
```

* To list systemd units
```bash
systemctl list-units
```

* Location of systemd unit config files. The config files specify what other services must be started,
when this service can be started etc...
```bash
cd /lib/systemd/system
cd /etc/systemd/system
# list config file names of service unit type
systemctl list-unit-files --type=service
# enabled: the unit is enabled currently
# disabled: the unit is disabled currently
# static: statically enabled, can not be disabled even by root  
```

* The basic service unit config file has the following options
```
Description: Free form description
After: Which units should be started before this service
Environment File: The service's config file
ExecStart: Command used to start this service
ExecReload: Command used to reload this service
WnatedBy: The target unit this service belongs to 
```

* The basic target unit config file has the following options
```
Description: Free form description
Requires: If this target unit is activated, so is the requires target unit
Conflicts: Avoids conflicts in services, starting this target unit stops the listed targets and services
After: Which units should be activated before this unit
AllowIsolate: If set to yes, then this unit is activated along with its dependencies and all others are deactivated
ExecStart: Commands that starts the service
ExecReload: Command used to reload this service
Alias: systemd creates a symbolic link from the target unit names listed to this unit
```

* Systemv backward compatibility unit config files
```
runlevel0.target
runlevel1.target
runlevel2.target (sybollically linked to multi-user.target)
runlevel3.target (sybollically linked to multi-user.target)
runlevel4.target (sybollically linked to multi-user.target)
runlevel5.target 
```

* Check out what the default.target links to 
```bash
ls -l /lib/systemd/system/default.target
```

* To list units that a target unit will activate
```bash
# can't see all the output
systemctl show --property "Wants" multi-user.target
# better output
systemctl show --property "Wants" multi-user.target | fmt -10 | sed 's/Wants=//g' | sort
# with requires (which is more stringent than wants)
systemctl show --property "Requires" multi-user.target | fmt -10 | sed 's/Wants=//g' | sort
```

* To see how getty.target is linked to multi-user.target
```bash
systemctl show --property "WantedBy" getty.target
```

* For SysVinit systems, check the list of services and their runlevels
```bash
chkconfig --list
```

* For SysVinit systems, check all running services
```bash
service --status-all | grep running... | sort
```

* To see an individual service's status
```bash
service cups status
systemctl status cups.service
```

* To see the status of all services
```bash
service --status-all
```

* To start, stop services with systemd
```bash
service cups stop
systemctl status cups.service
service cups start
systemctl start cups.service
service cups restart
systemctl restart cups.service
# the following is a conditional restart, restarts a service if it is currently running
systemctl condrestart cups.service
service cups reload # only config files are reloaded
systemctl reload cups.service
```

* To start, stop service with Upstart
```bash
initctl stop cups
initctl start cups
initctl restart cups
initctl reload cups
```

* To make a service persistent in SysVInit
```bash
chkconfig --level 3 cups on
chkconfig --list cups
ls /etc/rc.d/rc3.d/S*cups
# to make it persistent on more than one level
chkconfig --level 2345 cups on
```

* To make a service persistent in upstart
```bash
# edit /etc/init/service.conf file
# search for start line
# e.g. start on filesystem or runlevel [2345]
```

* To make a service persistent in systemd
```bash
systemctl enable cups.service
systemctl status cups.service
# to disable it
systemctl disable cups.service
systemctl status cups.service
```

* To prevent anyone from ever running a service in systemd
```bash
systemctl mask NetworkManager.service
# to enable running it again
systemctl unmask NetworkManager.service
```

* Configuring SysVinit default runlevel
```bash
# edit /etc/inittab
# current default runlevel is runlevel 5
id:5:initdefault: 
```

* Configuring Upstart default runlevel
```bash
# edit /etc/init/rc-sysinit.conf
# find DEFAULT_RUNLEVEL= and edit it
```

* Configuring systemd default runlevel
```bash
# link /lib/systemd/system/default.target to the desired runlevel's file
# but main options are multi-user.target which is same as runlevel2.target, runlevel3.target, and runlevel4.target
# other option is graphical.target which is same as runlevel5.target
ln -sf /lib/systemd/system/runlevel3.target /etc/systemd/system/default.target
```

* Get list of files installed for a package on ubuntu
```bash
dpkg-query -L {package-name}
```

* To get the list of users on a machine
```bash
cut -d: -f1 /etc/passwd
```

* To get a user's info from passwd database
```bash
getent passwd userName
```

* To kill all processes by name
```bash
killall -9 emacs
```

* To exclude files while copying files remotely
```bash
rsync -av -e ssh --exclude='*.sh' /source/path/ user@remoteHost:/dest/path/
# -a : recursive into directories
# -v : verbose output
# -e ssh : use ssh
# --exclude : exclude the given files
```

* To exclude files from scp
```bash
scp !(*.sh) userName@remoteHost:/dest/path
```

* To execute bash aliases on ssh
```bash
ssh -t user@host /bin/bash -ic 'alias_name'
# -t: force pseudo-terminal allocation, can be used to execute arbitrary
# screen based programs on a remote host
# -i: make bash interactive
# -c: commands are read from the first non-option argument command string
```