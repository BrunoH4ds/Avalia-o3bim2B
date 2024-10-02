def function_Encontrar_A_Sala(numero_participantes):
    try:
          if numero_participantes <= 0:
              return 'O número de participantes não pode ser menor ou igual a 0'
          else:
              if numero_participantes <= 3:
                  return 'A sala ideal é a sala pequena'
              elif numero_participantes > 3 and numero_participantes <= 10:
                  return 'A sala ideal é a sala média'
              else:
                  return 'A sala ideal é a sala grande'

    except ValueError:
        return 'Digite apenas números'
