from django.shortcuts import render
from .forms import TranslationForm
from deep_translator import GoogleTranslator

# Create your views here.
def index(request):
    translated_text = ""
    if request.method == "POST":

        form = TranslationForm(request.POST)
        if form.is_valid():
            src= form.cleaned_data['source_language']
            tgt= form.cleaned_data['target_language']
            text= form.cleaned_data['text_to_translate']
            try:
                translated_text = GoogleTranslator(source=src, target=tgt).translate(text)
            except:
                translated_text = "Error: Could not connect to translation service."
    else:
        form = TranslationForm()
            
    return render(request, 'translator/index.html', {'form': form, 'translated_text': translated_text})
    