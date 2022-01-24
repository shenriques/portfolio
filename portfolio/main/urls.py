from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    # class based views have to have the as_view(), names are for html template
	path('', views.IndexView.as_view(), name="home"),
    path('contact/', views.ContactView.as_view(), name="contact"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
    # for detail view, portfolio entry will include slug in url. same for blog
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
]