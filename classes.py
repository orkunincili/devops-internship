import configparser


class JiraAndBitbucket:

    jira_conf=None
    bitbucket_conf=None

    def __init__(self, conf_file):

        config = configparser.ConfigParser()
        config.read(conf_file)
        self.jira_conf = config['JIRA']
        self.bitbucket_conf = config['BITBUCKET']


    def jira_url(self):
        """Return the Jira base url"""
        return self.jira_conf['host']+self.jira_conf['port']+self.jira_conf['path']


    def bitbucket_url(self):
        """Return the Bitbucket base url"""
        return self.bitbucket_conf['host']+self.bitbucket_conf['port']+self.bitbucket_conf['path']


    def auth_jira(self):
        """Return Jira username and password as a Tuple"""

        return (self.jira_username(), self.jira_password())


    def jira_username(self):
        """Return Jira username"""
        return self.jira_conf['username']


    def jira_password(self):
        """Return Jira password"""
        return self.jira_conf['password']


    def bitbucket_username(self):
        """Return Bitbucket username"""
        return self.bitbucket_conf['username']


    def bitbucket_password(self):
        """Return Bitbucket password"""
        return self.bitbucket_conf['password']
