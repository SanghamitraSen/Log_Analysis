# Log_Analysis
Udacity's Log Analysis Database Project
## Project Description
The database contains newspaper articles, as well as the web server log for a site. The log has a database row for each time a reader loaded a web page. Using that information, the code will answer the following questions about the site's user activity:
 * What are the most popular three articles of all time?
 * Who are the most popular article authors of all time?
 * On which days did more than 1% of requests lead to errors?
## Pre-Requisites
  * **Python 3** should be installed. 
    You can get it from:https://www.python.org/downloads/
  * **A terminal like Git Bash.**
    If you don't already have Git installed, download Git from git-scm.com.
  * **VirtualBox.**
    You can download it from https://www.virtualbox.org/wiki/Download_Old_Builds_5_1. Make sure to choose October 2017 version       so         that it is compatible with vagrant.
  * **Vagrant.**
    You can download it from https://www.vagrantup.com/downloads.html
## Steps to execute the project
  * Clone this project in your desktop.
  * Create a new folder and cd into it through git bash.
  * Start the virtual machine using command:**vagrant up**
  * Once done,login using **vagrant ssh** and then type **cd /vagrant**
  * Manually add the newslog.py file from the repository you cloned and the newsdata.sql file into vagrant directory.
  * To execute the queries run this command: **python3 newslog.py**
  
*Note:The output.txt file shows how the output came when I executed.*
