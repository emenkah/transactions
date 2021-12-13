from rest_framework import serializers

class FileSerializer(serializers.Serializer):

    file_path = serializers.CharField(max_length = 100)
    credit_card_check = serializers.BooleanField(default = False)

    class Meta:
        
        fields = ["file_path"]
  

