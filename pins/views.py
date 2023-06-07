from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from Volume.models import Pin
from pins.forms import CreatePinForm, UpdatePinForm
from django.utils.text import slugify


# Create your views here.
def explore(request):
    if request.method == 'POST':
        pass
    else:
        if request.GET.get('sort'):
            if request.GET.get('sort') == 'justAdded':
                #  TODO: можна додати прикол типу шо тіки ті шо сьодні додались чи шось таке, якщо хо.
                pins = Pin.objects.order_by('updated_at')
            elif request.GET.get('sort') == 'lowToHigh':
                pins = Pin.objects.order_by('price')
            elif request.GET.get('sort') == 'highToLow':
                pins = Pin.objects.order_by('-price')
            elif request.GET.get('sort') == 'mostLiked':
                pins = Pin.objects.order_by('-likes')
            elif request.GET.get('sort') == 'leastLike':
                pins = Pin.objects.order_by('likes')
            else:
                pins = Pin.objects.order_by('updated_at')
        elif request.GET.get('search'):
            search = request.GET.get('search')
            pins = Pin.objects.filter(title__icontains=search) | Pin.objects.filter(description__icontains=search)
        else:
            pins = Pin.objects.order_by('updated_at')

    return render(request, 'pins/explore.html', {'pins': pins, 'current_user': request.user})

def add_like(request, pinId):
    pin = get_object_or_404(Pin, id=int(pinId))
    pin.increase_likes()
    request.user.liked_pins.add(pin)
    return HttpResponse(status=200)


def remove_like(request, pinId):
    pin = get_object_or_404(Pin, id=int(pinId))
    pin.decrease_likes()
    request.user.liked_pins.remove(pin)
    return HttpResponse(status=200)

def create_pin(request):
    if request.method == 'POST':
        form = CreatePinForm(request.POST, request.FILES)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.creator = request.user
            pin.save()
            redirect('pins:show_pin', slugify(pin.title), pin.id)
    else:
        form = CreatePinForm()
    return render(request, 'pins/new-item.html', {'form': form})

def show_pin(request, slug, pin_id):
    pin = get_object_or_404(Pin, pk=pin_id)

    if slugify(pin.title) != slug:
        return redirect('pins:show_pin', slug=slugify(pin.title), pin_id=pin_id)

    return render(request, 'pins/show-pin.html', {'pin': pin})

def edit_pin(request, pin_id):
    pin = get_object_or_404(Pin, pk=pin_id)

    if request.method == 'POST':
        form = UpdatePinForm(request.POST, request.FILES, instance=pin)
        if form.is_valid():
            if not form.fields['image']:
                updated_pin: Pin = form.save(commit=False)
                updated_pin.save(update_fields=[x for x in form.fields.keys() if x!='image'])

            else:
                form.save()
            return redirect('pins:show_pin', slugify(form.fields['title']), pin.pk)

    else:
        form = UpdatePinForm(instance=pin)
        print()

    return render(request, 'pins/edit-pin.html', {'form': form, 'pin_id': pin_id})
