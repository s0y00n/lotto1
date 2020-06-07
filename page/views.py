from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def result(request):

    number_list=[]

    for i in range(1,7,1):
        number = request.GET['number'+str(i)]
        number_list.append(number)
    
    random_list=[]

    import random
    for j in range(1,7,1):
         number1=random.randrange(0,46)
         random_list.append(number1)
         random_list.sort()

    count=0

    for i in range(0,len(number_list)):
        for j in range(0,len(random_list)):
            if number_list[i]==random_list[j]:
                count=count+1
    





    return render(request, 'result.html',{'number_list':number_list, 'random_list':random_list, 'count':count})