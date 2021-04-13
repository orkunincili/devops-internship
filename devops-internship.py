from jira import JIRA
import stashy
from classes import *
import sys
import logging



jandb = JiraAndBitbucket('config.ini')
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
err = False

"""Connect to API's"""
jira_api = JIRA(server=jandb.jira_url(), auth=jandb.auth_jira())
bitbucket_api = stashy.connect(jandb.bitbucket_url(),
                               jandb.bitbucket_username(),
                               jandb.bitbucket_password())

"""Listing projects in Jira and creating projects in Bitbucket"""
print("#### Projects in Jira ####")
for project in jira_api.projects():

    print("Project name:", project)
    try:
        new_project = bitbucket_api.projects.create(project.name, project.name)
        print(f"Projet {new_project['name']} was created successfully in Bıtbucket")

    except stashy.errors.GenericException as error:
        err = True
        for e in error.data['errors']:

            logging.error(f"Error: {e['message']} for {project}")

print("\n")
if err:
    """Warning message stating that if there is an error, it has written it to the log file."""
    print("WARNING - Found error(s), you may want to check 'app.log'.")

#"""Listing projects in Bitbucket"""
#print(bitbucket_api.projects.list())
