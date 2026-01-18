from tenants.models import Tenant


class TenantCORSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        origin = request.headers.get("Origin")
        if not origin:
            return response

        domain = (
            origin.replace("https://", "")
            .replace("http://", "")
            .split(":")[0]
        )

        if Tenant.objects.filter(domain=domain).exists():
            response["Access-Control-Allow-Origin"] = origin
            response["Access-Control-Allow-Credentials"] = "true"
            response["Vary"] = "Origin"

        return response
