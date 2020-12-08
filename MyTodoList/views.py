from django.shortcuts import render,redirect
from .forms import TodoForm
from .models import Todo

# Create your views here.
def Adminpage(request):
     #instanciate our form to make ready to receive date
    form=TodoForm() 
    #get all of our object and put them in Todos array
    Todos=Todo.objects.all()
    # check if the user try to post data   
    if request.method=="POST":  
        # intanciate our model with what our user write.  
        form=TodoForm(request.POST) 
         #check it if it is valid before save it
        if form.is_valid():   
            form.save()      # saving
            #create the context wich contain form and todos     
    context={"form":form, "Todos":Todos} 
    # rendering the html page passing the context dictionnary
    return render(request,'index.html',context) 

def UpdateTodo(request,pk):
    # get the object wich want to update
    todo=Todo.objects.get(id=pk) 
     #intanciate TodoForm without losing the previous data 
    form=TodoForm(instance=todo)
    if request.method=="POST":
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={"form":form, "Todo":Todo}
    return render(request,'index.html',context)
def DeleteTodo(request,pk):
    # get the object we want to delete
    todo=Todo.objects.get(id=pk) 
    todo.delete()   #delete object
    return redirect('home') # redirecting to the home page

