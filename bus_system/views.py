from django.shortcuts import render
from .models import Dispatch, LocationHistory
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def realtime_monitor(request):
    active_dispatches = Dispatch.objects.filter(
        booking__status='C'
    ).select_related('driver', 'vehicle')
    
    context = {
        'active_dispatches': active_dispatches
    }
    return render(request, 'bus_system/realtime_monitor.html', context)

@csrf_exempt
def update_location(request, dispatch_id):
    if request.method == 'POST':
        try:
            dispatch = Dispatch.objects.get(id=dispatch_id)
            data = json.loads(request.body)
            LocationHistory.objects.create(
                dispatch=dispatch,
                latitude=data['latitude'],
                longitude=data['longitude']
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'invalid_method'}, status=405)

def statistics_view(request):
    # 实际项目中应使用Matplotlib/Plotly生成图表
    # 这里使用静态数据演示
    stats_data = {
        'bookings_per_day': [45, 52, 48, 55, 60, 58, 65],
        'vehicle_utilization': [80, 85, 78, 90, 92, 88, 95],
        'popular_routes': [
            {'name': '校区A - 校区B', 'count': 120},
            {'name': '校区B - 校区C', 'count': 85},
            {'name': '校区C - 校区A', 'count': 65}
        ]
    }
    
    # 将数据转换为JSON字符串
    stats_json = json.dumps(stats_data)
    
    return render(request, 'bus_system/statistics.html', {
        'stats': stats_data,
        'stats_json': stats_json
    })