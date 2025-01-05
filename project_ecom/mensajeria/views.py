from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mensajeria.models import Message
from django.db.models import Q
from .forms import SendMessage, SendMessageByAdmin

# Create your views here.
@login_required(login_url='core:my-login')
def chat(request):
    try:
        all_messages = Message.objects.filter(
                    Q(from_user=request.user) | Q(to_user=request.user)
                ).order_by('creation_date')
        if request.user.username == 'admin':
            form = SendMessageByAdmin()
            if request.method == "POST":
                form = SendMessageByAdmin(request.POST)
                if form.is_valid():
                    form.save(from_user=request.user)
                    return redirect("mensajeria:chat")
        else:
            form = SendMessage()
            if request.method == "POST":
                form = SendMessage(request.POST)
                if form.is_valid():
                    form.save(from_user=request.user)
                    return redirect("mensajeria:chat")
        context = {'msgs': all_messages, 'form': form}
        return render(request, 'msg/chat.html', context=context)
    except:
        return redirect("mensajeria:chat")