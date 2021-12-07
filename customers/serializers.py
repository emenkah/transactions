from rest_framework import serializers

class FileSerializer(serializers.ModelSerializer):

    
    path = serializers.CharField(max_length = 100)
    # class Meta:
    #     model = Store
    #     fields = [ 'name', 'uuid' ,'created_by', 'created_by_details', 'timezone', 'telephone']
    #     extra_kwargs = {
    #         'created_by': {'write_only': True} 
    #     }

