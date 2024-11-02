import asyncio
from django.http import JsonResponse
from django.utils import timezone

async def async_timer_view(request):
    start_time = timezone.now()
    await asyncio.sleep(5)  # Contador de tempo (5 segundos)
    end_time = timezone.now()
    elapsed_time = (end_time - start_time).total_seconds()

    return JsonResponse({
        'message': 'Contador assíncrono concluído!',
        'elapsed_time': elapsed_time,
    })
