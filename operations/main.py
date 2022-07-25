def delete_spaces(text):
    return text.replace(' ', '')


def get_mat(text):
    text = delete_spaces(text)
    if not (text.startswith('[[') and text.endswith(']]')):
        raise Exception('Invalid input')
    if '],[' not in text:
        raise Exception('Invalid input')
    text = text[1:-1].replace('],[', '-|-').replace('[','').replace(']', '').split('-|-')
    mat = []
    for i in range(len(text)):
        col = text[i].split(',')
        for j in range(len(col)):
            try:
                col[j] = float(col[j])
            except:
                raise Exception('Invalid input')
        mat.append(col)
    return mat


def validate_matrix_sum(data_1, data_2):
    try:
        data_1 = get_mat(data_1)
        data_2 = get_mat(data_2)
        if len(data_1) != len(data_2):
            return False, ['Check the size of the matrix']
        try:
            for i in range(len(data_1)):
                if len(data_1[i]) != len(data_2[i]):
                    return False, ['Check the size of the matrix']
        except:
            return False, ['Check the size of the matrix']
    except:
        return False, ['Invalid input']
    return True, [data_1, data_2]


def validate_matrix_mult(data_1, data_2):
    try:
        data_1 = get_mat(data_1)
        data_2 = get_mat(data_2)
        rows_1 = len(data_1)
        rows_2 = len(data_2)
        print(f'data_1: {data_1}')
        print(f'data_2: {data_2}')
        print(f'rows_1: {rows_1}')
        print(f'rows_2: {rows_2}')
        print()
        try:
            for i in range(rows_1):
                print(f'len(data_1[{i}])({len(data_1[i])}) != rows_2({rows_2}): {len(data_1[i]) != rows_2}')
                if len(data_1[i]) != rows_2:
                    return False, ['Check the size of the matrix']
        except:
            return False, ['Check the size of the matrix']
    except:
        return False, ['Invalid input']
    return True, [data_1, data_2]


def validate_matrix(data):
    try:
        data = get_mat(data)
    except:
        return False, ['Invalid input']
    return True, data


def mat_sum(mat_1, mat_2):
    result = []
    for i in range(len(mat_1)):
        result.append([])
        for j in range(len(mat_1[i])):
            result[i].append(mat_1[i][j] + mat_2[i][j])
        
    return result


def mat_subtraction(mat_1, mat_2):
    result = []
    for i in range(len(mat_1)):
        result.append([])
        for j in range(len(mat_1[i])):
            result[i].append(mat_1[i][j] - mat_2[i][j])
        
    return result


def mult_escalar(escalar, mat):
    result = []
    for i in range(len(mat)):
        result.append([])
        for j in range(len(mat[i])):
            result[i].append(mat[i][j] * escalar)
        
    return result


def mat_multiply(mat_1, mat_2):
    res = []
    for i in range(len(mat_1)):
        res.append([])
        for j in range(len(mat_2[0])):
            res[i].append(0)
            for k in range(len(mat_2)):
                res[i][j] += mat_1[i][k] * mat_2[k][j]
    return res


def mat_transpose(mat):
    res = []
    for i in range(len(mat[0])):
        res.append([])
        for j in range(len(mat)):
            res[i].append(mat[j][i])
    return res