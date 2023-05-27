from django.forms import ModelForm
from .models import Document


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})