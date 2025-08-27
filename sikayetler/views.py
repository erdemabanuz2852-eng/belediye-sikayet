from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Sikayet
from .forms import SikayetForm, AksiyonForm

@method_decorator(login_required, name='dispatch')
class SikayetListView(ListView):
    model = Sikayet
    template_name = 'sikayetler/sikayet_list.html'
    context_object_name = 'sikayetler'
    paginate_by = 10
    ordering = ['-olusturma_tarihi']

@method_decorator(login_required, name='dispatch')
class SikayetCreateView(CreateView):
    model = Sikayet
    form_class = SikayetForm
    template_name = 'sikayetler/sikayet_form.html'
    success_url = reverse_lazy('sikayet_list')
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.olusturan_kullanici = self.request.user
        obj.save()
        messages.success(self.request, 'Şikayet oluşturuldu.')
        return super().form_valid(form)

@login_required
def sikayet_detay(request, pk):
    sikayet = get_object_or_404(Sikayet, pk=pk)
    aksiyon_form = AksiyonForm()
    if request.method == 'POST':
        if 'durum' in request.POST:
            sikayet.durum = request.POST.get('durum', sikayet.durum)
            sikayet.save()
            messages.success(request, 'Durum güncellendi.')
            return redirect('sikayet_detail', pk=pk)
        aksiyon_form = AksiyonForm(request.POST)
        if aksiyon_form.is_valid():
            aksiyon = aksiyon_form.save(commit=False)
            aksiyon.sikayet = sikayet
            aksiyon.yapan_kullanici = request.user
            aksiyon.save()
            messages.success(request, 'Aksiyon eklendi.')
            return redirect('sikayet_detail', pk=pk)
    return render(request, 'sikayetler/sikayet_detail.html', {
        'sikayet': sikayet,
        'aksiyon_form': aksiyon_form,
        'durum_secenekleri': [c[0] for c in sikayet.DURUM_SECENEKLERI],
    })
