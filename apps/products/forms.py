from django import forms
from apps.products.models import Event


class EventAdminForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = []

    # def clean(self):
    #     actual_from = self.cleaned_data['actual_from']
    #     actual_till = self.cleaned_data['actual_till']
    #
    #     for event in Event.objects.all():
    #         if event.actual_from < actual_from < event.actual_till:
    #             raise forms.ValidationError('акции пересекаются')
    #         elif event.actual_from < actual_till < event.actual_till:
    #             raise forms.ValidationError('акции пересекаются')
    #         elif actual_from < event.actual_from and actual_till > event.actual_till:
    #             raise forms.ValidationError('акции пересекаются')
    #
    #     return self.cleaned_data
