import simplejson as json
import os

from urllib2 import Request, urlopen, URLError
from os.path import join, dirname
from dotenv import load_dotenv

# Dotenv loading
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def api_request(api_segment, other_queries):
    api_private_token = os.environ.get('GITLAB_PRIVATE_TOKEN')
    api_key = '?private_token=' + api_private_token
    api_base_url = 'https://gitlab.havaslynx.com/api/v4'

    if other_queries:
        request = api_base_url + api_segment + api_key + other_queries
    else:
        request = api_base_url + api_segment + api_key

    return Request(request)


def create_projects_array():
    all_projects = api_request('/projects', '&per_page=1000')
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
    project_ids = create_projects_array()
    commits_array = []

    for project_id in project_ids:
        project_commits = api_request('/projects/' + str(project_id) + '/repository/commits', False)

        try:
            response = urlopen(project_commits)
            commits = json.loads(response.read())

            for commit in commits:
                print commit

        except URLError, e:
            print 'No Commits found', e


get_total_commits()
