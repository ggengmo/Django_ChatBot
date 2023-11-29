# chatting > decorators.py

from django.core.cache import cache
from django.http import HttpResponse

def daily_limit(func):
    def wrapper(self, *args, **kwargs):
        user = self.request.user
        count = cache.get(f'chatbot_count_{user.id}', 0)

        if count >= 5:
            return HttpResponse('하루에 5회만 이용 가능합니다.', status=429)

        response = func(self, *args, **kwargs)

        if self.request.method == 'POST':
            count += 1
            cache.set(f'chatbot_count_{user.id}', count, 86400)

        return response
    return wrapper
