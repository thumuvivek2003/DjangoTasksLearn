# myapp/middleware.py
import time
from django.http import JsonResponse
import time
import logging

logger = logging.getLogger(__name__)

class SimpleLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        # 🔹 Log incoming request path
        print(f"📥 Request: {request.method} {request.path}")

        response = self.get_response(request)

        # 🔹 Log time taken
        duration = time.time() - start_time
        print(f"⏱️ Took {duration:.2f} seconds to process")

        return response



VISIT_LOG = {}

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.max_requests = 5
        self.time_window = 60  # in seconds

    def __call__(self, request):
        ip = self.get_client_ip(request)
        now = time.time()

        # Initialize if IP not seen before
        if ip not in VISIT_LOG:
            VISIT_LOG[ip] = []

        # Remove timestamps older than the window
        VISIT_LOG[ip] = [t for t in VISIT_LOG[ip] if now - t < self.time_window]

        if len(VISIT_LOG[ip]) >= self.max_requests:
            return JsonResponse({'error': 'Rate limit exceeded. Try again later.'}, status=429)

        # Log this request
        VISIT_LOG[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')