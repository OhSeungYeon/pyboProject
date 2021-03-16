from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views

urlpatterns = [
    path('pybo/', include('pybo.urls')),
    # pybo/ 로 시작되는 페이지 요청은 모두 pybo/urls.py 파일에 있는 URL 매핑을 참고하라는 의미
    # 즉, pybo/ URL 매핑에 관해서는 더 이상 이 파일에서 하지 않아도 된다는 것이다.

    path('common/', include('common.urls')),

    path('admin/', admin.site.urls),
    #path('pybo/', views.index), #views 파일에 index 함수를 의미 (즉, pybo/ URL 과 views/index 함수(view 화면)를 매핑한 것이다.)

    path('', base_views.index, name='index')
]
