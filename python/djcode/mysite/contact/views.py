from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext

from contact.forms import ContactForm

# def contact(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#             send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST.get('email', 'noreply@example.com'),
#                 ['siteowner@example.com'],
#             )
#         return HttpResponseRedirect('/contact/thanks/')
#     return render_to_response('contact_form.html', {'errors': errors})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', '13971310804@163.com'),
                ['13971310804@163.com', '125384977@qq.com', 'fengzhu@blizzmi.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect('/hello')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    # return render_to_response('contact_form.html', {'form': form})
    return render(request, 'contact_form.html', {'form': form})
