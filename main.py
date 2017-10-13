import simplejson as json
import os
from urllib2 import Request, urlopen, URLError
from os.path import join, dirname
from dotenv import load_dotenv

# Dotenv loading
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Global Constants
API_PRIVATE_TOKEN = os.environ.get('GITLAB_PRIVATE_TOKEN')
API_KEY_QUERY = '?private_token=' + API_PRIVATE_TOKEN
API_BASE_URL = 'https://gitlab.havaslynx.com/api/v4/'

all_projects_request = Request(API_BASE_URL + '/projects' + API_KEY_QUERY)


def create_projects_array():
    array_of_project_ids = []
    try:
        response = urlopen(all_projects_request)
        projects = json.loads(response.read())

        for project in projects:
            array_of_project_ids.append(project.get('id'))

        print array_of_project_ids
        return array_of_project_ids

    except URLError, e:
        print 'No Projects found', e


create_projects_array()
