from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Home page view
def home_view(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align:left;
                margin-top: 50px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                border-radius:12px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>Hello praveen Here</h1>
        <p>Welcome to my Django Project </p>
        <form action="/about/">
            <button type="submit">About Me</button>
        </form>
    </body>
    </html>
    """
    return HttpResponse(html)

# About page view
def about_view(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align:left;
                margin-top: 50px;
            }
        </style>
    </head>
    <body>
        <h1>About Me</h1>
        <p>Full Name :Praveen.M</p>
        <p>Roll No : 22uit043</p>
        <p>Dept : B.Tech IT</p>
        <p>Class : III year IT-A</p>
        <p>College : Kamaraj college of engineering and technology</p>
    </body>
    </html>
    """
    return HttpResponse(html)

