from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

# 处理课程机构列表的view
class OrgView(View):
    def get(self, request):
        return render(request, "org_list.html", {})

