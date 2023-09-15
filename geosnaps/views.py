from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Place, Comment
from .forms import UploadForm, CommentForm
from django.utils import timezone


@login_required
def home_view(request):
    places = Place.objects.all()
    return render(request, "place_list.html", context={"places": places})


@login_required
def place_detail_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    user = request.user
    has_commented = Comment.objects.filter(user=user, place=place).exists()

    # Check if the current time is before the end_time
    allow_comments = timezone.now() < place.end_time
    winners = Comment.objects.filter(place=place, is_correct=True).order_by(
        "created_at"
    )

    # Handle comment submission
    if request.method == "POST":
        if not has_commented and allow_comments:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = user
                comment.place = place
                if place.location.lower() == comment.text.lower():
                    comment.is_correct = True
                comment.save()
                return redirect("place_detail", place_id=place_id)
        else:
            messages.error(request, "You have already commented on this place.")
    else:
        form = CommentForm()

    return render(
        request,
        "place_detail.html",
        {
            "place": place,
            "user": user,
            "has_commented": has_commented,
            "form": form,
            "allow_comments": allow_comments,
            "winners": winners,
        },
    )


@login_required
def upload_view(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_data = form.save(commit=False)
            upload_data.user = request.user
            upload_data.save()
            return redirect("home")
    else:
        form = UploadForm()
    return render(request, "upload.html", {"form": form})
