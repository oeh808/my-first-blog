from django.shortcuts import render
from django.utils import timezone
from .models import Post, cvText, cvList
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

def cv_view(request):
    return render(request, 'cv/cv_view.html')

def contact_details(request):
    address = cvText.objects.filter(pageTitle='Physical Address')
    number = cvText.objects.filter(pageTitle='Telephone Number')
    email = cvText.objects.filter(pageTitle='Email Address')
    return render(request, 'cv/contact_details.html', {'address': address,'number': number, 'email': email })

def personal_profile(request):
    me = cvText.objects.filter(pageTitle='About Me')
    return render(request, 'cv/personal_profile.html', {'me': me})

def education(request):
    school = cvList.objects.filter(pageTitle='School')
    uni = cvList.objects.filter(pageTitle='University')
    return render(request, 'cv/education.html', {'school' : school, 'uni' : uni})

def work_experience(request):
    work = cvList.objects.filter(pageTitle='Work Experience')
    return render(request, 'cv/work_experience.html', {'work': work})

def interests_achievements(request):
    interests = cvList.objects.filter(pageTitle='Interests')
    achievs = cvList.objects.filter(pageTitle='Achievements')
    return render(request, 'cv/interests_achievements.html', {'interests' : interests, 'achievs' : achievs})

def refrences(request):
    ref = cvList.objects.filter(pageTitle='References')
    return render(request, 'cv/refrences.html', {'ref' : ref})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
