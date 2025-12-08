import requests
from core.links import Links
from core.config import Config


class JenkinUtils:
    def __init__(self):
        self.session = requests.Session()
        self.session.auth = (Config.USER_NAME, Config.USER_PASSWORD)
        self.crumb_field, self.crumb = self._get_crumb()
        self.headers = {self.crumb_field: self.crumb}

    def _get_crumb(self):
        response = self.session.get(Links.CRUMB_URL).json()
        return response['crumbRequestField'], response['crumb']

    def _get_all_jobs(self):
        response = self.session.get(f"{Links.BASE_URL}/api/json").json()
        return [job['name'] for job in response['jobs']]

    def delete_all_jobs(self):
        jobs = self._get_all_jobs()
        for job in jobs:
            response = self.session.post(url=Links.DELETE_URL.format(job), headers=self.headers)
            print(f"StatusCode: {response.status_code}")
