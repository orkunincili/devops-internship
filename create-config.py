import configparser
import sys
config = configparser.ConfigParser()

config["JIRA"] = {
    "host": "http://localhost",
    "port": ":8080",
    "path": "/JIRA",
    "username": "",
    "password": ""
}

config["BITBUCKET"] = {
    "host": "http://localhost",
    "port": ":7990",
    "path": "/Bitbucket",
    "username": "",
    "password": ""
}


"""Info message"""
print("""Usernames and passwords are empty in config file.You should say me your
Jira and Bitbucket username and password\n""")

"""Jira username and password"""
print('Jira username:', end='')
jira_username = str(input())
print('Jira password:', end='')
jira_password = str(input())

"""Bitbucket username and password"""
print('Bitbucket username:', end='')
bitbucket_username = str(input())
print('Bitbucket password:', end='')
bitbucket_password = str(input())

with open('config.ini', 'w') as configfile:
    config['JIRA']['username'] = jira_username
    config['JIRA']['password'] = jira_password
    config['BITBUCKET']['username'] = bitbucket_username
    config['BITBUCKET']['password'] = bitbucket_password

    config.write(configfile)
