from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Note
import csv

def index(request):
    # get object
    lists = Note.objects.order_by('pub_date')
    balance = total_money()  # total money to show in index
    total = total_in_and_ex()
    income = total[0]  # income to show in table
    expense = -total[1]  # expense to show in table
    context = {'lists':lists,'balance':balance,
               'income':income,'expense':expense}
    return render(request, 'ledger/index.html',context)
    
def add_list(request):  # add note 
    # request all POST value
    new_note = request.POST['add_note']  # note's text 
    new_money = request.POST['add_money']  # money
    money_type = request.POST['money_type']  # money type (income,expense)
    date_note = request.POST['date']  # get date from input date
    time = date_note
    # if money_type is expense make it minus    
    if money_type == "ex":
        new_money = -int(new_money)
    total = total_money() + int(new_money)
    
   # re_balance(time)
    
    getnote = Note(note_text=new_note,cost_value=new_money,
                   cost_total=total,pub_date=time)
    getnote.save()
    print(timezone.now())
    return HttpResponseRedirect(reverse('ledger:index'))

def verify(request):
    q = request.POST['note_li']  # get list of selected note's id
    lists = Note.objects.get(pk=q)
    total_index = total_money()  # all money
    context = {'lists':lists,'total_index':total_index}
    return render(request,'ledger/verify_page.html',context)

def edit_list(request):  # use to view edit page
    lists = Note.objects.order_by('pub_date')  # get obj. and order by date
    total_index = total_money()  # all money
    context = {'lists':lists,'total_index':total_index}
    return render(request,'ledger/delete_page.html',context)

def del_list(request, note_id):  # delete note
    q = Note.objects.get(pk=note_id)
    q.delete()
    # redirect to edit page
    return HttpResponseRedirect(reverse('ledger:edit_list'))
                  
def total_money():  # all money 
    total = 0  # set default to 0
    n = Note.objects.all()  # get obj.
    for note in n:  # use for loop for all note in Model
        get_money = Note.objects.get(pk=note.id)
        total += get_money.cost_value  # calculate all money
    return total 

# this function use to calculate all income and expense
def total_in_and_ex():  # all income
    total_income = 0  # set default to 0
    total_expense = 0
    n = Note.objects.all()
    for note in n:
        get_money = Note.objects.get(pk=note.id)
        if get_money.cost_value > 0:  # if variable get_money is +
            total_income += get_money.cost_value  # increase total value
        else :
            total_expense += get_money.cost_value
    total = [total_income,total_expense]
    return total  # returnn total
    
def download(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="history.csv"'
    writer = csv.writer(response)
    n = Note.objects.all()
    writer.writerow(['pub_date', 'note', 'income', 'expense'])
    for note in n:
        if(note.cost_value < 0):
            value = -note.cost_value
            writer.writerow([note.pub_date,note.note_text,'0',value])
        else:
            writer.writerow([note.pub_date,note.note_text,note.cost_value,'0'])
        
    return response

def theme_select(request):
    return render(request,'ledger/theme_page.html')

def change_theme(request):
    theme = request.POST['selected_theme']
    