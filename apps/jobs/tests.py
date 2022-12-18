from django.test import TestCase
from .forms import AddJobForm

class AddJobFormTestCase(TestCase):
  def test_form_valid(self):
    # Submit a valid form
    form_data = {
      'title': 'Software Engineer',
      'company': 'Acme Inc.',
      'desc': 'We are seeking a talented software engineer to join our team.',
      'long_desc': 'Seattle, WA'
    }
    form = AddJobForm(data=form_data)
    self.assertTrue(form.is_valid())

  def test_form_invalid(self):
    # Submit a form with missing data
    form_data = {
      'title': '',
      'company': 'Acme Inc.',
      'desc': 'We are seeking a talented software engineer to join our team.',
      'long_desc': 'Seattle, WA'
    }
    form = AddJobForm(data=form_data)
    self.assertFalse(form.is_valid())
    # Check that the form contains the appropriate error message
    self.assertEqual(form.errors['title'], ['This field is required.'])
