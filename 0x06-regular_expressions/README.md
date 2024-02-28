# 0x06. Regular expression

# Background Context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

# Resources
**Read or watch**:

* [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
* [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
* [Rubular is your best friend](https://rubular.com/)
* [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
* [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)

# Requirements
## General
* Allowed editors: ```vi```, ```vim```, ```emacs```
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A ```README.md``` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* The first line of all your Bash scripts should be exactly ```#!/usr/bin/env ruby```
* All your regex must be built for the Oniguruma library

# Tasks
## 0. Simply matching School

* The regular expression must match ```School```
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:
```
sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```

## 1. Repetition Token #0
* Find the regular expression that will:
    * mkip:  hbn
    * mkip:  hbtn
    * match: hbttn
    * match: hbtttn
    * match: hbttttn
    * skip:  hbtttttn

* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## 2. Repetition Token #1
* Find the regular expression that will:
    * match: htn
    * match: hbtn
    * skip:  hbbtn
    * skip:  hbbbtn

* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## 3. Repetition Token #2
Find the regular expression that will:
    * skip:  hbn
    * match: hbtn
    * match: hbttn
    * match: hbtttn
    * match: hbttttn

Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## 4. Repetition Token #3
* Find the regular expression that will:
    * match: hbn
    * skip:  hbon
    * match: hbtn
    * match: hbttn
    * match: hbtttn
    * match: hbttttn

* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching meth
od

## 5. Not quite HBTN yet
* The regular expression must be exactly matching a string that starts with ```h``` ends with ```n``` and can have any single character in between
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:
```
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$
```
