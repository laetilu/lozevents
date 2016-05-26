from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.models import inlineformset_factory



from userena.forms import SignupForm
from models import ProfilePart, ProfilePro
from lozapp.models import Categorie, Address

class SignupFormExtra(SignupForm):
    # # company_name = forms.CharField(label=_(u'Company name'),
    # #                                max_length=200,
    # #                                required=False)
    #

    first_name = forms.CharField(label=_(u'First name'),
                                 max_length=30,
                                 required=False)

    last_name = forms.CharField(label=_(u'Last name'),
                                max_length=30,
                                required=False)
    street = forms.CharField(max_length=45)
    zipcode = forms.CharField(max_length=5)
    city =  forms.CharField(max_length=100)
    favorite_categories = forms.ModelMultipleChoiceField(queryset=Categorie.objects.all())



    def save(self):
        new_user = super(SignupFormExtra, self).save()

        user_profile = new_user.profile_part
        user_profile.first_name = self.cleaned_data['first_name']
        user_profile.last_name = self.cleaned_data['last_name']

        address = Address.objects.create(street=self.cleaned_data['street'],
                                            zipcode=self.cleaned_data['zipcode'],
                                            city=self.cleaned_data['city'])

        user_profile.address = address

        for g in self.cleaned_data['favorite_categories']:
            print g
            user_profile.favorite_categories.add(g)

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
