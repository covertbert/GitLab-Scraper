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
API_KEY_QUERY = '&private_token=' + API_PRIVATE_TOKEN
API_BASE_URL = 'https://gitlab.havaslynx.com/api/v4'


def create_projects_array():
    all_projects = Request(API_BASE_URL + '/projects?per_page=1000' + API_KEY_QUERY)
    array_of_project_ids = []
    try:
        response = urlopen(all_projects)
        projects = json.loads(response.read())

        for project in projects:
            # Only push to array if London project
            if project.get('namespace').get('name') == 'London':
                array_of_project_ids.append(project.get('id'))

        return array_of_project_ids

    except URLError, e:
        print 'No Projects found', e


def get_total_commits():
    projects = create_projects_array()
    print projects


get_total_commits()
