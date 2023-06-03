from django import forms
from .models import dialogue, QA

class SubmitForm():
    class Meta:
        model = dialogue
        fields = ("message",)