"""
Forms for the favorite places app.

created on: 14/09/2026
created by: Daryna Bogaevska
"""

from django import forms


class NewPlaceForm(forms.Form):
    """
    Form for adding a new place to the session list.
    """

    name = forms.CharField(label="Name", max_length=100)
    place_type = forms.CharField(label="Type", max_length=50)
    location = forms.CharField(label="Location", max_length=200, required=False)
    rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)
    description = forms.CharField(label="Description", widget=forms.Textarea)
