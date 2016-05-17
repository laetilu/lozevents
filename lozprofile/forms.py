from django import forms
from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupForm

class SignupFormExtra(SignupForm):
    # company_name = forms.CharField(label=_(u'First name'),
    #                                max_length=200,
    #                                required=False)


    first_name = forms.CharField(label=_(u'First name'),
                                 max_length=30,
                                 required=False)

    last_name = forms.CharField(label=_(u'Last name'),
                                max_length=30,
                                required=False)


    # def __init__(self, *args, **kw):
    #
    #     super(SignupFormExtra, self).__init__(*args, **kw)

    def save(self):
        new_user = super(SignupFormExtra, self).save()

        user_profile = new_user

        user_profile.first_name = self.cleaned_data['first_name']
        user_profile.last_name = self.cleaned_data['last_name']

        user_profile.save()

        if self.cleaned_data['profile_part'] == 'profile_part':
            pro = ProfilePro(profile = new_user.get_profile(), user=new_user)
            pro.save()


        # elif self.cleaned_data['teacher_or_student'] == 'profile_pro':
        #     student = Student(profile = new_user.get_profile())
        #     student.save()


        return new_user
