from .models import Message
from django import forms
from datetime import datetime
from django.contrib.auth.models import User

# - Chat -------------------------------------------------------------------
class SendMessage(forms.ModelForm):
    
    class Meta:
        model = Message
        fields = ['text']
    
    def save(self, commit=True, from_user=None, to_user=None):
        instance = super().save(commit=False)
        if from_user:
            instance.from_user = from_user  # Asignar el usuario logueado
        instance.creation_date = datetime.now()  # Asignar la fecha actual
        instance.to_user = User.objects.get(id=1)
        if commit:
            instance.save()
        return instance

class SendMessageByAdmin(forms.ModelForm):
    
    class Meta:
        model = Message
        fields = ['to_user', 'text']
    
    def save(self, commit=True, from_user=None):
        instance = super().save(commit=False)
        if from_user:
            instance.from_user = from_user  # Asignar el usuario logueado
        instance.creation_date = datetime.now()  # Asignar la fecha actual
        if commit:
            instance.save()
        return instance
