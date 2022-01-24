from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from . forms import ContactForm
from . models import (
		UserProfile,
		BlogPost,
		PortfolioEntry,
		Testimonial,
		Certificate
	)

# Homepage
class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		# only retrieve lists of the active data 
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blog_posts = BlogPost.objects.filter(is_active=True)
		portfolio_entries = PortfolioEntry.objects.filter(is_active=True)
		
		# enable home page to access content objects
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blog_posts"] = blog_posts
		context["portfolio_entries"] = portfolio_entries
		
		return context
