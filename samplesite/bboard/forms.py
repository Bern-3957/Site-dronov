from django.forms import ModelForm
from django.forms import modelform_factory, DecimalField
from django.forms.widgets import Select
from .models import Bb

# class BbForm(ModelForm):
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric',)

BbForm = modelform_factory(Bb,
        fields=('title', 'content', 'price', 'rubric'),
        labels={'title': 'Название товара'},
        help_texts={'rubric': 'He забудьте выбрать рубрику!'},
        field_classes={'price': DecimalField},)
        #widgets={'rubric': Select(attrs={'size': 7})})