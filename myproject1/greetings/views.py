import logging
from django.shortcuts import render
from django.http import JsonResponse
from sklearn.linear_model import LinearRegression
import numpy as np

# Configure logging
logger = logging.getLogger(__name__)

# Temporary storage for input data
data = {
    "areas": [],
    "prices": []
}

# Initialize the linear regression model
model = LinearRegression()

# Serve the template instead of raw text
def hello_world(request):
    logger.info("Rendering template: greeting/index.html")
    return render(request, 'greeting/index.html')  # This points to your index.html in templates/greeting/

# Save data from the frontend and train the model
def save_data(request):
    try:
        if request.method == 'POST':
            # Log incoming request data
            logger.info(f"Received POST data: {request.POST}")

            # Get data from the request
            area = request.POST.get('area')
            price = request.POST.get('price')

            # Validate input
            if not area or not price:
                error_message = "Both 'area' and 'price' are required."
                logger.error(error_message)
                return JsonResponse({"error": error_message}, status=400)

            # Save data into the temporary storage
            logger.info(f"Saving data: Area={area}, Price={price}")
            data["areas"].append(float(area))
            data["prices"].append(float(price))

            # Train the model with the updated data
            X = np.array(data["areas"]).reshape(-1, 1)  # Feature matrix
            y = np.array(data["prices"])  # Target values
            model.fit(X, y)
            logger.info("Model successfully trained with updated data.")

            return JsonResponse({"message": "Data saved successfully!"})

        # Log invalid method
        logger.warning(f"Invalid request method: {request.method}")
        return JsonResponse({"error": "Invalid request method"}, status=405)

    except Exception as e:
        # Log the exception with a stack trace
        logger.exception("An error occurred in save_data.")
        return JsonResponse({"error": "An unexpected error occurred. Check server logs for details."}, status=500)

# Predict house prices using the trained model
def predict(request):
    try:
        if request.method == 'POST':
            # Log incoming request data
            logger.info(f"Received POST data for prediction: {request.POST}")

            # Get the area value for prediction
            area = request.POST.get('area')

            # Validate input
            if not area:
                error_message = "Area is required for prediction."
                logger.error(error_message)
                return JsonResponse({"error": error_message}, status=400)

            # Perform prediction using the trained model
            area_value = np.array([[float(area)]])
            predicted_price = model.predict(area_value)[0]
            logger.info(f"Predicted price for area {area}: {predicted_price}")

            return JsonResponse({"predicted_price": predicted_price})

        # Log invalid method
        logger.warning(f"Invalid request method: {request.method}")
        return JsonResponse({"error": "Invalid request method"}, status=405)

    except Exception as e:
        # Log the exception with a stack trace
        logger.exception("An error occurred in predict.")
        return JsonResponse({"error": "An unexpected error occurred. Check server logs for details."}, status=500)
