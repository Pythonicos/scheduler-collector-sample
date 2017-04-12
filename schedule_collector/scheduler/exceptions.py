class ScheduleCollectorError:
    pass


class TaskMethodNotImplementedError(NotImplementedError, ScheduleCollectorError):
    def __init__(self):
        super(TaskMethodNotImplementedError, self).__init__("Task method is not define. I don't know what to do.")


class TaskAlreadyAppendedError(ScheduleCollectorError):
    def __init__(self):
        super(TaskAlreadyAppendedError, self).__init__()
