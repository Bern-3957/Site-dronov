from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import *
from .forms import *

def index(request):
    # s = 'Список объявлений\r\n\r\n\r\n'
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type='text/plain; charset=UTF-8')
    bbs = Bb.objects.all()
    context = {'bbs': bbs,}
    return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)  # Все объявления с данной рубрикой
    current_rubric = Rubric.objects.get(pk=rubric_id)  # берет конкр рубрику с данной id
    context = {'bbs': bbs, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

# def add(request):
#
#     if request.method == 'POST':
#         form = Bbform(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#     else:
#         form = Bbform()
#
#     rubrics = Rubric.objects.all()
#     context = {'rubrics': rubrics, 'form': form}
#
#     return render(request, 'bboard/create.html', context=context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


# Create your views here.

