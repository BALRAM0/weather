import cv2
import numpy as np
import pandas as pd



class AI():
    
    
    

    def temp(self,image):
        image=image
        image = cv2.imread(image)

        # Preprocess the image if necessary
        image = cv2.resize(image, (800, 600))

        # Extract temperature data
        # Assuming temperature is represented by red color channel (BGR format)
        red_channel = image[:, :, 2]  # Extract the red channel

        calibration_curve = {
            0: 10.0,
            50: 20.0,
            100: 30.0,
            150: 40.0,
            200: 50.0,
            # Add more mappings as per your calibration data
        }

        # Convert pixel values to temperature units (example conversion, adjust as per your image)
        # Convert pixel values to temperature units using calibration curve
        temperature_data = np.vectorize(lambda x: calibration_curve.get(x, np.nan))(red_channel)

        # Store temperature data in a DataFrame
        df = pd.DataFrame(temperature_data)
        max_temperature = df.max().values[0]
        min_temperature = df.min().values[0]
        current_temp=(max_temperature+min_temperature)//2


        # Print the DataFrame
        # print(df)
        print(max_temperature)
        print(min_temperature)
        print(current_temp)
        return max_temperature,min_temperature;
    
    
    def humidity(self,image):
        # Load the image
        image = cv2.imread(image)

        # Preprocess the image if necessary
        # Apply any necessary resizing, cropping, or filtering steps

        # Convert the image to a suitable color space (e.g., grayscale, HSV, LAB)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply image processing techniques to identify humidity-related patterns
        # This step heavily depends on the specific indicators or patterns you're looking for
        # Example: Applying a threshold to extract regions with high humidity indicator
        _, threshold = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

        # Analyze the extracted information and derive a measure or estimate of humidity
        # This step will highly depend on the nature of the humidity-related patterns in your image
        # Example: Counting the number of white pixels in the thresholded image
        humidity_pixels = np.sum(threshold == 255)

        # Calculate humidity percentage based on total image pixels or a calibration curve
        total_pixels = threshold.shape[0] * threshold.shape[1]
        humidity_percentage = (humidity_pixels / total_pixels) * 100

        # Print the humidity percentage
        print("Humidity: {}%".format(humidity_percentage))
        
        return humidity_percentage;
    
    def chanceofrain(self,image):
        def preprocess_image(image_path):
        # Load the image
            image = cv2.imread(image_path)
            
            # Resize the image for better performance (optional)
            image = cv2.resize(image, (800, 600))
            
            # Convert the image to grayscale
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Apply Gaussian blur to reduce noise
            blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
            
            return blurred_image

        def calculate_rain_chance(image_path):
            # Preprocess the image
            blurred_image = preprocess_image(image_path)
            
            # Apply adaptive thresholding to segment the image
            _, thresholded_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            
            # Count the number of white pixels (rainy regions)
            total_pixels = np.prod(thresholded_image.shape)
            white_pixels = np.sum(thresholded_image == 255)
            
            # Calculate the chance of rain
            rain_chance = (white_pixels / total_pixels) * 100
            
            return rain_chance

        image_path = image
        chance_of_rain = calculate_rain_chance(image_path)
        print(f"The chance of rain in the image is: {chance_of_rain}%")
        return chance_of_rain;
    
    
    
    def cloud(self,image):
        image = cv2.imread(image)


        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to obtain a binary image
        _, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

        # Calculate the cloud coverage percentage
        cloud_pixels = cv2.countNonZero(binary_image)
        total_pixels = binary_image.shape[0] * binary_image.shape[1]
        cloud_percentage = (cloud_pixels / total_pixels) * 100

        # Print the cloud coverage percentage
        print("Cloud Coverage Percentage:", cloud_percentage)
        return cloud_percentage;
    
    def priciption(self,image):
        image = cv2.imread(image)


        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to obtain a binary image
        _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Calculate the area covered by precipitation
        precipitation_area = cv2.countNonZero(binary_image)
        total_area = binary_image.shape[0] * binary_image.shape[1]

        precipitation_percentage = (precipitation_area / total_area) * 100


        # Display the original image and the binary image
        # cv2.imshow('Original Image', image)
        # cv2.imshow('Binary Image', binary_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # Print the calculated precipitation area
        print("Precipitation Area:", precipitation_area)
        print(precipitation_percentage)
        return precipitation_percentage;


# obj =AI()
# image='download.jpg'
# a,b=obj.temp(image)
# b=obj.humidity(image)
# c=obj.priciption(image)
# d=obj.chanceofrain(image)


    

                
        