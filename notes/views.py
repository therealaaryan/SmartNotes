from django.shortcuts import render
from .models import Notes
from django.views.generic import ListView, DetailView

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = "notes/notes_details.html"