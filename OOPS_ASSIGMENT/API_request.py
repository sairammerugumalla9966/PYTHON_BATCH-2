def build_api_request(endpoint, *args, **kwargs):
    print("Endpoint:", endpoint)
    print("Positional Parameters:", args)
    print("Query Parameters:", kwargs)


build_api_request(
    "/users",
    "v1",
    "active",
    limit=10,
    sort="desc"
)