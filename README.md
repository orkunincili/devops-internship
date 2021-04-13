# Kod Gemisi Internship 2021



**1.** Installation Jira and Bitbucket for Ubuntu 20.04<br>
**2.** Changing base urls<br>
**3.** Possible problems<br>
3a. **Error:** Unsupported database<br>
3b. **Mistake:** If we carelessly delete the database(like me)<br>
**4.** Script<br>




## Installation Jira and Bitbucket for Ubuntu 20.04

I used [this](https://confluence.atlassian.com/adminjiraserver/installing-jira-applications-on-linux-938846841.html) documentation for Jira installation.

For Bitbucket I used [this](https://confluence.atlassian.com/bitbucketserver/install-bitbucket-server-on-linux-868976991.html) documentation for Bitbucket
installation.

## Changing base urls

I changed base urls while I set up Jira and Bitbucket but both of them gave me the error that base urls don't match.

### For Jira:

**1)** To the command line for stop Jira:
````
    sudo /etc/init.d/jira stop
````

**2)** Open the configuration file.
````
    [Jira_INSTALLATION]/conf/server.xml
````
(for me server.xml is in **/opt/atlassian/jira/conf/**)

**3)** Open the server.xml and edit **<Context>** like this.
    
````
    <Context path="/JIRA" docBase="${catalina.home}/atlassian-jira" reloadable="false" useHttpOnly="true">
````
**4)** Save and exit.

I get help from [here](https://confluence.atlassian.com/adminjiraserver/configuring-the-base-url-938847830.html).

### For Bitbucket:

**1)** To the command line for stop Bitbucket:
````
    <installation directory>/bin/stop-jira.sh
````
My installation directory is **/home/orkun/temp/atlassian-bitbucket-7.11.2/**

**2)** Go to **bitbucket.properties** and open it.
(If only Bitbucket version 5.0 or later.More info [here](https://confluence.atlassian.com/kb/proxying-atlassian-server-applications-with-apache-http-server-mod_proxy_http-806032611.html) and [here](https://confluence.atlassian.com/bitbucketserver/change-bitbucket-s-context-path-776640153.html))
````
    <bitbucket-home-directory>/shared/bitbucket.properties
````
for me it's **/home/orkun/bitbucket-home/shared/**


**3)** Add this line:
````
    server.context-path=/Bitbucket
````

**4)** Save and exit.

## Possible problems:

### Error: Unsupported Postgresql version:

I had PostgreSQL version 12.6 on my computer. After installation finished I learned
PostgreSQL 12 is not supported. Unfortunately,downgrading [PostgreSQL is not supported](https://dba.stackexchange.com/questions/224991/downgrading-postgresql-10-to-9-4).

I removed PostgreSQL in my computer get help from [here](https://askubuntu.com/questions/32730/how-to-remove-postgres-from-my-installation).Then I reinstalled supported PostgresSQL version(9.6). Then create a new database.

But then I faced new problem. I could not connect to Jira and Bitbucket.

### For Jira
I must edited **db.config.xml** because my old database information still there. I became a root user and opened the dbconfig.xml.This file is in the **Jira home directory**.
````
   /var/atlassian/application-data/jira
````
and then I have arranged the places I marked with **X** according to the new database and user.
````
<?xml version="1.0" encoding="UTF-8"?>

<jira-database-config>
<name>defaultDS</name>
<delegator-name>default</delegator-name>
<database-type>postgres72</database-type>
<schema-name>public</schema-name>
<jdbc-datasource>
 <url>jdbc:postgresql://localhost:5432/XXXX</url>-------here
 <driver-class>org.postgresql.Driver</driver-class>
 <username>XXXX</username>------------------------------here
 <password>XXXX</password>------------------------------here
 <pool-min-size>20</pool-min-size>
 <pool-max-size>20</pool-max-size>
 <pool-max-wait>30000</pool-max-wait>
 <validation-query>select 1</validation-query>
 <min-evictable-idle-time-millis>60000</min-evictable-idle-time-millis>
 <time-between-eviction-runs-millis>300000</time-between-eviction-runs-millis>
 <pool-max-idle>20</pool-max-idle>
 <pool-remove-abandoned>true</pool-remove-abandoned>
 <pool-remove-abandoned-timeout>300</pool-remove-abandoned-timeout>
 <pool-test-on-borrow>false</pool-test-on-borrow>
 <pool-test-while-idle>true</pool-test-while-idle>
</jdbc-datasource>
</jira-database-config>

````
Then I restarted the Jira.

### For Bitbucket

In **<bitbucket-home-directory>/shared/bitbucket.properties**,
I changed the places marked with **X** with the new database username and password.
````
jdbc.driver=org.postgresql.Driver
jdbc.url=jdbc:postgresql://localhost:5432/XXXXX?targetServerType=master
jdbc.user=XXXXXX
jdbc.password=XXXXXX
server.context-path=/Bitbucket

````
Then problem solved.
I got help from [here](https://confluence.atlassian.com/adminjiraserver073/connecting-jira-applications-to-postgresql-861253040.html) and [here](https://confluence.atlassian.com/adminjiraserver073/jira-application-home-directory-861253888.html).

**4)** Script

First of all you should **requirements.txt**:

````
   pip install -r requirements.txt
````
After that you must run **create_confing.py** for create confing file.It will want
you your Jira and Bitbucket usernames and passwords.


Finally you can run ***devops-internship.py***


I used two Python library that allows me to use the API for [Jira](https://jira.readthedocs.io/en/latest/) and [Bitbucket](https://stashy.readthedocs.io/en/latest/).
I connect to API, get projects from Jira.
If the project in Jira is not in Bitbucket, script add it.
If there is error, a warning messages show up that say you should look log file
Errors are written to the log file.

Finally you can run **devops-internship.py**

