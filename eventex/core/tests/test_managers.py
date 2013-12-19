# coding: utf-8
from django.test import TestCase
from eventex.core.models import Contact, Speaker

class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Felipe Scampini', slug='felipe-scampini', url='http://fscampini.net')
        s.contact_set.add(Contact(kind='E', value='fscampini@gmail.com'),
                          Contact(kind='P', value='21-81066625'),
                          Contact(kind='F', value='21-12346625'))

    def test_emails(self):
        qs = Contact.emails.all()
        expected = ['<Contact: fscampini@gmail.com>']
        self.assertQuerysetEqual(qs, expected)

    def test_phones(self):
        qs = Contact.phones.all()
        expected = ['<Contact: 21-81066625>']
        self.assertQuerysetEqual(qs, expected)

    def test_faxes(self):
        qs = Contact.faxes.all()
        expected = ['<Contact: 21-12346625>']
        self.assertQuerysetEqual(qs, expected)