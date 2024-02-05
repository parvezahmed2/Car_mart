from django.shortcuts import render, redirect,get_object_or_404
from . import forms
from . import models
from brand.models import CarModel
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator   # class base view login required 
from django.urls import  reverse_lazy
from django.views.generic import DetailView
 
# Create your views here.




class DetailPostView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post 
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object   # post model er object  ekhane store korlam 
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments']  = comments
        context['comment_form'] = comment_form
        return context  




@login_required
def buyNow(request, car_id):
    car = get_object_or_404(models.Car, pk=id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        return render(request, 'profile.html', {'car': car})
    else:
        return render(request, 'profile.html', {'car': car})