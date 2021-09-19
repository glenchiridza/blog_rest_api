from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter

from users.models import User, Writer, Subscriber


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'is_writer', 'is_subscriber')


class CustomRegisterSerializer(RegisterSerializer):
    is_writer = serializers.BooleanField()
    is_student = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_writer', 'is_subscriber',)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username'),
            'password1': self.validated_data.get('password1'),
            'password2': self.validated_data.get('password2'),
            'email': self.validated_data.get('email'),
            'is_writer': self.validated_data.get('is_writer'),
            'is_subscriber': self.validated_data.get('is_subscriber'),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_writer = self.cleaned_data.get('is_writer')
        user.is_subscriber = self.cleaned_data.get('is_subscriber')
        user.save()

        # determine the type of user to create

        if user.is_subscriber:
            subscriber = Subscriber.objects.create(id=user.id, user=user)
            subscriber.save()
        if user.is_writer:
            writer = Writer.objects.create(id=user.id, user=user)
            writer.save()

        adapter.save_user(request, user, self)

        return user
