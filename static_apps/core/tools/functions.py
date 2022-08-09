def show_error(e, send_email = False):
    import os
    import datetime
    exc_type, exc_obj, exc_tb = os.sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)
    rute, file_name = fname[0], fname[1]
    fname = file_name
    file = rute + '/' + fname
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    
    error = f'ERROR INFO\nTipo: {exc_type}\nArchivo: {file}\nlinea: {exc_tb.tb_lineno}\nError: {e}\nFecha: {now}'
    
    if send_email:
        from static_apps.core.emails.emails import EmailError
        email = EmailError(error)
        email.send()
    return error