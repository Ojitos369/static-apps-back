# Python
import os
import json
import random

# Django
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

# Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view

# User
from static_apps.core.tools.errors import show_error
from static_apps.core.tools.functions import print_line_center, currency_convertions


@api_view(['POST'])
def convertir_precios(request):
    status = 200
    response = {}
    try:
        data = json.loads(request.body.decode('utf-8'))
        amount = data['amount'] if 'amount' in data else '1'
        c_from = data['from'].upper() if 'from' in data else ['USD']
        c_to = data['to'] if 'to' in data else ['MXN']
        conversiones = {}
        for c in c_to:
            c = c.upper()
            try:
                results = currency_convertions(amount, c_from, c)
                conversiones[c] = results
            except Exception as e:
                # error = show_error(e, send_email=False)
                # print_line_center(error)
                conversiones[c] = f'No se puede hacer la conversion {c_from}-{c}. Revise que las monedas sean correcta'
        response = {
            'origin': c_from,
            'amount': amount,
            'results': conversiones
        }
        print(response)
    except Exception as e:
        error = show_error(e)
        print_line_center(error)
        response['message'] = str(e)
        status = 400
    return Response(response, status=status)


