from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email',max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        message = self.cleaned_data['message']

        conteudo = f'Nome: {name}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {message}'

        mail = EmailMessage(
            subject= assunto,
            body= conteudo,
            from_email= email,
            to=['contato@fusion.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()