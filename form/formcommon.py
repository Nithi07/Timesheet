from django import forms

from QMS.models import Audittype, EmployePosition, EmployeDepartment
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset





class Audittypeform(forms.ModelForm):
        audittype = forms.CharField(label = "Audit Type") 
        auditcode = forms.CharField(label = "Audit Code") 

        def __init__(self, *args, **kwargs):
            super(Audittypeform, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            #self.helper.form_method = 'post'
            #self.helper.form_action = reverse('audittype_view.html')
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
            self.helper.form_class = 'form-horizontal'
            self.helper.layout = Layout(
                ('audittype'),
                ('auditcode')
                )


        class Meta:
            """Meta Attributes"""
            model = Audittype
            fields = ['audittype','auditcode']

                
            

class EmployePositionform(forms.ModelForm):
        emp_posn = forms.CharField(label = "Employee Categorie") 
       

        def __init__(self, *args, **kwargs):
            super(EmployePositionform, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            #self.helper.form_method = 'post'
            #self.helper.form_action = reverse('audittype_view.html')
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
            self.helper.form_class = 'form-horizontal'
            self.helper.layout = Layout(
                ('emp_posn')
                )


        class Meta:
            """Meta Attributes"""
            model = EmployePosition
            fields = ['emp_posn']




class EmployeDepartmentform(forms.ModelForm):
        department_name = forms.CharField(label = "Department Name") 
        dept_code = forms.CharField(label = "Department Code") 

        def __init__(self, *args, **kwargs):
            super(EmployeDepartmentform, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            #self.helper.form_method = 'post'
            #self.helper.form_action = reverse('audittype_view.html')
            self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
            self.helper.form_class = 'form-horizontal'
            self.helper.layout = Layout(
                ('department_name'),
                ('dept_code')
                )


        class Meta:
            """Meta Attributes"""
            model = EmployeDepartment
            fields = ['department_name','dept_code']

                