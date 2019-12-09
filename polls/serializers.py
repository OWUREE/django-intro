from rest_framework import serializers

from polls.models import DustBin

# Serializers define the API representation.
class DustBinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DustBin
        fields = ['type', 'level']

    def create(self, validated_data):
        level = validated_data.get('level', None)
        if level == 0:
            validated_data['comment'] = "Bin Empty"
        elif level > 0 and level < 50:
            validated_data['comment'] = "Bin not Full"
        elif level > 50 and level < 75:
            validated_data['comment'] = "Bin almost full"
        elif level > 75 and level < 90:
            validated_data['comment'] = "Bin full"
        else:
            validated_data['comment'] = "Bin overflow"
        
        type_ = validated_data.get('type', None)
        try:
            last_entry_level = DustBin.objects.filter(type=type_).last().level
            if last_entry_level is not None and level < last_entry_level:
                validated_data['has_been_emptied'] = True
        except AttributeError:
            # When no values for previous data exist the last_entry_level query fails
            pass
        return DustBin.objects.create(**validated_data)
