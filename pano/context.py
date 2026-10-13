from .models import Notification
def common(request):
    if request.user.is_authenticated:
        return {'unread_count': Notification.objects.filter(recipient=request.user, read_at__isnull=True).count()}
    return {}
