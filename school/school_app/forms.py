from django import forms
from .models import Registration, Courses


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['course'].queryset = Courses.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Courses.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')