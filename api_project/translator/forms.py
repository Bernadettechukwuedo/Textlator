from django import forms
from deep_translator import GoogleTranslator


def list_languages():
    try:
        languages = GoogleTranslator().get_supported_languages(as_dict=True)
        return [(code, name.title()) for name, code in languages.items()]
    except:
        return [("en", "English"), ("es", "Spanish"), ("fr", "French")]


class TranslationForm(forms.Form):
    source_language = forms.ChoiceField(
        choices=list_languages(), initial="en", label="Source Language"
    )
    target_language = forms.ChoiceField(
        choices=list_languages(), label="Target Language"
    )
    text_to_translate = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter text to translate...",
                "class": "outline-none text-lg",
            }
        ),
        label="Text to Translate",
    )
