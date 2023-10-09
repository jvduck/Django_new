from django.shortcuts import render, redirect
from inventario.models import Productos
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def listarProductos(req):
    productos = Productos.objects.all()
    contexto = {"productos":productos}
    return render(req, 'index.html', contexto)

#Eliminar un producto
def eliminarProducto(req,id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect(req,'index')

#Usamos la funcion para RECIBIR el producto a EDITAR y tambien GUARDAR el producto editado
def editarProducto(req,id):
    producto = Productos.objects.get(id=id)
    
    if req.method == "GET":
        contexto = {"producto": producto}
        return render(req,'editar.html',contexto)
    elif req.method == "POST":
        #capturar los datos del POST
        nombre_nuevo = req.POST["nombre"]
        precio_nuevo = req.POST["precio"]
        stock_nuevo = req.POST["stock"]
        producto.nombre = nombre_nuevo
        producto.precio = precio_nuevo
        producto.stock = stock_nuevo
        #necesito si o si volver a guardar el producto
        producto.save()
        return redirect('index')

def crearProducto(req):
    nombre_post = req.POST["nombre"]
    precio_post = req.POST["precio"]
    stock_post = req.POST["stock"]
    producto = Productos(nombre=nombre_post, precio=precio_post, stock=stock_post)
    producto.save() #si o si preciso el save para guardar mi producto!!!
    return redirect('index')