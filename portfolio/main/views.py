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

# Portfolio page
class PortfolioView(generic.ListView):
	model = PortfolioEntry
	template_name = "main/portfolio.html"
	# show the first 10 entries
	paginate_by = 10

	def get_queryset(self):
		# only retrieve active entries
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = PortfolioEntry
	# shows the entry that has the slug in the url
	template_name = "main/portfolio-detail.html"

# Blog page
class BlogView(generic.ListView):
	model = BlogPost
	template_name = "main/blog.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = BlogPost
	# shows the entry that has the slug in the url
	template_name = "main/blog-detail.html"

# Contact page
class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	# where users get redirected to if the message sent
	success_url = "/"
	
	def form_valid(self, form):
		# save the form before showing success message
		form.save()
		messages.success(self.request, 'Thanks for the message! I\'ll be in touch :)')
		return super().form_valid(form)

