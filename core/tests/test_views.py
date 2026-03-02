from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados = {
            'name': 'Teste',
            'email': 'teste@teste.com',
            'assunto': 'Teste',
            'message': 'Teste'
        }
        self.client = Client()
    
    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'name': 'Teste',
            'assunto': 'Teste',
        }        
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)