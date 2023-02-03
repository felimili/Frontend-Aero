cls
Echo off
Echo+
Echo+
Echo ***********************************
Echo * FACTURACION ELECTRONICA - Paso 2*
Echo ***********************************
Echo+
Echo+


Echo Introduzca el nombre del archivo sin extension

Set /p var1=

REM Verifica que se introduzcan los parametros necesarios
REM Si falta alguno, salta a la etiqueta falto_parametro

if .%var1% ==. goto falto_parametro


REM Verifica la existencia de los archivos necesarios
REM Si falta alguno, salta a la etiqueta correspondiente

if not exist respuesta.crt goto falta_certAFIP
if not exist privkey.pem goto falta_privkey
if not exist openssl.exe goto falta_openssl
if not exist openssl.cnf goto falta_opencnf

Echo OBTENIENDO CERTIFICADO DE SEGURIDAD .CRT
Echo ----------------------------------------
Echo+
openssl pkcs12 -export -in respuesta.crt -inkey privkey.pem -out %var1%.p12
Echo+
Echo+
Echo -----------------------------------------------------
Echo  Se ha creado correctamente el certificado %var1%.P12
Echo -----------------------------------------------------
Echo+
Echo off
pause
goto salir

:falto_parametro
Echo +++++++++++++++++++++++++++++++++++++
Echo  ATENCION: 
Echo +
Echo   Debe indicar el nombre del archivo. Se ha cancelado la generacion
Echo +++++++++++++++++++++++++++++++++++++
Echo +
pause
goto salir


:falta_certAFIP
Echo+++++++++++++++++++++++++++++++++++++
Echo ATENCION: 
Echo+
Echo  No se encuentra el archivo respuesta.crt. Se ha cancelado la generacion
Echo+++++++++++++++++++++++++++++++++++++
Echo+
pause
goto salir

:falta_privkey

Echo+++++++++++++++++++++++++++++++++++++
Echo ATENCION: 
Echo+
Echo  No se encuentra el archivo privkey.pem. Se ha cancelado la generacion
Echo+++++++++++++++++++++++++++++++++++++
Echo+
pause
goto salir


:falta_openssl

Echo+++++++++++++++++++++++++++++++++++++
Echo ATENCION: 
Echo+ 
Echo  No se encuentra el archivo openssl.exe. Se ha cancelado la generacion
Echo+++++++++++++++++++++++++++++++++++++
Echo+
pause
goto salir

:falta_opencnf

Echo+++++++++++++++++++++++++++++++++++++
Echo ATENCION: 
Echo+ 
Echo  No se encuentra el archivo openssl.cnf. Se ha cancelado la generacion
Echo+++++++++++++++++++++++++++++++++++++
Echo+
pause

:salir