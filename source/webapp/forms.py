from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


class ToDoForm(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок', required=False)
    description = forms.CharField(max_length=3000, label='Описание', widget=widgets.Textarea, required=True)
    status = forms.CharField(max_length=100, label='Статус', required=False)
    created_at = forms.DateTimeField(label='Дата', required=False)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длинее 2 символов')





