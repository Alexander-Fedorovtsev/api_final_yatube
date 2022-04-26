from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class PostsPagination(PageNumberPagination):
    page_size = 20


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "results": data,
            }
        )
