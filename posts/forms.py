from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','title', 'comment']

    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    title = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'class':'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out'}),
        required=False
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 6, 'class':'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out'}),
        required=False
    )

class PostSearchForm(forms.Form):
    address = forms.CharField(
        max_length=255,
        required=False,
        label='',
        widget=forms.TextInput(
            attrs={
                "class": (
                    "bg-gray-50 border border-gray-300 text-gray-900 "
                    "text-sm rounded-lg focus:ring-blue-500 "
                    "focus:border-blue-500 block w-full ps-10 p-1 h-10 w-50"
                    "dark:bg-gray-700 dark:border-gray-600 "
                    "dark:placeholder-gray-400 dark:text-white "
                    "dark:focus:ring-blue-500 dark:focus:border-blue-500"
                ),
                "placeholder":"Enter place, city, country."
            }
        )
    )
