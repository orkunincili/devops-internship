from jira import JIRA
import stashy
from classes import *
import sys



jandb = JiraAndBitbucket('config.ini')



"""Connect to API's"""
jira_api = JIRA(server=jandb.jira_url(), auth=jandb.auth_jira())
bitbucket_api = stashy.connect(jandb.bitbucket_url(),
                               jandb.bitbucket_username(),
                               jandb.bitbucket_password())

"""Listing projects in Jira and creating projects in Bitbucket"""
for project in jira_api.projects():
    print("Project name:", project)
    bitbucket_api.projects.create(project.name, project.name)
    


"""Listing projects in Bitbucket"""
print(bitbucket_api.projects.list())
