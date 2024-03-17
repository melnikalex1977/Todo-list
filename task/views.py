from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from .models import Task, Tag

def index(request):
    """View function for the home page of the site."""

    num_drivers = Task.objects.count()
    tasks_list = Task.objects.all()
    tag_list = Tag.objects.values_list('name', flat=True)
    task_list = Task.objects.values_list('content', 'datetime', 'published_date', 'tags')
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "tasks_list": tasks_list,
        "num_drivers": num_drivers,
        "tag_list": tag_list,
        "task_list": task_list,
        "num_visits": num_visits + 1,
    }

    return render(request, "task/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"
    paginate_by = 5
    template_name = "task/index.html"

class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["tags"]
    success_url = reverse_lazy("task:task-list")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        context['tag_id'] = task.tags.id
        return context


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:task-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5
    template_name = "task/task_list.html"


class TagDetailView(generic.DetailView):
    model = Tag
    queryset = Tag.objects.all().prefetch_related("cars__manufacturer")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:driver-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:driver-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:driver-list")

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_is_done']


class TaskNotDoneView(generic.UpdateView):
    model = Task
    fields = ["task_is_done"]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.task_is_done = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("task:task-list")


class TaskDone(generic.UpdateView):
    model = Task
    fields = ["task_is_done"]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.task_is_done = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("task:task-list")
