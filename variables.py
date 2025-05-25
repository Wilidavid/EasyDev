import json
opciones=[['Lista de problemas'], ['Opciones de cuenta'], ['amongus'] ,['Salir']] #meter funciones
archivo_temporal_temporasitario_numero_uno_ppunto_iuno_version_2 = open('cuentas.json')
cuentas=json.load(archivo_temporal_temporasitario_numero_uno_ppunto_iuno_version_2)
archivo_temporal_temporasitario_numero_uno_ppunto_iuno_version_2.close()

translator = ['Facil', 'Medio', 'Dificil', 'Avanzado']

usuario_actual=None
k = open('archivos.json')
archivos=json.load(k)
k.close()