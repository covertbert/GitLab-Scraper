from urllib2 import Request, urlopen, URLError
import simplejson as json
import os
from dotenv import load_dotenv

# Global Constants
API_PRIVATE_TOKEN = os.environ.get('GITLAB_PRIVATE_TOKEN')
API_KEY_QUERY = '?private_token='
API_BASE_URL = 'https://gitlab.havaslynx.com/api/v4/'

# Dotenv loading
dotenv_path = '.env'
load_dotenv(dotenv_path)

all_projects_request = Request(API_BASE_URL + '/projects' + API_KEY_QUERY)
array_of_project_ids = []


def create_projects_array():
    try:
        response = urlopen(all_projects_request)
        projects = json.loads(response.read())

        for project in projects:
            array_of_project_ids.append(project.get('id'))

    except URLError, e:
        print 'No Projects found', e


create_projects_array()

print array_of_project_ids
