from datetime import datetime
from typing import Callable

from schedule_collector.scheduler.exceptions import TaskMethodNotImplementedError


class TaskDaysOfWeek:
    EVERYDAY = 127
    MONDAY = 2 ** 0
    TUESDAY = 2 ** 1
    WEDNESDAY = 2 ** 2
    THURSDAY = 2 ** 3
    FRIDAY = 2 ** 4
    SATURDAY = 2 ** 5
    SUNDAY = 2 ** 6


class Task:
    def __init__(self, name: str, frequency: str, repeated: bool = False, days_of_week: int = 0,
                 handler: Callable = None):
        """

        :param name:
        :param frequency: hour format. Ex.: 02:00.
        :param repeated: When repeated is True, it executes each [frequency] times.
         When False execute at [frequency] each day of week
        :param days_of_week: Sum of days of week: Integer until 127 where it bit represent a allowed day
        Ex.:
            MONDAY + TUESDAY + SUNDAY
            SUNDAY
            EVERYDAY
        """
        self.name = name
        self.frequency = frequency
        self.repeated = repeated
        self.days_week = days_of_week
        self._handler = handler

    @property
    def handler(self) -> Callable:
        if self._handler:
            return self._handler
        raise TaskMethodNotImplementedError()

    @property
    def execute_today(self):
        return datetime.today().isoweekday() & 2 != 0

    def run(self, force: bool = True):
        if force or self.execute_today:
            self.handler()
