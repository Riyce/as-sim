from lightparser import LightParser
from models import ExtractResponse, ExtractRequest


class StoreTask:
    def similar(self, request: ExtractRequest) -> ExtractResponse:
        apps = LightParser().extract(
            request.similar_clp, 'en_US', request.country
        )
        return ExtractResponse(request.id, apps)
