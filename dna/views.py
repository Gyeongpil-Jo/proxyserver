
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Dna
from .forms import DnaForm


@csrf_exempt
def input_dna(request):
    if request.method == 'POST':
        form = DnaForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.seq_num = len(job.seq)
            job.save()

            return redirect('dna:output', job_id=job.id)

    else:
        form = DnaForm()
    context = {'form': form}
    return render(request, 'dna/input.html', context)


@csrf_exempt
def output_dna(request, job_id):
    job = get_object_or_404(Dna, pk=job_id)
    form = DnaForm()
    context = {'job': job, 'form': form}
    return render(request, 'dna/output.html', context)


