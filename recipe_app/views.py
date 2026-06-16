from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from dotenv import load_dotenv
from openai import OpenAI

import os

from .models import Recipe
from .forms import RecipeForm
from .ingredient_detector import detect_ingredient


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
print(os.getenv("OPENAI_API_KEY"))
def generate_recipe(ingredients):

    prompt = f"""
Generate a recipe using:

{ingredients}

Give:

1. Dish Name
2. Ingredients
3. Cooking Steps
4. Cooking Time
"""
    response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


@login_required
def home(request):

    generated_recipe = ""

    if request.method == "POST":

        form = RecipeForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            ingredients = form.cleaned_data["ingredients"]

            image = form.cleaned_data["image"]

            if image:

                image_path = os.path.join(
                    "media",
                    image.name
                )

                with open(
                    image_path,
                    "wb+"
                ) as destination:

                    for chunk in image.chunks():
                        destination.write(chunk)

                detected = detect_ingredient(
                    image_path
                )

                if detected:

                    if ingredients:

                        ingredients += ", " + detected

                    else:

                        ingredients = detected

            generated_recipe = generate_recipe(
                ingredients
            )

            Recipe.objects.create(
                user=request.user,
                ingredients=ingredients,
                recipe=generated_recipe,
                image=image
            )

    else:

        form = RecipeForm()

    return render(
        request,
        "home.html",
        {
            "form": form,
            "recipe": generated_recipe
        }
    )


@login_required
def history(request):

    recipes = Recipe.objects.filter(
        user=request.user
    ).order_by(
        "-created_at"
    )

    return render(
        request,
        "history.html",
        {
            "recipes": recipes
        }
    )


def register(request):

    message = ""

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        if User.objects.filter(
            username=username
        ).exists():

            message = "Username already exists"

        else:

            User.objects.create_user(
                username=username,
                password=password
            )

            return redirect(
                "login"
            )

    return render(
        request,
        "register.html",
        {
            "message": message
        }
    )


def user_login(request):

    message = ""

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect(
                "home"
            )

        else:

            message = "Invalid Credentials"

    return render(
        request,
        "login.html",
        {
            "message": message
        }
    )


def user_logout(request):

    logout(request)

    return redirect(
        "login"
    )