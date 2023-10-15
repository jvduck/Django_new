from django.shortcuts import render, redirect, get_object_or_404
from inventario.models import Productos, Categorias
from django.contrib.auth.decorators import login_required
from .forms import FormProducto

# Create your views here.
def listarProductos(req):
    productos = Productos.objects.all() #equivale a un "SELECT FROM Productos
    categorias = Categorias.objects.all()#equivale a un "SELECT FROM Categorias
    formulario = FormProducto()
    #renderizamos en el CONTEXTO
    contexto = {"productos":productos, "categorias":categorias, "formulario":formulario}
    return render(req, 'index.html', contexto)

#Eliminar un producto
@login_required
def eliminarProducto(req,id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect('index')

#Usamos la funcion para RECIBIR el producto a EDITAR y tambien GUARDAR el producto editado
@login_required
def editarProducto(req,id):
    #producto = Productos.objects.get(id=id)
    #lista_categorias = Categorias.objects.all()
    producto = get_object_or_404(Productos, id=id)
    
    if req.method == "GET":
        formulario = FormProducto(instance=producto)
        contexto = {"producto":producto, "formulario":formulario}
        return render(req,'editar.html',contexto)
    
    elif req.method == "POST":
        #capturar los datos del POST
        #nombre_nuevo = req.POST["nombre"]
        #precio_nuevo = req.POST["precio"]
        #stock_nuevo = req.POST["stock"]
        #id_categoria_nueva =req.POST["categoria"]
        #categoria_nueva = Categorias.objects.get(id=id_categoria_nueva)
        #producto.nombre = nombre_nuevo
        #producto.precio = precio_nuevo
        #producto.stock = stock_nuevo
        #producto.categoria_fk = categoria_nueva #! guardaos instancias (creacion de objetos)
        ##necesito si o si volver a guardar el producto
        #producto.save()
        formulario = FormProducto(req.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')

@login_required
def crearProducto(req):
    #nombre_post = req.POST["nombre"]
    #precio_post = req.POST["precio"]
    #stock_post = req.POST["stock"]
    #categoria_id = req.POST["categoria"]
    #categoria_instance = Categorias.objects.get(id=categoria_id)
    #producto = Productos(nombre=nombre_post, precio=precio_post, stock=stock_post, categoria_fk=categoria_instance)
    #producto.save() #si o si preciso el save para guardar mi producto!!!
    #? Form de creacion de prodcutos:
    form_producto = FormProducto(req.POST)
    if form_producto.is_valid():
        form_producto.save()
    return redirect('index')