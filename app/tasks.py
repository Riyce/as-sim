from os import name
from celery import Celery, shared_task

from models import ExtractRequest
from storetask import StoreTask


app = Celery('tasks')
app.config_from_object('celeryconfig')


@app.task(bind=True, name='ps.similar')
def ps_similar(self, request: ExtractRequest):
    result = StoreTask().similar(request)
    return result