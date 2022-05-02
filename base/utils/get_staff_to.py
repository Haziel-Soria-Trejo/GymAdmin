def save_str(staffs:tuple):
    """
    Para guardar la lista de destinos en la base de datos
    necesitamos guardarla como una cadena completa.
    """
    text=''
    for i in staffs:
        text = text + i + ' '
    
    return text[:-1]#eliminamos el espacio final

# NOTE: Posiblemente no sea necesario.
def decode_str(text:str):
    """
    Se pasa la cadena de texto guardada en la base de datos y retorna 
    una lista.
    """
    return text.split(' ')