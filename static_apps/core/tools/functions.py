def show_error(e, send_email = False):
    import os
    import datetime
    info_exc = os.sys.exc_info()
    exc_type, exc_obj, exc_tb = info_exc
    file = exc_tb.tb_frame.f_code.co_filename
    function_data = str(exc_tb.tb_frame).split()
    function_data = function_data[-1][:-1]
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    
    error = f'ERROR INFO\nTipo: {exc_type}\nArchivo: {file}\nFuncion: {function_data}\nLinea: {exc_tb.tb_lineno}\nError: {e}\nFecha: {now}'
    
    if send_email:
        from static_apps.core.emails.emails import EmailError
        email = EmailError(error)
        email.send()
    return error