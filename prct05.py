#!/usr/bin/python
#!encoding: UTF-8
import sys

argumentos=sys.argv[1:]
print argumentos
if(len(argumentos)==1):
  n=int(argumentos[0])
else:
  print "Introduzca el número de intervalos (n>0): "
  n=int(raw_input())

if (n>0):
  PI35 = 3.1415926535897931159979634685441852
  sumatorio=0.0
  ini=0
  intervalos=1.0/float(n)
  for i in range(n):
    x_i=((i+1) - 1.0/2.0)/n
    fx_i=4.0/(1.0 + x_i*x_i)
    print "Subintervalo: [",ini,",",ini+intervalos,"] x_i: ",x_i," fx_i:", fx_i
    ini+=intervalos
    sumatorio+=fx_i
  valor_pi=sumatorio/n
  print "El valor de aproximado de PI es: ",valor_pi
  print "El valor de PI con 35 decimales es: %10.35f" % PI35
else:
  print "El valor de los intervalos debe ser positivo"

