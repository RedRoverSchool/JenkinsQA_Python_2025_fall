
class Endpoints:

    JOB_CONFIGURE_URL = lambda self, job_name: f"/job/{job_name}/configure"
    JOB_STATUS_PAGE_URL = lambda self, job_name: f"/job/{job_name}"
    MANAGE_URL = "/manage"
    SECURITY_REALM_URL = "/securityRealm/"
    VIEW_ALL_PAGE_URL = "/view/all/"
    ALL_NEW_JOB_URL = "/view/all/newJob"

    FOLDER_NEW_ITEM_URL = lambda self, folder_name: f"/job/{folder_name}/newJob"