class ReservationEnum(object):
    PENDIENTE = 0
    ENTREGADO = 1
    RECHAZADO = 2

    RESERVATION_STATES = (
        (PENDIENTE, 'pendiente'),
        (ENTREGADO, 'entregado'),
        (RECHAZADO, 'rechazado'),
    )


class LoanEnum(object):
    VIGENTE = 0
    CADUCADO = 1
    RECIBIDO = 2
    PERDIDO = 3

    RESERVATION_STATES = (
        (VIGENTE, 'vigente'),
        (CADUCADO, 'caducado'),
        (RECIBIDO, 'recibido'),
        (PERDIDO, 'perdido'),
    )

