# Django
from django.shortcuts import render

# Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view

# User
from . import main as operaciones


@api_view(['GET'])
def sum_matrix(request, data_1, data_2):
    """Generate the sum of two matrices

    Args:
        data_1 (str): matrix style [[2,5],[7,3]]
        data_2 (str): matrix style [[7,8],[3,9]]

    Returns:
        matrix style [[9,13],[10,12]]
    
    Raises:
        400: Invalid input
        400: Check the size of the matrix
    """
    
    validation = operaciones.validate_matrix_sum(data_1, data_2)
    
    if not validation[0]:
        return Response({
            'status': 'error',
            'errors': validation[1]
        }, status=400)
    
    data_1, data_2 = validation[1]
    
    result = operaciones.mat_sum(data_1, data_2)
    
    data = {
        'status': 'ok',
        'result': result
    }
    return Response(data, status = 200)


@api_view(['GET'])
def sub_matrix(request, data_1, data_2):
    """Generate the subtraction of two matrices
    
    Args:
        data_1 (str): matrix style [[2,5],[7,3]]
        data_2 (str): matrix style [[7,8],[3,9]]
        
    Returns:
        matrix style [[-5,-3],[4,2]]
    
    Raises:
        400: Invalid input
        400: Check the size of the matrix
    """
    validation = operaciones.validate_matrix_sum(data_1, data_2)
    
    if not validation[0]:
        return Response({
            'status': 'error',
            'errors': validation[1]
        }, status = 400)
    
    data_1, data_2 = validation[1]
    
    result = operaciones.mat_subtraction(data_1, data_2)
    
    data = {
        'status': 'ok',
        'result': result
    }
    return Response(data, status = 200)


@api_view(['GET'])
def escalar_multiply(request, escalar, data):
    """Generate the multiplication of a matrix by a scalar

    Args:
        escalar (str): number
        data (str): matrix style [[2,5],[7,3]]

    Returns:
        matrix style [[4,10],[14,9]]
    
    Raises:
        400: Invalid input
    """
    try:
        escalar = float(escalar)
    except:
        return Response({
            'status': 'error',
            'error': 'Invalid input'
        }, status = 400)
    
    validation = operaciones.validate_matrix(data)
    
    if not validation[0]:
        return Response({
            'status': 'error',
            'errors': validation[1]
        }, status = 400)
    
    data = validation[1]
    
    result = operaciones.mult_escalar(escalar, data)
    
    data = {
        'status': 'ok',
        'result': result
    }
    return Response(data, status = 200)


@api_view(['GET'])
def matrix_multiply(request, data_1, data_2):
    """Generate the multiplication of two matrices

    Args:
        data_1 (str): matrix style [[1,3],[2,0]]
        data_2 (str): matrix style [5,0,1],[3,-2,6]]

    Returns:
        matrix style [[14,-6,19],[10,0,2]]
        
    Raises:
        400: Invalid input
        400: Check the size of the matrix
    """
    validation = operaciones.validate_matrix_mult(data_1, data_2)
    
    if not validation[0]:
        return Response({
            'status': 'error',
            'errors': validation[1]
        }, status = 400)
    
    data_1, data_2 = validation[1]
    
    result = operaciones.mat_multiply(data_1, data_2)
    
    data = {
        'status': 'ok',
        'result': result
    }
    return Response(data, status = 200)


@api_view(['GET'])
def trans_matrix(request, data):
    """Generate transpose from matrix

    Args:
        data (str): matrix style [[1,3],[2,0]]
        
    Returns:
        matrix style [[14,-6,19],[10,0,2]]
        
    Raises:
        400: Invalid input
        400: Check the size of the matrix
    """
    
    validation = operaciones.validate_matrix(data)
    
    if not validation[0]:
        return Response({
            'status': 'error',
            'errors': validation[1]
        }, status = 400)
    
    data = validation[1]
    
    result = operaciones.mat_transpose(data)
    
    data = {
        'status': 'ok',
        'result': result
    }
    return Response(data, status = 200)
    

# [[1,2,5],[6,2,4]]/[[4,7,2],[2,6,3]]