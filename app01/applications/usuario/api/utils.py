
def get_key_colaborador_data():
    extra_kwargs = {
                    'user_id': 'required',
                    'cargo_id': 'required',
                    'centrocosto_id': 'required',
                    'sucursal_id': 'required',
                    'empresa_id': 'required',
                    'ue_tipotrabajdor': 'required',
                    'ue_fechacontratacion': 'required',
                    'ue_fecharenovacioncontrato': 'required',
                    'ue_horassemanales': 'required',
                    'ue_asignacionfamiliar': 'required',
                    'ue_cargasfamiliares': 'required',
                    'ue_montoasignacionfamiliar': 'required',
                    'ue_sueldobase': 'required',
                    'ue_gratificacion': 'required',
                    'ue_tipogratificacion': 'required',
                    'ue_comiciones': 'required',
                    'ue_porcentajecomicion': 'required',
                    'ue_semanacorrida': 'required',
                }
    keys = extra_kwargs.keys()
    return list(keys)