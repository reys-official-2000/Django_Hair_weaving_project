from django.views.generic import TemplateView
from model.models import Model





class HomePageView(TemplateView):
    template_name = 'home/home.html'
    model = Model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['french'] = Model.objects.filter(name_en='french')
        context['dutch'] = Model.objects.filter(name_en='dutch')
        context['mexican'] = Model.objects.filter(name_en='mexican')
        context['fishtail'] = Model.objects.filter(name_en='fishtail')
        context['chignon'] = Model.objects.filter(name_en='chignon')
        return context



