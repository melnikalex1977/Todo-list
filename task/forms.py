from django.contrib.auth import get_user_model
from django import forms


from task.models import Task, Tag

class TaskLicenseUpdateForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
