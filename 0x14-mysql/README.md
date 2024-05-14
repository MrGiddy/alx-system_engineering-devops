# 0x14. MySQL

![](./imgs/hbnb-architecture-mysql.png)

# Concepts
* [[How to : ] Fresh Reset and Install mysql 5.7](https://docs.google.com/document/d/1btVRofXP75Cj90_xq2x8AmzuMPOKq6D_Dt_SCDD6GrU/edit)
```
sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57
```

# Resources
* [What is a database](https://www.techtarget.com/searchdatamanagement/definition/database)
* [What is a database primary/replicate cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
* [MySQL primary/replicate setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
* [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)

**man or help**:
* ```mysqldump```

# Learning Objectives
## General
* What is the main role of a database
* What is a database replica
* What is the purpose of a database replica
* Why database backups need to be stored in different physical locations
* What operation should you regularly perform to make sure that your database backup strategy actually works

# Requirements
## General
* Allowed editors: ```vi```, ```vim```, ```emacs```
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A ```README.md``` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass ```Shellcheck``` (version ```0.3.7-5~ubuntu16.04.1 via apt-get```) without any error
* The first line of all your Bash scripts should be exactly ```#!/usr/bin/env bash```
* The second line of all your Bash scripts should be a comment explaining what is the script doing

# Tasks
## 0. Install MySQL

First things first, let’s get MySQL installed on **both** your web-01 and web-02 servers.
* MySQL distribution must be 5.7.x
* Make sure that ```task #3``` of your ```SSH project``` is completed for ```web-01``` and ```web-02```. The checker will connect to your servers to check MySQL status
* Please make sure you have your ```README.md``` pushed to GitHub.

Example:
```
ubuntu@229-web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
ubuntu@229-web-01:~$
```
