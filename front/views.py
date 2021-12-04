from django.shortcuts import render, redirect


def home_view(request):
    return render(request, 'front/home.html')


# def add_socilas(request):
#     if request.method == 'POST':
#         form = AddSocials(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile-view')

#     else:
#         form = AddSocials(instance=request.user)

#     context = {
#         'form': form,
#     }

#     return render(request, 'front/socials.html', context)