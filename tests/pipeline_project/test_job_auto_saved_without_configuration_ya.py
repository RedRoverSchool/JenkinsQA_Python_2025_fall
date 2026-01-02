from data.enums import ItemType
from utils.generators.project_generator import ProjectGenerator
from data.endpoints import Endpoints


def test_tc_01_004_04_job_auto_saved_without_configuration(create_job, page):
    """TC_01.004.04 | New Item > Select an Item type > Verify job is automatically saved without configuration"""

    pipeline_name = ProjectGenerator.generate_pipeline_name()
    create_job(pipeline_name, ItemType.PIPELINE)
    page.goto(Endpoints().VIEW_ALL_PAGE_URL)

    assert pipeline_name in page.content()



