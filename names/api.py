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
from static_apps.core.tools.functions import show_error

@api_view(['GET'])
def test(request):
    return Response({'message': 'Hello, world!'})


@api_view(['POST'])
def generate_names(request):
    status = 200
    response = {}
    
    try:
        vocals = ['a', 'e', 'i', 'o', 'u']
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        
        data = json.loads(request.body.decode('utf-8'))
        try:
            range_min = int(data['range_min'])
            range_max = int(data['range_max'])
            quantity = int(data['quantity'])
            merge = int(data['merge'])
        except Exception as e:
            status = 400
            response = {'message': 'Invalid data. All parameters need to be integers.'}
            return Response(response, status=status)
        
        vocals_seg = 0
        const_seg = 0
        names = []
        for _ in range(quantity):
            name = ''
            length = random.randint(range_min, range_max)
            for x in range(length):
                n = random.randint(1, 100)
                if n <= merge and vocals_seg > 1:
                    n += 100
                if n >= merge and const_seg > 1:
                    n -= 100
                if n <= merge:
                    name += random.choice(vocals)
                    vocals_seg += 1
                    const_seg = 0
                else:
                    name += random.choice(consonants)
                    const_seg += 1
                    vocals_seg = 0
            
            names.append(name.title())
        
        response['names'] = names
    except Exception as e:
        error = show_error(e, send_email = True)
        print(error)
        response['message'] = error
        status = 400
    return Response(response, status=status)