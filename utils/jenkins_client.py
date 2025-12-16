import requests


class JenkinsAPI:

    def __init__(self, base_url, user, token):
        self.base_url = base_url
        self.auth = (user, token)

    def create_item_from_file(self, name: str, config_xml: str, folder: str = None):
        if folder:
            url = f"{self.base_url}/job/{folder}/createItem?name={name}"
        else:
            url = f"{self.base_url}/createItem?name={name}"

        headers = {"Content-Type": "application/xml"}

        r = requests.post(
            url,
            auth=self.auth,
            headers=headers,
            data=config_xml
        )

        if r.status_code not in (200, 201):
            raise RuntimeError(f"Failed to create item: {r.status_code}, {r.text}")
