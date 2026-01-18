from rest_framework.decorators import api_view
from rest_framework.response import Response
from tenants.models import Tenant
from .serializers import TenantSerializer
from .utils import get_tenant_from_request

@api_view(['GET'])
def tenant_info(request):
    tenant = get_tenant_from_request(request)
    if not tenant:
        return Response({"error": "Invalid tenant"}, status=400)

    serializer = TenantSerializer(tenant)
    return Response(serializer.data)
