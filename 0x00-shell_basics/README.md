# 0x00. Shell, Basics

# Write a script which if executed will:

### task 0-current_working_directory
* Print the absolute path name of current working directory

### task 1-listit
* Display the content list of current working directory

### task 2-bring_me_home
* Change the working directory to the user's home directory

### task 3-listfiles
* Display current directory contents in long format

### task 4-listmorefiles
* Display current directory contents, including hidden files in long format

### task 5-listfilesdigitonly
* Display current directory contents in
	- Long format
	- Numeric user and group ID's
	- Hidden files (starting with .)

### task 6-firstdirectory
* Create a directory named my_first_directory inside /tmp/ directory

### task 7-movethatfile
* Move file "betty" from /tmp/ to /tmp/my_first_directory

### task 8-firstdelete
* Delete "betty" from /tmp/my_first_directory

### task 9-firstdirdeletion
* Delete directory my_first_directory in /tmp directory

### task 10-back
* Change working directory to previous one

### task 11-lists
* List all files, including hidden ones in long format in
	- Current directory
	- Parent of working directory
	- /boot directory

### task 12-file_type
* Print the file type of file named "iamafile" in /tmp directory

### task 13-symbolic_link
* Create a symbolic link to /bin/ls named __ls__ in the current working directory

### task 14-copy_html
* Copy all HTML files from current working directory to parent of the working directory, but only copy files that do not exist in the parent of the working directory or are newer than the versions in the parent of the working directory

### task 15: 100-lets_move
* Move all files beginning with an uppercase letter to the directory /tmp/u

### task 16: 101-clean_emacs
* Delete all files ending with ~ in the current working directory

### task 17: 102-tree
* Create directories welcome/, welcome/to/ and welcome/to/scool in the current directory. Use only two spaces(and lines) in the script

### task 18: 103-commas
* List all files and directories of the current directory separated by commas
	- Directory names should end swith slash (/)
	- Hidden files and directories should be listed
	- Listing should be alpha ordered, except for directories . and .. which are listed at the beginning
	- Only digits and letters are used to sort: Digits should come first
	- The listing should end with a new line

### task 19: school.mgc
* Create a magic file "school.mgc" that can be used with the command "file" to detect data files of file "school". School data files always contain the string SCHOOL at offset 0.
