from django.shortcuts import render
from blog.models import Author, Post, Comment
from django.views import generic
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
	"""View function for home page of site."""
	return render(request, 'index.html')

class BlogListView(generic.ListView):
	"""
	Generic class-based view for a list of all blogs.
	"""
	model = Post

class BlogDetailView(generic.DetailView):
	"""
	Generic class-based detail view for a blog.
	"""
	model = Post

class BlogListbyAuthorView(generic.ListView):
	"""
	Generic class-based view for a list of blogs posted by a particular BlogAuthor.
	"""
	model = Post
	template_name ='blog/post_list_by_author.html'
	
	def get_queryset(self):
		"""
		Return list of Blog objects created by BlogAuthor (author id specified in URL)
		"""
		id = self.kwargs['pk']
		target_author=get_object_or_404(Author, pk = id)
		return Post.objects.filter(author=target_author)
		
	def get_context_data(self, **kwargs):
		"""
		Add PostAuthor to context so they can be displayed in the template
		"""
		# Call the base implementation first to get a context
		context = super(BlogListbyAuthorView, self).get_context_data(**kwargs)
		# Get the blogerger object from the "pk" URL parameter and add it to the context
		context['blogger'] = get_object_or_404(Author, pk = self.kwargs['pk'])
		return context

class BloggerListView(generic.ListView):
    """
    Generic class-based view for a list of bloggers.
    """
    model = Author