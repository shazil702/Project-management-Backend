import pytest
from datetime import date
from .models import Projects

@pytest.mark.django_db
def test_create_project():
    project = Projects.objects.create(projectName="Test Project", description="Description for test project", startDate=date(2025,8,4),dueDate=date(2025,3,5))
    assert project.projectName == 'Test Project'
    assert project.description == 'Description for test project'
    assert project.startDate == date(2025,8,4)
    assert project.dueDate == date(2025,3,5)
    assert project.status == 'notStarted'
    assert str(project) == "Test Project"