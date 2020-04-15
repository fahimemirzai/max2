from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import forms
from django.shortcuts import redirect

class HomeView(generic.TemplateView):
    template_name='home/home.html'

    def get(self,request):
        form=forms.HomeForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=forms.HomeForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()

            text=form.cleaned_data['post']

            form=forms.HomeForm()
            return redirect('home:home')


        return render(request,self.template_name,{'form':form,'text':text})

