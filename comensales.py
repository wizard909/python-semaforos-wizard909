import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

platosDisponibles = 0
platos = threading.Semaphore(3)
dormirCocinero = threading.Semaphore(1)


class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    global dormirCocinero
    global platos

    while (True):
      dormirCocinero.acquire()

      logging.info('Reponiendo los platos...')
      platosDisponibles = 3
      logging.info('Platos reponidos')

    
class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    global platos
    global dormirCocinero

  
    if platos._value > 0 and platosDisponibles > 0:
      platos.acquire() 
      platosDisponibles -= 1
      logging.info(f'Que rico ,Quedan {platosDisponibles} platos')
    else if platos._value == 0 and platosDisponibles == 0:
        dormirCocinero.release()
    else:
      time.sleep(2)
      

      

Cocinero().start()
for i in range(5):
  Comensal(i).start()