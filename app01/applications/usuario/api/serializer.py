from rest_framework import serializers

from django.contrib.auth.models import User

from applications.base.utils import validarRut
from applications.usuario.models import Colaborador, UsuarioEmpresa

class UsuarioSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    first_name = serializers.CharField(max_length=150, required=True)
    last_name = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(max_length=254, required=True)
    password = serializers.CharField(max_length=128, required=True)

class ColaboradorSerializers(serializers.ModelSerializer):
    user = UsuarioSerializers(read_only=True)

    class Meta:
        model = Colaborador
        fields = (
            'col_extranjero',
            'col_rut',
            'col_sexo',
            'col_fechanacimiento',
            'col_estadocivil',
            'col_direccion',
            'pais',
            'region',
            'comuna',
            'col_tipousuario',
            'col_profesion',
            'col_titulo',
            'col_formapago',
            'banco',
            'col_tipocuenta',
            'col_cuentabancaria',
            'col_usuarioactivo',
            'col_licenciaconducir',
            'col_tipolicencia',
            'col_fotousuario',
            'user',
        )

    def validate(self, data):
        if not validarRut(data['col_rut']):
            raise serializers.ValidationError(f'El rut del cliente es invalido')
        return data

    def create(self, validated_data):
        #usuario_data = validated_data.pop('user')
        usuario_data = self.initial_data['user']
        usuario = User.objects.create_user(**usuario_data)
        colaborador = Colaborador.objects.create(user=usuario, **validated_data)
        return colaborador

class UsuarioEmpresaDatosLaboralesSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsuarioEmpresa
        fields = (
            'user',
            'empresa',
            'cargo',
            'centrocosto',
            'sucursal',
            'ue_tipotrabajdor',
            'ue_tipocontrato',
            'ue_fechacontratacion',
            'ue_fecharenovacioncontrato',
            'ue_horassemanales',
            'ue_asignacionfamiliar',
            'ue_cargasfamiliares',
            'ue_montoasignacionfamiliar',
            'ue_sueldobase',
            'ue_gratificacion',
            'ue_tipogratificacion',
            'ue_comiciones',
            'ue_porcentajecomicion',
            'ue_semanacorrida',
        )

        extra_kwargs = {
            'user': {'required': False},
            'empresa': {'required': False},
            'cargo': {'required': False},
            'centrocosto': {'required': False},
            'sucursal': {'required': False},
        }

class UsuarioEmSerializers(serializers.Serializer):
    usuario_empresa = UsuarioEmpresaDatosLaboralesSerializers(read_only=True)
    class Meta:
        model = User
        fields = ('__all__')

class DatosPrevisionalesUsuarioEmpresaDatosLaboralesSerializers(serializers.Serializer):
    user = serializers.IntegerField(required=True)
    afp = serializers.IntegerField(required=True)
    salud = serializers.IntegerField(required=True)
    ue_ufisapre = serializers.CharField(max_length=100, required=True)
    ue_funisapre = serializers.CharField(max_length=100, required=True)
    ue_cotizacion = serializers.FloatField(required=True)
