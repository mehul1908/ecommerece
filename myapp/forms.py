from . import models
from django import forms

utype=(('buyer',"Buyer"),('seller','Seller'))

class UserMasterForm(forms.ModelForm):
    class Meta:
        model=models.UserMaster
        fields="__all__"
        widgets={
            'password':forms.PasswordInput(),
            'usertype':forms.Select(choices=utype)
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=models.UserProfile
        fields="__all__"

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model=models.ProductCategory
        fields='__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields='__all__'

class ComplaintForm(forms.ModelForm):
    class Meta:
        model=models.Complaint
        fields=['compdesc',]
        widgets={
            'compdesc':forms.Textarea(attrs= {'name':'compdesc','rows':5,'cols':30}),
        }

class ComplaintResponseForm(forms.ModelForm):
    class Meta:
        model=models.Complaint
        fields="__all__"
        widgets={
            'compdesc':forms.Textarea(attrs= {'name':'compdesc','rows':5,'cols':30}),
            'response':forms.Textarea(attrs= {'name':'response','rows':5,'cols':30}),        
        }