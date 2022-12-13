from rest_framework import serializers

from deliver.models import Order, Box


class BoxSerializer(serializers.ModelSerializer):
    goods = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )


    class Meta:
        model = Box
        fields = ['name', 'goods']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    boxes = BoxSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['name', 'boxes']


