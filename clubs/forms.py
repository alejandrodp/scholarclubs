from django import forms

from clubs.models import Club


class ClubSuggestForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'tag']


class ClubSelectionForm(forms.Form):
    clubs = forms.ModelMultipleChoiceField(
                        queryset=Club.objects.all(),
                        label="Clubs",
                        widget=forms.CheckboxSelectMultiple)
