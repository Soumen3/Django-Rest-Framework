from rest_framework.pagination import LimitOffsetPagination

class MyOffsetPagination(LimitOffsetPagination):
	default_limit = 5
	max_limit = 10
	limit_query_param = 'mylimit'
	offset_query_param = 'myoffset'