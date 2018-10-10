from django.views.generic import TemplateView
from django.shortcuts import render

from home.forms import HomeForm

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            #clean something like sql injections by code cleaned_data
            text = form.cleaned_data['post']
        args = {'form': form, 'text': text}   
        return render(request, self.template_name, {'form': form})