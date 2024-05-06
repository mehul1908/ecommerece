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

