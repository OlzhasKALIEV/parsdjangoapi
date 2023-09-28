from rest_framework import serializers

from parsapi.models import CatalogPatrioticMusic


class MuseumFundRFSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogPatrioticMusic
        fields = "__all__"
