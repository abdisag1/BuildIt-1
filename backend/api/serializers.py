from rest_framework import serializers
from builder.models import Pages, Templetes, Catagories

class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields ='__all__'
class TempletesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Templetes
        fields ='__all__'
class CatagoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagories
        fields ='__all__'