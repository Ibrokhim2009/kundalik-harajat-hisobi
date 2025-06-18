from django.shortcuts import render, redirect
from .models import Category, Expense
from .forms import CategoryForm, ExpenseForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    total = sum(x.amount for x in expenses)
    return render(request, 'dashboard.html', {'expenses': expenses, 'total': total})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('dashboard')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

