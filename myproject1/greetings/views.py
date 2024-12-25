from django.shortcuts import render

# Serve the template instead of raw text
def hello_world(request):
    print("Rendering template: greeting/index.html")  # Debugging message
    return render(request, 'greeting/index.html')  # This points to your index.html in templates/greeting/
