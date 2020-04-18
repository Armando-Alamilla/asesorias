"""Users serializers."""

# Django imports
from django.contrib.auth import authenticate, password_validation
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

# Models
from asesorias.users.models import User, StudentProfile, TeacherProfile


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )


class UserSignUpSerializer(serializers.Serializer):
    """User signup serializer.
    
    Handle signup data validation and user/profile creation.
    """
    # Email
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Username
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    # Is teacher
    is_teacher = serializers.BooleanField()

    def validate(self, data):
        """Verify password match."""
        passwd = data['password']
        passwd_conf = data['password_confirmation']

        if passwd != passwd_conf:
            raise serializers.ValidationError('Password don\'t match.')

        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop('password_confirmation')

        user = User.objects.create_user(**data, is_verified=False)

        if data['is_teacher'] == True:
            TeacherProfile.objects.create(user=user)
        else:
            StudentProfile.objects.create(user=user)

        self.send_confirmation_email(user)
        return user

    def send_confirmation_email(self, user):
        """Send account verification link to user."""
        verification_token = self.gen_verification_token(user)
        
        subject = 'Verify your account to start using asesorias.'
        from_email = 'Asesorias <noreply@aztech-4775.com>'
        content = render_to_string(
            'emails/users/account_verification.html',
            {'token': verification_token, 'user': user}
        )

        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()

    def gen_verification_token(self, user):
        """Create JWT token that user can use to verify its account."""
        return 'abc'


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.
    
    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Verify credentials."""
        user = authenticate(
            username=data['email'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError('Invalid credentials.')

        if not user.is_verified:
            raise serializers.ValidationError('Account is not active yet.')

        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrive new token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
