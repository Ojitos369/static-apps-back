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

@api_view(['GET'])
def test(request):
    return Response({'message': 'Hello, world!'})


@api_view(['GET', 'POST'])
def generate_names(request):
    state = 200
    response = {}
    
    vocals = ['aeiou']
    consonants = ['bcdfghjklmnpqrstvwxyz']
    
    data = json.loads(request.body.decode('utf-8'))
    range_min = int(data['range_min'])
    range_max = int(data['range_max'])
    quantity = int(data['quantity'])
    merge = int(data['merge'])
    
    names = []
    for _ in range(quantity):
        name = ''
        length = random.randint(range_min, range_max)
        for __ in range(length):
            n = random.randint(1, 100)
            if n <= merge:
                name += random.choice(vocals)
            else:
                name += random.choice(consonants)
        
        names.append(name.title())
    
    response['names'] = names
    return Response(response, status=state)