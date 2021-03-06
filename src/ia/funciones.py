import datetime

from ia.models import CiaConsecutivo, DocRep
from rest_framework.exceptions import APIException


class InvalidAPIQuery(APIException):
	status_code = 400
	default_detail = 'An invalid query parameter was provided'


def consecutivo_doc(cia_id, tipo_doc):
	"""
    Trae el consecutivo por tipo de documento
    :param cia_id: 
    :param tipo_doc: 
    :return: diccionario retorno con error, numero y status
    """

	retorno = {'error': '', 'numero': 0, 'status': 1}
	numero = 0
	try:
		retorno = {'error': '', 'numero': 0, 'status': 1}
		numero = 0
		# error = 'error en la funcion'
		while True:

			ciaconsecutivo = CiaConsecutivo.objects.filter(
				cia_id__exact=cia_id, tipo_documento__exact=tipo_doc).first()

			if ciaconsecutivo:
				print("ciaconsecutivo")
				print("Encontro el registro en ciaconsecutivo")
				print(ciaconsecutivo)
				print(ciaconsecutivo.cia_id)
				print(ciaconsecutivo.tipo_documento)
				print(ciaconsecutivo.numero)
				numero = ciaconsecutivo.numero
				numero += 1
				ciaconsecutivo.numero = numero
				ciaconsecutivo.save()
			else:
				print("ciaconsecutivo")
				print("Va a crear el registro en ciaconsecutivo")
				numero = 1
				cc = CiaConsecutivo.objects.create(
					cia_id=cia_id,
					tipo_documento=tipo_doc,
					numero=numero
				)
				cc.save()

			registros = DocRep.objects.filter(
				cia_id__exact=cia_id, tipo_documento__exact=tipo_doc, numero__exact=numero).count()

			print("registros conseguidos")
			print(registros)
			print("numero")
			print(numero)
			if registros < 1:
				break

		# val1 = 0
		# val2 = 100/val1
		# if funciondiv(1, 1, val3, error) == -1:
		#     raise InvalidAPIQuery(
		#          'Funcion: consecutivo_doc. Error Buscando el Número consecutivo. ' + str(e))

		retorno['numero'] = numero
		var3 = 10 / 0

		return retorno

	except Exception as e:
		print("status en la exc")
		print(retorno['status'])
		error = "Error en la Funcion consecutivo_doc. " + str(e)

		retorno['error'] = error
		retorno['status'] = -1
		#  {'error': error, 'numero': 0, 'status': -1}
		print("error en la funcion consecutivo_doc..........")
		print(error)
		print("numero en la exc")
		print(numero)
		# retorno.error = error
		# retorno.status = -1
		return retorno

		# print("Exception")
		# print(str(e))
		# raise InvalidAPIQuery(
		#          'Funcion: consecutivo_doc. Error Buscando el Número consecutivo. ' + str(e))


def funciondiv(val1, val2, division, error):
	"""
	Funcion para dividir val1 por val2
	:param val1: 
	:param val2: 
	:param division: 
	:param error: 
	:return: 
	"""
	try:
		division = val / val2
		return division

	except Exception as e:
		error = 'Funcion: funciondiv. En la division. ' + str(e)
		return -1
		# raise InvalidAPIQuery(
		#          'Funcion: funciondiv. En la division. ' + str(e))


def strToDatetime(strFecha, fmt="%Y-%m-%d %H:%M:%S"):
	try:
		# if fmt is None:
		#     fmt = "%Y-%m-%d %H:%M:%S.%f"

		dt = datetime.datetime.strptime(strFecha, fmt)
		return dt
	except Exception as e:
		raise e


def strToBoolean(strValor):
	return strValor.lower() in ("yes", "true", "t", "1")


def midivision(val1, val2):
	return val1 / val2
