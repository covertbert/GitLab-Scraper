import simplejson as json
import os

from urllib2 import Request, urlopen, URLError
from os.path import join, dirname
from dotenv import load_dotenv

# Loads dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def api_request(api_segment, other_queries):
    # Sets API request variables
    api_private_token = os.environ.get('GITLAB_PRIVATE_TOKEN')
    api_key = '?private_token=' + api_private_token
    api_base_url = 'https://gitlab.havaslynx.com/api/v4'

    # Checks if there are any extra query parameters
    if other_queries:
        request = api_base_url + api_segment + api_key + other_queries
    else:
        request = api_base_url + api_segment + api_key

    # Tries to make the request and returns stack trace on fail
    try:
        response = urlopen(Request(request))
        response_formatted = json.loads(response.read())

        return response_formatted

    except URLError, e:
        print e


def create_projects_array():
    # Sets function scoped variables
    all_projects = api_request('/projects', '&per_page=1000')
    array_of_project_ids = []

    for project in all_projects:
        # Only pushes to array if project is in London namespace
        if project.get('namespace').get('name') == 'London':
            array_of_project_ids.append(project.get('id'))

    print 'There are %s projects in the London namespace' % len(array_of_project_ids)
    return array_of_project_ids


def get_total_commits():
    # Sets function scoped variables
    project_ids = create_projects_array()
    commits_array = []

    # Loops through array of project IDs and gets each project's commits
    for project_id in project_ids:
        project_commits = api_request('/projects/' + str(project_id) + '/repository/commits', False)

        # Loops through the array of current project's commits and pushes them to global commits array
        for commit in project_commits:
            commits_array.append(commit)

    print 'Each project has an average of %s commits on the master branch' % (len(commits_array) / len(project_ids))
    print 'There is a total of %s commits on all master branches across the London namespace' % len(commits_array)


get_total_commits()
