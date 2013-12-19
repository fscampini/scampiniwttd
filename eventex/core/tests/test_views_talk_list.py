#coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

class TalkListTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        'GET must result in 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template should be core/talk_list.html'
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        'Html should list talks.'
        self.assertContains(self.resp, u'Titulo da palestra', 2)
        self.assertContains(self.resp, u'10:00')
        self.assertContains(self.resp, u'13:00')
        self.assertContains(self.resp, u'/palestras/1/')
        self.assertContains(self.resp, u'/palestras/2/')
        self.assertContains(self.resp, u'/palestrantes/felipe-scampini/', 2)
        self.assertContains(self.resp, u'Passionate software developer!', 2)
        self.assertContains(self.resp, u'Felipe Scampini', 2)
        self.assertContains(self.resp, u'Descricao da palestra', 2)