from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ShortURL
from .serializers import ShortURLSerializer
from .utils import generate_short_code
from tenants.utils import get_tenant_from_request
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse

def home(request):
    return HttpResponse(
        "<h2>Welcome to Multi-Tenant URL Shortener!</h2>"
        "<p>Use /api/shorten/ to create short URLs.</p>"
    )

def redirect_url(request, short_code):
    tenant = get_tenant_from_request(request)

    short_url = get_object_or_404(
        ShortURL,
        tenant=tenant,
        short_code=short_code
    )

    return redirect(short_url.original_url)

def get_unique_code():
    while True:
        code = generate_short_code()
        if not ShortURL.objects.filter(short_code=code).exists():
            return code


@api_view(['POST'])
def shorten_url(request):
    tenant = get_tenant_from_request(request)

    if not tenant:
        return Response(
            {"error": "Invalid tenant"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = ShortURLSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    short_code = get_unique_code()

    short = ShortURL.objects.create(
        tenant=tenant,
        original_url=serializer.validated_data['original_url'],
        short_code=short_code
    )

    return Response(
        {
            "short_url": f"http://{request.get_host()}/{short.short_code}",
            "original_url": short.original_url
        },
        status=status.HTTP_201_CREATED
    )
