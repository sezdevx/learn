* To start/stop mysql server in ubuntu
```
sudo service mysql start
sudo service mysql stop
```

* To reset mysql root password (e.g. you forgot the password)
```
sudo service mysql stop
sudo mysqld_safe --skip-grant-tables &
# or edit /etc/mysql/mysql.conf.d/mysqld.cnf and
# add skip-grant-tables under [mysqld]
mysql -u root
```

```sql
use mysql;

update user set authentication_string=PASSWORD("myNewPassword") where User='root';
update user set plugin="mysql_native_password" where User='root';

flush privileges;
quit;```

```bash
sudo /etc/init.d/mysql stop
sudo service mysql start
```