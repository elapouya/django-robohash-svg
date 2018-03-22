#
# Created : 2018-03-22
#
# @author: Eric Lapouyade
#

from django.http import HttpResponse
from .robotmaker import make_robot_svg

__all__ = ['robohash']

def robohash(request, string, *args, **kwargs):
    width = request.GET.get('width', 300)
    height = request.GET.get('height', 300)
    return HttpResponse(make_robot_svg(string, width, height),
                        content_type="image/svg+xml")
