from enum import Enum

class OrdenEstado(Enum):
    CREADO = 'CREADO'
    PAGADO = 'PAGADO'
    COMPLETADA = 'COMPLETADA'
    CANCELADA = 'CANCELADA'
    
choices = [ (tag, tag.value) for tag in OrdenEstado ]