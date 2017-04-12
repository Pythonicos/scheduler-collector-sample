from typing import List

from schedule_collector.scheduler.exceptions import TaskAlreadyAppendedError
from schedule_collector.scheduler.task import Task


class SchedulerCollector:
    TaskList = List[Task]

    def __init__(self, task_list: List):
        self.tasks = {task.name: task for task in task_list}

    def append_task(self, task: Task):
        if task.name not in self.tasks:
            self.tasks[task.name] = task
            return Task
        raise TaskAlreadyAppendedError()
