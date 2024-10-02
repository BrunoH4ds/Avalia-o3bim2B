while True:  
  try:
          numero_participantes = int(input('digite quantos participaram da reuniao: '))
          if numero_participantes <= 0:
              print('O número de participantes não pode ser menor ou igual a 0')
          else:
              if numero_participantes <= 3:
                  print('A sala ideal é a sala pequena')
                  exit()
              elif numero_participantes > 3 and numero_participantes <= 10:
                  print('A sala ideal é a sala média')
                  exit()
              else:
                  print('A sala ideal é a sala grande')
                  exit()

  except ValueError:
    print('Digite apenas números')
