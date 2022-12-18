from django.test import TestCase
from .forms import AddJobForm, ApplyForm

class AddJobFormTestCase(TestCase):
  def test_form_valid(self):
    form_data = {
      'title': 'Software Engineer',
      'company': 'Acme Inc.',
      'desc': 'We are seeking a talented software engineer to join our team.',
      'long_desc': 'Seattle, WA'
    }
    form = AddJobForm(data=form_data)
    self.assertTrue(form.is_valid())

  def test_form_invalid(self):
    form_data = {
      'title': '',
      'company': 'Acme Inc.',
      'desc': 'We are seeking a talented software engineer to join our team.',
      'long_desc': 'Seattle, WA'
    }
    form = AddJobForm(data=form_data)
    self.assertFalse(form.is_valid())


class ApplyJobFormTestCase(TestCase):
  def test_apply_form_valid(self):
    form_data = {
      'content': 'This is a coverletter for no reason',
      'experience': '1-3 years'
    }
    form = ApplyForm(data=form_data)
    self.assertTrue(form.is_valid())

  def test_apply_form_invalid(self):
    form_data = {
      'content': 'This is a coverletter for no reason',
      'experience': ''
    }
    form = ApplyForm(data=form_data)
    self.assertFalse(form.is_valid())