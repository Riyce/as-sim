from celery import shared_task

from models import ExtractRequest, ExtractResponse
from storetask import StoreTask


@shared_task(name="ps.similar", base=StoreTask)
def ps_similar(self, request: ExtractRequest):
    result = self.similar(request.id, request.similar_clp, request.country)
    return result