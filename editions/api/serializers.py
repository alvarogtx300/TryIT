from django.contrib.auth.models import User
from rest_framework import serializers

from editions.models import Edition, Company, Session, Speaker


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class EditionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edition
        fields = ('url', 'year', 'title', 'slogan', 'description', 'start_date', 'end_date')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ('name', 'bio', 'picture')


class SessionSerializer(serializers.ModelSerializer):
    speakers = SpeakerSerializer(many=True, read_only=True)
    company = serializers.SerializerMethodField('getCompany')

    class Meta:
        model = Session
        fields = ('title', 'start_date', 'end_date', 'description', 'url', 'company', 'speakers')

    def getCompany(self, session):
        companiesString = ""
        if session.companies.all():
            for sesi in session.companies.all():
                companiesString += sesi.name+", "
        return companiesString[:-2]


class YearSessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('code', 'title', 'start_date')
