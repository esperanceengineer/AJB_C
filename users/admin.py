from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms


from users.models import MyUser, Profil, TypeActivte,TypeSpeculation
# Register your models here.
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'credits','profile')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'is_active', 'is_admin', 'status','situation','photo')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('name','email', 'is_admin', 'profil','typeActivte','photo')
    list_filter = ('is_admin', )
    fieldsets = (
        (None, {'fields': ('email','password',)}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin','is_active')}),
        ('Site Info', {'fields': ('credits', 'status','situation')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','email', 'password1', 'password2', 'profil','typeActivte','status','situation','photo'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'active')

class TypeActiviteAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'active','description')

class TypeSpeculationAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'active','activite','description')

#admin.site.unregister(Group)
admin.site.unregister(Group)
admin.site.register(MyUser, UserAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(TypeActivte, TypeActiviteAdmin)
admin.site.register(TypeSpeculation, TypeSpeculationAdmin)