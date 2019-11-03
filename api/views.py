from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView

from api.forms import FactorialForm, AckermannForm, FibonacciForm
from api.tasks import time_func, ackermann, fibonacci, factorial


def root(request):
    return render(request, 'root.html', {
        "subpages": [
            {'name': "Ackermann", 'path': reverse('ackermann-view')},
            {'name': "Factorial", 'path': reverse('factorial-view')},
            {'name': "Fibonacci", 'path': reverse('fibonacci-view')},
        ]
    })


class ResultMixin:
    """
    Handles fetching and rendering of results.
    """
    def get_results(self, form):
        raise NotImplementedError()

    def form_valid(self, form):
        return self.get_result_appended_context_data(form)

    def get_result_appended_context_data(self, form):
        print(form.cleaned_data)
        exec_time, res = self.get_results(form)
        context = self.get_context_data()
        context['results'] = {
            "result": res,
            "exec_time": exec_time,
        }
        return self.render_to_response(context=context)


class FactorialView(ResultMixin, FormView):
    template_name = "factorial.html"
    form_class = FactorialForm

    def get_results(self, form):
        return time_func(factorial, **form.cleaned_data)


class AckermannView(ResultMixin, FormView):
    template_name = "ackermann.html"
    form_class = AckermannForm

    def get_results(self, form):
        try:
            return time_func(ackermann, **form.cleaned_data)
        except RecursionError:
            return -1, "That's too big, I can't handle this one."


class FibonacciView(ResultMixin, FormView):
    template_name = "fibonacci.html"
    form_class = FibonacciForm

    def get_results(self, form):
        return time_func(fibonacci, **form.cleaned_data)
