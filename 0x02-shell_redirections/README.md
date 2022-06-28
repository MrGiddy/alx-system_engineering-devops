# 0x02. Shell, I/O Redirections and filters

### task 0-hello_world
Write a script that prints "Hello, World", followed by a new line to the standard output.

### task 1-confused_smiley
Write a script that displays a confused smiley "(Ôo)'.

### task 2-hellofile
Display the content of the /etc/passwd file.

### task 3-twofiles
Display the content of /etc/passwd and /etc/hosts

### task 4-lastlines
Display the last 10 lines of /etc/passwd

### task 5-firstlines
Display the first 10 lines of /etc/passwd

### task 6-third_line
Write a script that displays the third line of the file iacta.

	- The file iacta will be in the working directory

	- You’re not allowed to use sed

### task 7-file
Write a shell script that creates a file named exactly _\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)_(everything between the underscres) containing the text Best School ending by a new line.

### task 8-cwd_state
Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

### task 9-duplicate_last_line
Write a script that duplicates the last line of the file iacta
	- The file iacta will be in the working directory

### task 10-no_more_js
Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.

### task 11-directories
Write a script that counts the number of directories and sub-directories in the current directory.
	- The current and parent directories should not be taken into account
	- Hidden directories should be counted

### task 12-newest_files 
Create a script that displays the 10 newest files in the current directory.

Requirements:
	- One file p`er line
	- Sorted from the newest to the oldest

### task 13-unique
Create a script that takes a list of words as input and prints only words that appear exactly once.
	- Input format: One line, one word
	- Output format: One line, one word
	- Words should be sorted

### task 14-findthatword
Display lines containing the pattern “root” from the file /etc/passwd

### task 16-countthatword
Display the number of lines that contain the pattern “bin” in the file /etc/passwd

### task 17-whatsnext
Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.

### task 18-letteronly
Display all lines of the file /etc/ssh/sshd_config starting with a letter.
	- include capital letters as wel

### task 19-AZ
Replace all characters A and c from input to Z and e respectively.

### task 20-hiago
Create a script that removes all letters c and C from input.

### task 21-reverse
Write a script that reverse its input.

### task 22-users_and_homes
Write a script that displays all users and their home directories, sorted by users.
	- Based on the the /etc/passwd file

### task 23: 100-empty_casks
Write a command that finds all empty files and directories in the current directory and all sub-directories.
Only the names of the files and directories should be displayed (not the entire path)
	- Hidden files should be listed
	- One file name per line
	- The listing should end with a new line
	- You are not allowed to use basename, grep, egrep, fgrep or rgrep

### task 24: 101-gif
Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.
	- Hidden files should be listed
	- Only regular files (not directories) should be listed
The names of the files should be displayed without their extensions
	- The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
	- One file name per line
	- The listing should end with a new line
	- You are not allowed to use basename, grep, egrep, fgrep or rgrep
