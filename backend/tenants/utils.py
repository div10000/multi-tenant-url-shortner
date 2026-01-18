from .models import Tenant

def get_tenant_from_request(request):
    host = request.get_host().split(':')[0]

    try:
        return Tenant.objects.get(domain=host)
    except Tenant.DoesNotExist:
        return None
