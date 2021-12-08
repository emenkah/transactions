from rest_framework import serializers

class FileSerializer(serializers.Serializer):

    
    file_path = serializers.CharField(max_length = 100)
    #file_uploaded = serializers.FileField()

    class Meta:
        #fields = ['file_uploaded', "path"]
        fields = ["file_path"]
    # class Meta:
    #     model = Store
    #     fields = [ 'name', 'uuid' ,'created_by', 'created_by_details', 'timezone', 'telephone']
    #     extra_kwargs = {
    #         'created_by': {'write_only': True} 
    #     }

