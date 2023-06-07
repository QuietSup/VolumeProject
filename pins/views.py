from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from Volume.models import Pin
from pins.forms import CreatePinForm, UpdatePinForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
import datetime
from django.core.paginator import Paginator


def explore(request):
    sort_by = {
        'Most_liked': '-likes',
        'Least liked': 'likes',
        'Latest added': '-created_at',
        'Earliest added': 'created_at',
        'Latest updated': '-updated_at',
        'Earliest updated': 'updated_at',
    }

    when_created = {
        'last_6hours': 'Last six hours',
        'last_day': 'Last day',
        'last_2days': 'Last two days',
        'last_week': 'Last week',
        'last_month': 'Last month',
        'last_year': 'Last year',
    }

    if request.GET.get('sort') and request.GET.get('sort') in sort_by.values():
        pins = Pin.objects.order_by(request.GET['sort'])
    else:
        pins = Pin.objects.order_by('created_at')

    if request.GET.get('when_created') and request.GET.get('when_created') in when_created.keys():
        if request.GET.get('when_created') == 'last_6hours':
            delta = datetime.timedelta(hours=6)
        if request.GET.get('when_created') == 'last_day':
            delta = datetime.timedelta(days=1)
        if request.GET.get('when_created') == 'last_2days':
            delta = datetime.timedelta(days=2)
        if request.GET.get('when_created') == 'last_week':
            delta = datetime.timedelta(weeks=1)
        if request.GET.get('when_created') == 'last_month':
            delta = datetime.timedelta(weeks=4)
        if request.GET.get('when_created') == 'last_year':
            delta = datetime.timedelta(days=365)

        date_from = datetime.datetime.now() - delta
        pins.filter(created_at__gt=date_from)

    if request.GET.get('search'):
        pins = Pin.objects.filter(title__icontains=request.GET.get('search')) \
               | Pin.objects.filter(description__icontains=request.GET.get('search')) \
               | Pin.objects.filter(creator__username__icontains=request.GET.get('search'))

    paginator = Paginator(pins, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pins/explore.html', {'current_user': request.user, 'sort_by': sort_by, 'when_created': when_created, 'page_obj': page_obj})

@login_required
def add_like(request, pinId):
    pin = get_object_or_404(Pin, id=int(pinId))
    pin.increase_likes()
    request.user.liked_pins.add(pin)
    return HttpResponse(status=200)

@login_required
def remove_like(request, pinId):
    pin = get_object_or_404(Pin, id=int(pinId))
    pin.decrease_likes()
    request.user.liked_pins.remove(pin)
    return HttpResponse(status=200)

@login_required
def create_pin(request):
    if request.method == 'POST':
        form = CreatePinForm(request.POST, request.FILES)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.creator = request.user
            pin.save()
            return redirect('pins:show_pin', slugify(pin.title), pin.id)
    else:
        form = CreatePinForm()
    return render(request, 'pins/new-item.html', {'form': form})

def show_pin(request, slug, pin_id):
    pin = get_object_or_404(Pin, pk=pin_id)

    if slugify(pin.title) != slug:
        return redirect('pins:show_pin', slug=slugify(pin.title), pin_id=pin_id)

    creator_pins = pin.creator.pin_set.order_by('created_at').exclude(pk=pin_id)[:6]


    return render(request, 'pins/show-pin.html', {'pin': pin, 'creator_pins': creator_pins})

@login_required
def edit_pin(request, pin_id):
    if not request.user.pin_set.filter(pk=pin_id):
        redirect('pins:explore')

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

    return render(request, 'pins/edit-pin.html', {'form': form, 'pin': pin})

@login_required
def delete_pin(request, pin_id):
    if not request.user.pin_set.filter(pk=pin_id):
        return redirect('pins:explore')

    pin = get_object_or_404(Pin, pk=pin_id)
    pin.delete()

    return redirect('pins:explore')
