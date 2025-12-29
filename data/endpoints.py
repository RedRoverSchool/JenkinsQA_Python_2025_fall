
class Endpoints:

    JOB_CONFIGURE_URL = lambda self, job_name: f"/job/{job_name}/configure"
    JOB_STATUS_PAGE_URL = lambda self, job_name: f"/job/{job_name}"
    MANAGE_URL = "/manage"
    SECURITY_REALM_URL = "/securityRealm/"
    VIEW_ALL_PAGE_URL = "/view/all/"