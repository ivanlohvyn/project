from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect

from .models import Post, Tag
from .forms import PostForm, TagForm


def index(request):
    return render(request, "blog/index.html")


def post_list(request):
    latest_post_list = Post.objects.order_by("-created")[:10]
    return render(
        request,
        "blog/post_list.html",
        context={"latest_post_list": latest_post_list},
    )


def post_create(request):
    form = PostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(reverse("blog:post_detail", args=(post.slug,)))
    else:
        form = PostForm()
    return render(request, "blog/post_create.html", {"form": form})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    return render(request, "blog/post_detail.html", context={"post": post})


def tag_list(request):
    tag_list = Tag.objects.all()
    return render(request, "blog/tag_list.html", context={"tag_list": tag_list})


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, "blog/tag_detail.html", context={"tag": tag})


def tag_create(request):
    form = TagForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            tag = form.save()
            return HttpResponseRedirect(reverse("blog:tag_detail", args=(tag.slug,)))
    else:
        form = TagForm()
    return render(request, "blog/tag_create.html", {"form": form})
