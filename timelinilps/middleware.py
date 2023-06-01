from datetime import datetime, timedelta
from django.utils.cache import patch_response_headers

class DisableBrowserCachingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        patch_response_headers(response, cache_timeout=0)
        response['Expires'] = (datetime.utcnow() - timedelta(minutes=1)).strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response