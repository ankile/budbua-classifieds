from rest_framework import serializers


def try_cast_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise serializers.ValidationError(f"Minimum bid must be an positive integer.")