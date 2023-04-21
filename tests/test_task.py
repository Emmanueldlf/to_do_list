import pytest
from app.task import Task

@pytest.fixture
def TestClassTask(app):
    def tasks_list():
        """a tasks list that will be available to all test functions."""
        tasks_list = Task()
        return tasks_list

    def test_add_task(tasks_list):
        """Test that a task is added properly"""

        assert self.task in self.tasks
