from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.models import inlineformset_factory


from userena.forms import SignupForm
from models import ProfilePart, ProfilePro

class SignupFormExtra(SignupForm):
    # company_name = forms.CharField(label=_(u'Company name'),
    #                                max_length=200,
    #                                required=False)

    first_name = forms.CharField(label=_(u'First name'),
                                 max_length=30,
                                 required=False)

    last_name = forms.CharField(label=_(u'Last name'),
                                max_length=30,
                                required=False)



    def save(self):
        new_user = super(SignupFormExtra, self).save()

        user_profile = new_user

        user_profile.first_name = self.cleaned_data['first_name']
        user_profile.last_name = self.cleaned_data['last_name']
        # user_profile.company_name = self.cleaned_data['company_name']

        user_profile.save()

        # if self.cleaned_data['profile_part'] == 'profile_part':
        #     profile_part = ProfilePart(user = new_user.get_profile())
        #     profile_part.save()



        return new_user


# ProfilFormset = inlineformset_factory(ProfilePart,
#                                       ProfilePro,
#                                       fields='__all__',
#                                       extra=1,
#                                       can_delete=True)
