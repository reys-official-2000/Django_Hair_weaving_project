from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Model
from django.views.generic import ListView
from .models import Model






class ModelDetailsView(DetailView):
    model = Model
    template_name = 'details.html'
    context_object_name = 'model'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_model = self.get_object()
        similar_models = Model.objects.filter(name_fa=current_model.name_fa).exclude(pk=current_model.pk).order_by('?')[:5]
        context['similar_models'] = similar_models
        return context








class BaseModelListView(ListView):
    model = Model
    template_name = 'model.html'
    context_object_name = 'model_list'
    paginate_by = 12

    def get_queryset(self):
        language = self.kwargs.get('language', 'dutch')
        return Model.objects.filter(name_en=language).order_by('-created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_obj = context['page_obj']

        if paginator.num_pages <= 4:
            page_range = paginator.page_range
        else:
            page_range = []
            if page_obj.number > 2:
                page_range.append(1)
                if page_obj.number > 3:
                    page_range.append('...')

            page_range.extend(
                num for num in range(max(1, page_obj.number - 1), min(paginator.num_pages + 1, page_obj.number + 2))
            )

            if page_obj.number < paginator.num_pages - 1:
                if page_obj.number < paginator.num_pages - 2:
                    page_range.append('...')
                page_range.append(paginator.num_pages)

        context['page_range'] = page_range
        context['show_start_end'] = paginator.num_pages > 4
        return context

class DutchModelListView(BaseModelListView):
    pass

class FrenchModelListView(BaseModelListView):
    def get_queryset(self):
        return Model.objects.filter(name_en='french').order_by('-created')


class MexicanModelListView(BaseModelListView):
    def get_queryset(self):
        return Model.objects.filter(name_en='mexican').order_by('-created')


class FishTailModelListView(BaseModelListView):
    def get_queryset(self):
        return Model.objects.filter(name_en='fishtail').order_by('-created')


class ChignonModelListView(BaseModelListView):
    def get_queryset(self):
        return Model.objects.filter(name_en='chignon').order_by('-created')


class JournalModelListView(BaseModelListView):
    def get_queryset(self):
        return Model.objects.filter(name_en='journal').order_by('-created')


class SpiralModelListView(BaseModelListView):
    def get_queryset(self):
        return Model.objects.filter(name_en='spiral').order_by('-created')






class AboutView(TemplateView):
    template_name = 'about.html'
    extra_context = {
        'whatsapp': '+98901234567', # Phone number
        'instagram': 'reys__official', # id instagram
        'telegram': 'reys_89', # id telegram
    }





