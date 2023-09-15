from django import forms
from .models import Place, Comment
from django.utils import timezone


class UploadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "location":
                field.widget.attrs["placeholder"] = "Enter photo location"
            elif field_name == "end_time":
                field.widget.attrs["placeholder"] = "Enter quiz ending time"
                field.widget = forms.DateTimeInput(
                    attrs={
                        "type": "datetime-local",
                    }
                )

            field.widget.attrs.update(
                {
                    "class": "block w-full px-3 py-1.5 text-gray-700 border rounded-md bg-gray-100 border-gray-600 placeholder-gray-400 focus:border-blue-500 focus:outline-none focus:ring",
                }
            )

    class Meta:
        model = Place
        fields = ["photo", "end_time", "location"]

    def clean_end_time(self):
        end_time = self.cleaned_data.get("end_time")
        if end_time < timezone.now():
            raise forms.ValidationError("Photo size exceeds the 20mb.")
        return end_time


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "block w-full px-3 py-1.5 text-gray-700 border rounded-md bg-gray-100 border-gray-600 placeholder-gray-400 focus:border-blue-500 focus:outline-none focus:ring",
                }
            )
            if field_name == "text":
                field.widget.attrs["placeholder"] = "Guess photo location"

    class Meta:
        model = Comment
        fields = ["text"]
