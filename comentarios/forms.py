from dataclasses import fields
from pyexpat import model
from statistics import mode
from django.forms import ModelForm
from .models import Comentario
import requests
class FormComentario(ModelForm):
    def clean(self):
        raw_data=self.data
        recaptcha_response=raw_data.get('g-recaptcha-response')
        if not recaptcha_response:
            self.add_error(
                'comentario',
                'Marque o recaptcha'
            )

        recaptcha_request=requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret_key':'6Lc-qSshAAAAAATxpJNbeLUWXUCU0QRdpTa3ZGoD',
                'resposta_captcha':recaptcha_response
            }
        )
        recaptcha_result=recaptcha_request.json()
        print(recaptcha_result)

        if recaptcha_result.get('success'):
            self.add_error(
                'comentario',
                'Desculpe, recaptcha falhou!!'
            )
        
        cleaned_data=self.cleaned_data
        nome=cleaned_data.get('nome')
        if len(nome)<5:
            self.add_error(
                'nome',
                'O nome precisa conter mais de 5 caracteres.'
            )
        print(cleaned_data)
    class Meta:
        model=Comentario
        fields=('nome','email','comentario')