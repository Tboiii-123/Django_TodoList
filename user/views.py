from django.shortcuts import render,redirect

# Create your views here.
from . models import *



def index(request):

    task=Task.objects.all()

    if request.method =="POST":
        taskname =request.POST.get('task')
        if taskname=='':
            redirect('/')

        else:
            model_task =Task(title=taskname)
            model_task.save()



    return render(request,'list.html',{
        'task':task,
    })



def update(request,item):
        
        task =Task.objects.get(id=item)

        if request.method =="POST":
            
             Title = request.POST.get('task',task.title)
            
             if Title == "":
                  return redirect('update',item)
            
             else:

                task.title = Title 
                task.complete = 'complete' in request.POST

                task.save()
                return redirect('/')



        return render(request,'update.html',{
             'task':task
             
        })







# def updateTask(request,item):

#     task =Task.objects.get(pk=item)
    
#     form =TaskForm(instance=task)
    
#     if request.method =="POST":
#         form =TaskForm(request.POST,instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
            
    
#     return render(request,'update_task.html',{
        
#         'form':form,
        
#     })





def delete(request,item):
    
    tasks =Task.objects.get(id=item)

    if request.method =="POST":
        tasks.delete()
        return redirect('/')

    return render(request,'delete.html',{
        'task':tasks
    })











#password
#hussein
#1234