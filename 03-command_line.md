# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

ls #list directories and files under a given path
mkdir #create new directory
pwd #print working directory
cd #change directory
rm #delete files or empty directory
rmdir #delete directory
mv #move files or directory to different directory or use it to change file name
cp #copy files
cat #output file content to terminal
> filename #redirect standard output to a file

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

ls #list files and directories without details, does not list hidden files
ls -a #list all files and directories including hidden files
ls -l #list all contents in a directory in long form (have details about files and directories)
ls -lh #show conetents in long form and sizes in human readable format
ls -lah #show all contents including hidden files in long form and with sizes in human readable format
ls -t #order files and directories by the time they were last modified
ls -Glp #I don't know what G option does, but when I tried it, it seems to list content name in different color
---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

ls -c #display files by file timestamp
ls -d #display only directories
ls -t #display newest files first
ls -u #display files by file access time
ls -l #display files in long format listing

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs #read items from the standard input, delimited by blanks, and executes the command
example: batch delete files
find /tmp -name core -type f -prnt | xargs /bin/rm -f


 

