from django.views import generic 
from django.urls import reverse_lazy
from boto3 import Session
from .models import Translate
from django.core.files.base import ContentFile

class TranslateListView(generic.ListView):
  model = Translate
  template_name = 'translate/list.html'

class TranslateDetailView(generic.DetailView):
  model = Translate
  template_name = 'translate/detail.html'

class TranslateCreateView(generic.CreateView):
  model = Translate
  template_name = 'translate/create.html'
  success_url = reverse_lazy('translate:list')
  fields = ['text']
  
  def form_valid(self, form):
    translate = form.save(commit=False)
    response = use_translate(translate.text)
    if "TranslatedText" in response:
        translate.translated_text = response["TranslatedText"]
    translate.save()
    return super().form_valid(form)

def use_translate(text):

    # create session
    session = Session(profile_name="default")
    translate = session.client("translate")

    # create translation data
    response = translate.translate_text(
                Text = text,
                SourceLanguageCode='ja',
                TargetLanguageCode='en'
                )

    return response
