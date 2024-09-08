from django.contrib.auth.backends import ModelBackend
from .models import CustomUser
from Patients.models import PatientProfile,visitor
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password  
from .models import CustomUser
from Patients.models import PatientProfile,visitor 

class PhoneNumberBackend(ModelBackend):
    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        try:
          
            Visitor = visitor.objects.get(phone_number=phone_number)
            user = visitor.user 
            if user.check_password(password):
                return user 
            else:
                return None  
        except visitor.DoesNotExist:
           
            user = CustomUser.objects.create(
                username=phone_number,  
                email=None,  
                password=make_password(password), 
            )

            Visitor = visitor.objects.create(
                user=user,
                phone_number=phone_number,
            )
            
           
            return user

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
