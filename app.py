from celery import Celery as _Celery
from celery.utils.log import get_logger

_logger = get_logger(__name__)


class Celery(_Celery):
    def _get_backend(self):
        _logger.info(f"Importing backend from {self.conf.result_backend}")
        return super()._get_backend()


app = Celery('tasks', broker='redis://redis/0', backend='redis://redis/0')


@app.task
def add(x, y):
    return x + y
