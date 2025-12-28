from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def calculator_home(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        operator = request.POST.get('operator')
        num2 = request.POST.get('num2')

        result = 0
        if operator == '+':
            result = float(num1) + float(num2)
        elif operator == '-':
            result = float(num1) - float(num2)
        elif operator == '*':
            result = float(num1) * float(num2)
        elif operator == '/':
            if float(num2) != 0:
                result = float(num1) / float(num2)
            else:
                result = 'Error: Division by zero'

        return render(request, 'calculator/calculator.html', {
            'result': result,
            'num1': num1,
            'num2': num2,
            'operator': operator
        })

    return render(request, 'calculator/calculator.html')