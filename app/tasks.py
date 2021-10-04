from celery import Celery

from models import ExtractRequest
from storetask import StoreTask


app = Celery('tasks')
app.config_from_object('celeryconfig')


@app.task
def ps_similar(request: ExtractRequest):
    result = StoreTask().similar(request)
    return result
