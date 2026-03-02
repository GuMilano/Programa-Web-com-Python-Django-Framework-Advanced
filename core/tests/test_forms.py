from django.test import TestCase
from core.forms import ContactForm

class ContatoFormTestCase(TestCase):
    def setUp(self):
        self.nome = 'John Doe'
        self.email = 'john.doe@example.com'
        self.assunto = 'Test Subject'
        self.mensagem = 'Hello, this is a test message.'
        
        self.dados = {
            'name': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'message': self.mensagem,
        }

        self.form = ContactForm(data=self.dados)
    
    def test_send_email(self):
        form1 = ContactForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_email()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_email()

        self.assertEqual(res1, res2)
