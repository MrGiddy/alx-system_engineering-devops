# 0x04. Loops, conditions and parsing

# Resources
**Read or watch**:

* [Loops sample](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
* [Variable assignment and arithmetic](https://tldp.org/LDP/abs/html/ops.html)
* [Comparison operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
* [File test operators](https://tldp.org/LDP/abs/html/fto.html)
* [Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)

**man or help**:
* ```env```
* ```cut```
* ```for```
* ```while```
* ```until```
* ```if```

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General
* How to create SSH keys
* What is the advantage of using ```#!/usr/bin/env bash``` over ```#!/bin/bash```
* How to use ```while```, ```until``` and ```for``` loops
* How to use ```if```, ```else```, ```elif``` and ```case``` condition statements
* How to use the ```cut``` command
* What are files and other comparison operators, and how to use them

# More Info
Shellcheck
Shellcheck is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. Shellcheck is your friend! All your Bash scripts must pass Shellcheck without any error or you will not get any points on the task.

```Shellcheck``` is available on the school’s computers. If you want to use it on your own computer, here is how to [install](https://github.com/koalaman/shellcheck#installing) it.

For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code SC2034, you can browse [https://github.com/koalaman/shellcheck/wiki/SC2034](https://github.com/koalaman/shellcheck/wiki/SC2034).

# Tasks

## 0. Create a SSH RSA key pair

Read for this task:

* [Linux and Mac OS users](https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys)
* [Windows users](https://docs.rackspace.com/docs/generating-rsa-keys-with-ssh-puttygen)
man: ```ssh-keygen```

You will soon have to manage your own servers concept page hosted on remote [data centers](https://www.youtube.com/watch?v=iuqXFC_qIvA&feature=youtu.be&t=46). We need to set them up with your RSA public key so that you can access them via SSH.

Create a RSA key pair.

Requirements:

* Share your **public key** in your answer file ```0-RSA_public_key.pub```
* Fill the ```SSH public key``` field of your intranet profile with the public key you just generated
* **Keep the private key to yourself in a secure location**, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
* If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase

SSH and RSA keys will be covered in depth in a later project.

## 1. For Best School loop
Write a Bash script that displays ```Best School``` 10 times.

Requirement:

* You must use the ```for``` loop (```while``` and ```until``` are forbidden)
```
sylvain@ubuntu$ head -n 2 1-for_best_school 
#!/usr/bin/env bash
# This script is displaying "Best School" 10 times
sylvain@ubuntu$ ./1-for_best_school 
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
```

## 2. While Best School loop
Write a Bash script that displays ```Best School``` 10 times.

Requirements:
* You must use the ```while``` loop (for and ```until``` are forbidden)
```
sylvain@ubuntu$ ./2-while_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
```
