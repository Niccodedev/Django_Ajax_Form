from Django_Ajax_Form.forms import CalculationForm
from django.shortcuts import render
from django.http import JsonResponse
import math
def first_page(request):
    form = CalculationForm()
    return render(request, 'calculate.html',{
        'form':form
    })
def calculate(request):
    operand = float(request.GET.get('operand',0.0))
    operator = request.GET.get('operator','sqrt')
    if operator=='sqrt' and operand < 0:
        return JsonResponse({ 'success':False, 'error': "Operand can't be negative"  })
    if operator == 'sqrt':
        result = math.sqrt(operand)
    if operator == 'square':
        result = operand * operand
    return JsonResponse({'success': True, 'result': result})
