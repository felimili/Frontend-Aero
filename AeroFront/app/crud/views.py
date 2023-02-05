from django.shortcuts import render, redirect, HttpResponse
from django.core.files import File
from django.http import FileResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from typing import List

from .forms import CustomUserCreationFrom, LoginForm, Usuario, Avion, Vuelo, Uploads
import requests, os
import json, datetime,zipfile
import mimetypes



# Create your views here.


def inicio(request):
    try:
        request.COOKIES['token']
    except:
        return redirect ('login') 
        
    return render (request, 'base.html')   

            
def me2():
    
            
    tk = "Bearer " + token
    reqUrl = "http://127.0.0.1:8080/api/me"

    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Authorization": tk,
    "Content-Type": "application/x-www-form-urlencoded" 
    }

    payload = tk
    #response = requests.request("GET", reqUrl, headers=headersList)
    
    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    
    if response.status_code == 401:
        state = False
        return (state)
    
    if response.status_code == 400:
        state = False
        return (state) 
    state = True
    return (state)

def logout(request):
    form = LoginForm()
    resp = render (request, 'login.html', {'form': form} )
    resp.delete_cookie('token')
    return resp


def login(request):
    
    global token
    
    url = "http://127.0.0.1:8080/api/login"
    HEADERS = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Content-Type": "application/x-www-form-urlencoded" 
              }

    form = LoginForm()

    if request.method == 'POST':
        
        payload = {"username": str(request.POST['username']), "password": str(request.POST['password'])}
        
                
        response = requests.request("POST", url, data=payload,  headers=HEADERS)
        
        
        token = str(response.text[17:-24])
             
               

        if response.status_code == 200:
            resp = render (request,'base.html')
            resp.set_cookie('token',token, max_age=60)
            return resp
            

        if response.status_code == 400:
            messages.error(request, 'El usuario no existe')
            
            
        if response.status_code == 401:
            messages.warning(request, 'Credenciales de autenticas invalidas')
        
           

    return render (request, 'login.html', {'form': form})

def altauser(request):
    try:
        request.COOKIES['token']
    except:
        return redirect ('login') 
    
    import requests
    url = "http://127.0.0.1:8080/api/user/"
    HEADERS = {
        "Content-Type": "application/json"
            }

    form = Usuario()

    if request.method == 'POST':
        payload = {"username": str(request.POST['username']) , "password": str(request.POST['password']),"nombre": str(request.POST['nombre']),"apellido": str(request.POST['apellido']),"email": str(request.POST['email'])}
        response = requests.post(url, headers=HEADERS, json= payload)

        if response.status_code == 201:
            print('ok')
            print(response)
            return redirect ('login')

        else:
            print('no ok')
            print(response)
    return render (request, 'alta.html', {'form': form})   



def usuarios(request):
    try:
        request.COOKIES['token']
    except:
        return redirect ('login')
    
    
    if request.method == 'GET':

        users = Usuario()

        url = 'http://127.0.0.1:8080/api/user/'
        response = requests.get(url)
       
        users  = json.loads(response.content)
       
        return render (request, 'usuarios.html', {'users' : users})   


def editar(request,id):
    try:
        request.COOKIES['token']
    except:
        return redirect ('login')
        
    if request.method == 'GET':

        users = Usuario()

        url = 'http://127.0.0.1:8080/api/user/'+str(id)
        response = requests.get(url)
       
        users  = json.loads(response.content)
       
        return render (request, 'editar.html', {'users' : users})  
        


    if request.method == 'POST':
        
        url = "http://127.0.0.1:8080/api/user/"+str(id)
        
        HEADERS = {
        "Content-Type": "application/json"
            }

        payload = {"username": str(request.POST['username']) , "password": str(request.POST['password']),"nombre": str(request.POST['nombre']),"apellido": str(request.POST['apellido']),"email": str(request.POST['email'])}
        response = requests.put(url, headers=HEADERS, json= payload)
        if response.status_code == 200:
            return redirect('usuarios') 

        else:
            return redirect('inicio') 

 
    

def eliminar(request,id):

    try:
        request.COOKIES['token']
    except:
        return redirect ('login')

    users = Usuario()

    if request.method == 'GET':
               
        url= 'http://127.0.0.1:8080/api/user/'+str(id)

        response = requests.delete(url)

    return redirect('usuarios')       

def aviones(request):

    try:
        request.COOKIES['token']
    except:
        return redirect ('login')

    if request.method == 'GET':

        planes = Avion()

        url = 'http://127.0.0.1:8080/api/plane/'
        response = requests.get(url)
       
        planes  = json.loads(response.content)
       
        return render (request, 'aviones.html', {'planes' : planes})

def alta_avion(request):

    try:
        request.COOKIES['token']
    except:
        return redirect ('login')

    
    url = "http://127.0.0.1:8080/api/plane/"
    HEADERS = {
        "Content-Type": "application/json"
            }

    planes = Avion()
    
    if request.method == 'POST':
        payload = {"matricula": str(request.POST['matricula']), "marca": str(request.POST['marca']),"modelo": str(request.POST['modelo'])}
        
        response = requests.post(url, headers=HEADERS, json= payload)
        if response.status_code == 201:
            return redirect('aviones') 
        
        else:
            return redirect('aviones')

    return render (request, 'altaavion.html', {'planes': planes })


def eliminar_avion(request,id):

    try:
        request.COOKIES['token']
    except:
        return redirect ('login')

    planes = Avion()

    if request.method == 'GET':
               
        url= 'http://127.0.0.1:8080/api/plane/'+str(id)

        response = requests.delete(url)

    return redirect('aviones')  


def editar_avion(request,id):

    try:
        request.COOKIES['token']
    except:
        return redirect ('login')

        
    if request.method == 'GET':

        planes = Avion()

        url = 'http://127.0.0.1:8080/api/plane/'+str(id)
        response = requests.get(url)
        
       
        planes  = json.loads(response.content)
       
        return render (request, 'editaravion.html', {'planes' : planes})  
        


    if request.method == 'POST':
        
        url = "http://127.0.0.1:8080/api/plane/"+str(id)
        print(url)
        HEADERS = {
        "Content-Type": "application/json"
            }

        payload = {"matricula": str(request.POST['matricula']) , "marca": str(request.POST['marca']),"modelo": str(request.POST['modelo'])}
        response = requests.put(url, headers=HEADERS, json= payload)
        if response.status_code == 200:
            return redirect('aviones') 

        else:
            return redirect('inicio') 


def vuelos(request):

    try:
        request.COOKIES['token']
    except:
        return redirect ('login')

    if request.method == 'GET':

        vuelos = Vuelo()

        url = 'http://127.0.0.1:8080/api/vuelo/'
        response = requests.get(url)
       
        vuelos  = json.loads(response.content)
       
        return render (request, 'vuelos.html', {'vuelos' : vuelos})
    
def altavuelo(request):
    
    
    try:
        request.COOKIES['token']
    except:
        return redirect ('login')
    
       
    if request.method  =='GET':
        
        users = Usuario()
        url = 'http://127.0.0.1:8080/api/user/'
        response = requests.get(url)
        users  = json.loads(response.content)
        
        planes = Avion()
        url = 'http://127.0.0.1:8080/api/plane/'
        response = requests.get(url)
       
        planes  = json.loads(response.content)
        
        return render(request, 'altavuelo.html',{'users': users,'planes':planes})    
        
    if request.method == 'POST':
        
        url = 'http://127.0.0.1:8080/api/vuelo/'
        HEADERS = {
        "Content-Type": "application/json"
            }
        
        if request.POST['piloto'] == 'Piloto':
            messages.warning(request, 'Debe ingresar un Piloto')
            return redirect('vuelos')
        if request.POST['avion'] == 'Avion':    
            messages.warning(request, 'Debe ingresar un Avion')
            return redirect('vuelos')
        
        payload = {"usuario_id": int(request.POST['piloto']), "avion_Id": int(request.POST['avion']),"inicio": str(request.POST['inicio_f_h']),"fin": str(request.POST['fin_f_h']),"origen": str(request.POST['desde']),"destino": str(request.POST['hasta']),"tiempoVuelo":float(request.POST['tiempo_vuelo']) }
    
        response = requests.post(url, headers=HEADERS, json= payload)
        if response.status_code == 201:
            return redirect('vuelos') 
        
        else:
            return redirect('vuelos')
        
        
def eliminar_vuelo(request,id):
    try:
        request.COOKIES['token']
    except:
        return redirect ('login')

    
    if request.method == 'GET':
               
        url= 'http://127.0.0.1:8080/api/vuelo/'+str(id)

        response = requests.delete(url)

    return redirect('vuelos')  


def editar_vuelo(request,id):

    try:
        request.COOKIES['token']
    except:
        return redirect ('login')

        
    if request.method == 'GET':
        
        users = Usuario()
        url = 'http://127.0.0.1:8080/api/user/'
        response = requests.get(url)
        users  = json.loads(response.content)
        
        planes = Avion()
        url = 'http://127.0.0.1:8080/api/plane/'
        response = requests.get(url)
       
        planes  = json.loads(response.content)

        vuelos = Vuelo()

        url = 'http://127.0.0.1:8080/api/vuelo/'+str(id)
        response = requests.get(url)
       
        vuelos  = json.loads(response.content)
        
        vuelos['tiempoVuelo']= str(vuelos['tiempoVuelo'])
        
        vuelos['tiempoVuelo'] = vuelos['tiempoVuelo'].replace(".",",")
                       
        return render (request, 'editarvuelo.html', {'vuelos' : vuelos, 'planes' : planes, 'users': users})  
        

    if request.method == 'POST':
        
        url = "http://127.0.0.1:8080/api/vuelo/"+str(id)
        HEADERS = {
        "Content-Type": "application/json"
            }
        
        if request.POST['tiempo_vuelo'] is str:
            return redirect('vuelos')     
        
        tv = request.POST['tiempo_vuelo'].replace(",", ".");

        payload = {"usuario_id": int(request.POST['piloto']), "avion_Id": int(request.POST['avion']),
                   "inicio": str(request.POST['inicio_f_h']),"fin": str(request.POST['fin_f_h']),
                   "origen": str(request.POST['desde']),"destino": str(request.POST['hasta']),
                   "tiempoVuelo":float(tv) }
        response = requests.put(url, headers=HEADERS, json= payload)
        if response.status_code == 200:
            return redirect('vuelos') 

        else:
            return redirect('inicio')
        
        
def upload(request,id):
    
    try:
        request.COOKIES['token']
    except:
        return redirect ('login')
    
    if request.method == 'GET':
    #    url = "http://127.0.0.1:8080/api/upload/" + str(id)
    #    HEADERS = {
    #    "Content-Type": "multipart/form-data"
    #        }
    #    respones = requests.get(url)
    #    uploads = Uploads()
    #    
    #    uploads = respones.content
        
        return render (request, 'upload.html')
    
    
    if request.method == 'POST':
        
        url = "http://127.0.0.1:8080/api/upload/" + str(id)
        HEADERS = {
        "Content-Type": "multipart/form-data"
            }
        archivos = request.FILES.getlist('myfile')
        
        for f in archivos:
            files = {"files": f}
            requests.post(url, files = files)  
        
               
        return redirect ('vuelos')
         
    
    return render(request, 'upload.html')

def download(request,id):
        try:
            request.COOKIES['token']
        except:
            return redirect ('login')
        
    
        if request.method == 'GET':
    
            url = "http://127.0.0.1:8080/api/upload/" + str(id)
            HEADERS = {
            "Content-Type": "multipart/form-data"
                }
            
            requests.get(url)
            
            filename = str(id)+'.zip'
            
            filepath = 'D:/Proyectos Python/backendAeroclub/API/'+ filename
            
            path = open(filepath, 'rb')
            
            mime_type, _ = mimetypes.guess_type(filepath)
            
            response = HttpResponse(path, content_type = mime_type)
            
            response['Content-Disposition'] = "attachment; filename=%s" % filename
                        
            return response
            
