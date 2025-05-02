from rest_framework import serializers
from usuario.models import Usuario
import re

class UsuarioSerializer(serializers.ModelSerializer):
    
    # Validación personalizada para el nombre de usuario
    def validate_nombre_usuario(self, value):
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
            raise serializers.ValidationError("El nombre solo puede contener letras y espacios.")
        return value

    # Validación personalizada para el correo
    def validate_correo(self, value):
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$', value):
            raise serializers.ValidationError("Ingrese un correo válido.")
        return value

    # Validación personalizada para la contraseña
    def validate_contraseña(self, value):
        if not re.match(r'^[a-zA-Z0-9@#$%^&+=!?*-]{8,20}$', value):
            raise serializers.ValidationError(
                "La contraseña debe tener entre 8 y 20 caracteres, incluyendo letras, números y símbolos."
            )
        return value

    class Meta:
        model = Usuario
        fields = '__all__'

    # Sobrescribe el método create para utilizar set_password
    def create(self, validated_data):
        contraseña = validated_data.pop('contraseña')  # Obtener la contraseña antes de crear el usuario
        usuario = Usuario.objects.create(**validated_data)
        usuario.set_password(contraseña)  # Utiliza set_password para encriptar la contraseña
        usuario.save()
        return usuario

    # Sobrescribe el método update para utilizar set_password al actualizar la contraseña
    def update(self, instance, validated_data):
        contraseña = validated_data.pop('contraseña', None)  # Obtén la nueva contraseña si existe
        if contraseña:
            instance.set_password(contraseña)  # Usa set_password para encriptar la nueva contraseña
        return super().update(instance, validated_data)
