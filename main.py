# # # # # # from wifimgr import WifiManager
# # # # # # import machine
# # # # # # import dht
# # # # # # import time
# # # # # # import urequests
# # # # # # import ujson
# # # # # # import ubinascii
# # # # # # import network



# # # # # # wm = WifiManager()
# # # # # # wm.connect()

# # # # # # # FIREBASE_URL = "https://irridate-b5b0a-default-rtdb.firebaseio.com/"
# # # # # # FIREBASE_URL = "https://irridate-b5b0a-default-rtdb.firebaseio.com"
# # # # # # SECRET_KEY = "AIzaSyDCr-6ucuulvgfHHnoV10MaTii7lPOCaj0"


# # # # # # # dht_pin = machine.Pin(2) 
# # # # # # # sensor = dht.DHT22(dht_pin)
# # # # # # # ao_pin = machine.ADC(0)

# # # # # # def send_to_firebase(data):
# # # # # #     headers = {
# # # # # #         "Content-Type": "application/json",
# # # # # #         "Authorization": "Bearer " + SECRET_KEY
# # # # # #     }
# # # # # #     # url = FIREBASE_URL + "/test.json"  # Change 'your-collection' to your Firebase collection
# # # # # #     url = FIREBASE_URL + "/test.json?auth=" + SECRET_KEY


# # # # # #     response = urequests.post(url, data=ujson.dumps(data), headers=headers)
# # # # # #     print("Firebase Response:", response.text)
# # # # # #     response.close()

# # # # # # sensor_data = {
# # # # # #     "temperature": 25.5,
# # # # # #     "humidity": 60
# # # # # # }

# # # # # # if wm.is_connected():
   
# # # # # #     print("Connected to WiFi")
# # # # # #     wlan_sta = network.WLAN(network.STA_IF)
# # # # # #     wlan_sta.active(True)
# # # # # #     wlan_mac = wlan_sta.config('mac')
# # # # # #     print(ubinascii.hexlify(wlan_mac).decode())

# # # # # #     send_to_firebase(sensor_data)

# # # # # #     # while True:
# # # # # #         try:
# # # # # #             sensor.measure()  # Measure temperature and humidity
# # # # # #             temp = sensor.temperature()  # Get temperature
# # # # # #             humidity = sensor.humidity()  # Get humidity
# # # # # #             moisture_level = ao_pin.read()  # Value from 0 to 1023

# # # # # #             print("Moisture Level:", moisture_level)
# # # # # #             print('Temperature: {:.2f}°C'.format(temp))
# # # # # #             print('Humidity: {:.2f}%'.format(humidity))

# # # # # #     #     except OSError as e:
# # # # # #     #         print('Failed to read sensor.')
        
# # # # # #     #     time.sleep(2)
# # # # # # else:
# # # # # #     machine.reset()

# # # # # ######################################################################
# # # # # import urequests
# # # # # import ujson
# # # # # import time
# # # # # import machine
# # # # # import dht

# # # # # # Wi-Fi manager from your previous code
# # # # # from wifimgr import WifiManager

# # # # # # Firebase configuration
# # # # # FIREBASE_URL = "https://irridate-b5b0a-default-rtdb.firebaseio.com/"
# # # # # API_KEY = "AIzaSyDCr-6ucuulvgfHHnoV10MaTii7lPOCaj0"  # Replace with your Firebase API key

# # # # # # User credentials for Firebase Authentication
# # # # # tokentokentoken = "test@test.com"  # Replace with your tokentokentoken
# # # # # password = "123456789"  # Replace with your password

# # # # # # Set up the sensor
# # # # # dht_pin = machine.Pin(2)  # Assuming DHT22 sensor is connected to GPIO 2
# # # # # sensor = dht.DHT22(dht_pin)

# # # # # # ADC pin for moisture sensor (assuming analog pin)
# # # # # moisture_sensor_pin = machine.ADC(0)

# # # # # wm = WifiManager()
# # # # # wm.connect()

# # # # # # Function to get ID token using tokentokentoken and password
# # # # # def get_id_token(tokentokentoken, password):
# # # # #     url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
# # # # #     payload = {
# # # # #         "tokentokentoken": email,
# # # # #         "password": password,
# # # # #         "returnSecureToken": True
# # # # #     }
# # # # #     headers = {
# # # # #         "Content-Type": "application/json"
# # # # #     }
    
# # # # #     try:
# # # # #         # response = urequests.post(url, data=ujson.dumps(payload), headers=headers)
# # # # #         response = urequests.post(url, data=ujson.dumps(payload), headers=headers, timeout=10)
# # # # #         result = response.json()
# # # # #         response.close()
# # # # #         if 'idToken' in result:
# # # # #             print("Successfully authenticated.")
# # # # #             return result['idToken']
# # # # #         else:
# # # # #             print("Authentication failed:", result)
# # # # #             return None
# # # # #     except Exception as e:
# # # # #         print("Error during authentication:", e)
# # # # #         return None

# # # # # # Function to send data to Firebase using ID token
# # # # # def send_to_firebase(data, id_token):
# # # # #     headers = {
# # # # #         "Content-Type": "application/json"
# # # # #     }
# # # # #     url = FIREBASE_URL + "/sensor_data.json?auth=" + id_token  # Change 'sensor_data' to whatever path you'd like

# # # # #     response = urequests.post(url, data=ujson.dumps(data), headers=headers)
# # # # #     print("Firebase Response:", response.text)
# # # # #     response.close()

# # # # # # Main function to measure and send sensor data
# # # # # def main():
# # # # #     if wm.is_connected():
# # # # #         print("Connected to WiFi")
        
# # # # #         # Authenticate user and get ID token
# # # # #         id_token = get_id_token(email, password)
# # # # #         if id_token:
# # # # #             while True:
# # # # #                 try:
# # # # #                     # Measure temperature and humidity
# # # # #                     sensor.measure()
# # # # #                     temp = sensor.temperature()  # Get temperature in Celsius
# # # # #                     humidity = sensor.humidity()  # Get humidity in percentage
# # # # #                     moisture_level = moisture_sensor_pin.read()  # Read moisture level (0 to 1023)

# # # # #                     # Print sensor values
# # # # #                     print("Moisture Level:", moisture_level)
# # # # #                     print('Temperature: {:.2f}°C'.format(temp))
# # # # #                     print('Humidity: {:.2f}%'.format(humidity))

# # # # #                     # Prepare the data to send
# # # # #                     sensor_data = {
# # # # #                         "temperature": temp,
# # # # #                         "humidity": humidity,
# # # # #                         "moisture_level": moisture_level,
# # # # #                         "timestamp": time.time()
# # # # #                     }

# # # # #                     # Send data to Firebase
# # # # #                     send_to_firebase(sensor_data, id_token)
                    
# # # # #                     # Sleep for a while before measuring again (e.g., 10 seconds)
# # # # #                     time.sleep(10)

# # # # #                 except OSError as e:
# # # # #                     print('Failed to read sensor:', e)

# # # # #         else:
# # # # #             print("Unable to get ID token.")
# # # # #     else:
# # # # #         print("Failed to connect to WiFi.")
# # # # #         machine.reset()

# # # # # # Run the main function
# # # # # if __name__ == '__main__':
# # # # #     main()

# # # # import urequests
# # # # import ujson
# # # # import time
# # # # import machine
# # # # import dht
# # # # from wifimgr import WifiManager
# # # # from machine import Pin, ADC
# # # # import socket

# # # # # Firebase configuration
# # # # FIREBASE_URL = "https://irridate-b5b0a-default-rtdb.firebaseio.com/"

# # # # # Email to be updated when received from the app
# # # # user_email = None

# # # # # Set up the sensor
# # # # dht_pin = machine.Pin(2)  # Assuming DHT22 sensor is connected to GPIO 2
# # # # sensor = dht.DHT22(dht_pin)

# # # # moisture_sensor_pin = machine.ADC(0)  # Assuming analog pin for moisture sensor

# # # # wm = WifiManager()
# # # # wm.connect()

# # # # # Function to send data to Firebase using email (as ID token)
# # # # def send_to_firebase(data, email):
# # # #     headers = {
# # # #         "Content-Type": "application/json"
# # # #     }
# # # #     url = FIREBASE_URL + f"/sensor_data.json?auth={email}"  # Use the email as the ID token
    
# # # #     response = urequests.post(url, data=ujson.dumps(data), headers=headers)
# # # #     print("Firebase Response:", response.text)
# # # #     response.close()

# # # # # Function to handle HTTP requests from the React Native app
# # # # def handle_client(client_socket):
# # # #     global token
# # # #     request = client_socket.recv(1024)
# # # #     request = str(request)
    
# # # #     if "POST /post-expoPushToken" in request:
# # # #         json_data = request.split("\r\n\r\n")[1]
# # # #         tokentokentoken_data = ujson.loads(json_data)
# # # #         token = tokentokentoken_data['token']  # Capture the user's tokentokentoken
# # # #         print(f"Received tokentokentoken: {token}")
# # # #         response = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{\"status\": \"tokentokentoken received\"}"
# # # #     else:
# # # #         response = "HTTP/1.1 404 Not Found\r\n\r\n"
    
# # # #     client_socket.send(response)
# # # #     client_socket.close()

# # # # # Main function to handle Wi-Fi connection and sensor data processing
# # # # def main():
# # # #     if wm.is_connected():
# # # #         print("Connected to WiFi")

# # # #         server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # # #         server_socket.bind(('0.0.0.0', 80))
# # # #         server_socket.listen(5)
# # # #         print("Server listening on port 80")

# # # #         while True:
# # # #             client_socket, addr = server_socket.accept()
# # # #             handle_client(client_socket)  # Wait for the tokentokentoken from the React Native app

# # # #             if token:  # Check if the tokentokentoken has been received
# # # #                 try:
# # # #                     # Measure temperature and humidity
# # # #                     sensor.measure()
# # # #                     temp = sensor.temperature()  # Temperature in Celsius
# # # #                     humidity = sensor.humidity()  # Humidity percentage
# # # #                     moisture_level = moisture_sensor_pin.read()  # Moisture level (0 to 1023)

# # # #                     # Prepare the data to send
# # # #                     sensor_data = {
# # # #                         "temperature": temp,
# # # #                         "humidity": humidity,
# # # #                         "moisture_level": moisture_level,
# # # #                         "timestamp": time.time(),
# # # #                         "tokentokentoken": token
# # # #                     }

# # # #                     # Send data to Firebase using the tokentokentoken as the identifier
# # # #                     send_to_firebase(sensor_data, token)
                    
# # # #                     # Sleep for a while before measuring again (e.g., 10 seconds)
# # # #                     time.sleep(10)

# # # #                 except OSError as e:
# # # #                     print('Failed to read sensor:', e)
# # # #             else:
# # # #                 print("Waiting for tokentokentoken from the React Native app...")

# # # #     else:
# # # #         print("Failed to connect to WiFi.")
# # # #         machine.reset()

# # # # # Run the main function
# # # # if __name__ == '__main__':
# # # #     main()

# # # import urequests
# # # import ujson
# # # import time
# # # import machine
# # # import dht
# # # from wifimgr import WifiManager
# # # from machine import Pin, ADC
# # # import socket

# # # # Firebase configuration
# # # FIREBASE_URL = "https://irridate-b5b0a-default-rtdb.firebaseio.com/"

# # # # Variable to store the received expoPushToken
# # # user_expoPushToken = None

# # # # Set up the sensor
# # # dht_pin = machine.Pin(2)  # Assuming DHT22 sensor is connected to GPIO 2
# # # sensor = dht.DHT22(dht_pin)

# # # moisture_sensor_pin = machine.ADC(0)  # Assuming analog pin for moisture sensor

# # # # Initialize WiFi Manager
# # # wm = WifiManager()
# # # wm.connect()

# # # # Function to send data to Firebase using the expoPushToken
# # # def send_to_firebase(data, expoPushToken):
# # #     headers = {
# # #         "Content-Type": "application/json"
# # #     }
# # #     # Use the expoPushToken as the identifier in Firebase
# # #     url = FIREBASE_URL + f"/sensor_data.json?auth={expoPushToken}"
    
# # #     response = urequests.post(url, data=ujson.dumps(data), headers=headers)
# # #     print("Firebase Response:", response.text)
# # #     response.close()

# # # # Function to handle incoming HTTP requests from the React Native app
# # # # def handle_client(client_socket):
# # # #     global user_expoPushToken
# # # #     request = client_socket.recv(1024)
# # # #     request = str(request)
# # # #     print(request)

# # # #     # Look for a POST request to /post-expoPushToken
# # # #     if "POST /post-expoPushToken" in request:
# # # #         json_data = request.split("\r\n\r\n")[1]  # Get the JSON body from the request
# # # #         expoPushToken_data = ujson.loads(json_data)  # Parse the JSON
# # # #         print(expoPushToken_data)
# # # #         user_expoPushToken = expoPushToken_data['token']  # Capture the expoPushToken
# # # #         print(f"Received expoPushToken: {user_expoPushToken}")
        
# # # #         # Send response to client
# # # #         response = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{\"status\": \"expoPushToken received\"}"
# # # #     else:
# # # #         # If not the expected request, send 404 Not Found
# # # #         response = "HTTP/1.1 404 Not Found\r\n\r\n"
    
# # # #     client_socket.send(response)
# # # #     client_socket.close()

# # # def handle_client(client_socket):
# # #     global user_expoPushToken
# # #     request = client_socket.recv(1024)
# # #     request = str(request)
# # #     print(request)

# # #     # Ensure there is a JSON body in the request
# # #     parts = request.split("\r\n\r\n")
# # #     if len(parts) > 1:
# # #         json_data = parts[1]  # Get the JSON body from the request
# # #         expoPushToken_data = ujson.loads(json_data)  # Parse the JSON
# # #         print(expoPushToken_data)
# # #         user_expoPushToken = expoPushToken_data['token']  # Capture the expoPushToken
# # #         print(f"Received expoPushToken: {user_expoPushToken}")
        
# # #         # Send response to client
# # #         response = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{\"status\": \"expoPushToken received\"}"
# # #     else:
# # #         # If not the expected request, send 404 Not Found
# # #         response = "HTTP/1.1 404 Not Found\r\n\r\n"
    
# # #     client_socket.send(response)
# # #     client_socket.close()
# # # # Main function to handle Wi-Fi connection and sensor data processing
# # # def main():
# # #     if wm.is_connected():
# # #         print("Connected to WiFi")

# # #         # Set up the server to listen for connections
# # #         server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # #         server_socket.bind(('0.0.0.0', 80))
# # #         server_socket.listen(5)
# # #         print("Server listening on port 80")

# # #         while True:
# # #             print("jsndjnfds")
# # #             client_socket, addr = server_socket.accept()
# # #             handle_client(client_socket)  # Handle incoming request
# # #             print("Waiting for client connection...")

# # #             # Check if we have received the expoPushToken
# # #             if user_expoPushToken:
# # #                 try:
# # #                     # Measure temperature and humidity
# # #                     sensor.measure()
# # #                     temp = sensor.temperature()  # Temperature in Celsius
# # #                     humidity = sensor.humidity()  # Humidity percentage
# # #                     moisture_level = moisture_sensor_pin.read()  # Moisture level (0 to 1023)

# # #                     # Prepare the data to send
# # #                     sensor_data = {
# # #                         "temperature": temp,
# # #                         "humidity": humidity,
# # #                         "moisture_level": moisture_level,
# # #                         "timestamp": time.time(),
# # #                         "expoPushToken": user_expoPushToken
# # #                     }

# # #                     # Send data to Firebase
# # #                     send_to_firebase(sensor_data, user_expoPushToken)
                    
# # #                     # Sleep for a while before measuring again (e.g., 10 seconds)
# # #                     time.sleep(10)

# # #                 except OSError as e:
# # #                     print('Failed to read sensor:', e)
# # #             else:
# # #                 print("Waiting for expoPushToken from the React Native app...")

# # #     else:
# # #         print("Failed to connect to WiFi.")
# # #         machine.reset()

# # # # Run the main function
# # # if __name__ == '__main__':
# # #     main()

# # import urequests
# # import ujson
# # import time
# # import machine
# # import dht
# # from wifimgr import WifiManager
# # from machine import Pin, ADC
# # import socket

# # # Firebase configuration
# # FIREBASE_URL = "https://irridate-b5b0a-default-rtdb.firebaseio.com/"

# # # Variable to store the received expoPushToken
# # user_expoPushToken = None

# # # Set up the sensor
# # dht_pin = machine.Pin(2)  # Assuming DHT22 sensor is connected to GPIO 2
# # sensor = dht.DHT22(dht_pin)

# # moisture_sensor_pin = machine.ADC(0)  # Assuming analog pin for moisture sensor

# # # Initialize WiFi Manager
# # wm = WifiManager()
# # wm.connect()

# # # Function to send data to Firebase using the expoPushToken
# # def send_to_firebase(data, expoPushToken):
# #     headers = {
# #         "Content-Type": "application/json"
# #     }
# #     # Use the expoPushToken as the identifier in Firebase
# #     url = FIREBASE_URL + f"/sensor_data.json?auth={expoPushToken}"
    
# #     response = urequests.post(url, data=ujson.dumps(data), headers=headers)
# #     print("Firebase Response:", response.text)
# #     response.close()

# # # Function to handle incoming HTTP requests from the React Native app
# # def handle_client(client_socket):
# #     global user_expoPushToken
# #     request = client_socket.recv(1024)
# #     request = request.decode('utf-8')  # Ensure request is decoded properly
# #     print("Full Request:", request)  # Debugging: print the full request to check its structure

# #     # Look for a POST request to /post-expoPushToken
# #     if "POST /post-expoPushToken" in request:
# #         try:
# #             if "\r\n\r\n" in request:
# #                 json_data = request.split("\r\n\r\n")[1]  # Get the JSON body from the request
# #                 expoPushToken_data = ujson.loads(json_data)  # Parse the JSON
# #                 print("Received expoPushToken:", expoPushToken_data)  # Debugging
                
# #                 if 'token' in expoPushToken_data:
# #                     user_expoPushToken = expoPushToken_data['token']  # Capture the expoPushToken
# #                     print(f"expoPushToken: {user_expoPushToken}")

# #                     # Send response to client
# #                     response = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{\"status\": \"expoPushToken received\"}"
# #                 else:
# #                     response = "HTTP/1.1 400 Bad Request\r\n\r\n{\"error\": \"Invalid token format\"}"
# #             else:
# #                 response = "HTTP/1.1 400 Bad Request\r\n\r\n{\"error\": \"No JSON body found\"}"
# #         except Exception as e:
# #             print("Error processing request:", e)
# #             response = "HTTP/1.1 500 Internal Server Error\r\n\r\n{\"error\": \"Failed to process request\"}"
# #     else:
# #         # If not the expected request, send 404 Not Found
# #         response = "HTTP/1.1 404 Not Found\r\n\r\n"
    
# #     client_socket.send(response)
# #     client_socket.close()

# # # Main function to handle Wi-Fi connection and sensor data processing
# # def main():
# #     if wm.is_connected():
# #         print("Connected to WiFi")

# #         # Set up the server to listen for connections
# #         server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #         server_socket.bind(('0.0.0.0', 80))
# #         server_socket.listen(5)
# #         print("Server listening on port 80")

# #         while True:
# #             print("Waiting for client connection...")
# #             client_socket, addr = server_socket.accept()
# #             handle_client(client_socket)  # Handle incoming request

# #             # Check if we have received the expoPushToken
# #             if user_expoPushToken:
# #                 try:
# #                     # Measure temperature and humidity
# #                     sensor.measure()
# #                     temp = sensor.temperature()  # Temperature in Celsius
# #                     humidity = sensor.humidity()  # Humidity percentage
# #                     moisture_level = moisture_sensor_pin.read()  # Moisture level (0 to 1023)

# #                     # Prepare the data to send
# #                     sensor_data = {
# #                         "temperature": temp,
# #                         "humidity": humidity,
# #                         "moisture_level": moisture_level,
# #                         "timestamp": time.time(),
# #                         "expoPushToken": user_expoPushToken
# #                     }

# #                     # Send data to Firebase
# #                     send_to_firebase(sensor_data, user_expoPushToken)
                    
# #                     # Sleep for a while before measuring again (e.g., 10 seconds)
# #                     time.sleep(10)

# #                 except OSError as e:
# #                     print('Failed to read sensor:', e)
# #             else:
# #                 print("Waiting for expoPushToken from the React Native app...")

# #     else:
# #         print("Failed to connect to WiFi.")
# #         machine.reset()

# # # Run the main function
# # if __name__ == "__main__":
# #     main()

# import urequests
# import ujson
# import time
# import machine
# import dht
# from wifimgr import WifiManager
# from machine import Pin, ADC
# import socket

# # Firebase configuration
# FIREBASE_URL = "https://irridate-b5b0a-default-rtdb.firebaseio.com/"

# # Variable to store the received expoPushToken
# user_expoPushToken = None

# # Set up the sensor
# dht_pin = machine.Pin(2)  # Assuming DHT22 sensor is connected to GPIO 2
# sensor = dht.DHT22(dht_pin)

# moisture_sensor_pin = machine.ADC(0)  # Assuming analog pin for moisture sensor

# # Initialize WiFi Manager
# wm = WifiManager()
# wm.connect()

# # Function to send data to Firebase using the expoPushToken
# def send_to_firebase(data, expoPushToken):
#     headers = {
#         "Content-Type": "application/json"
#     }
#     # Use the expoPushToken as the identifier in Firebase
#     url = FIREBASE_URL + f"/sensor_data.json?auth={expoPushToken}"
    
#     response = urequests.post(url, data=ujson.dumps(data), headers=headers)
#     print("Firebase Response:", response.text)
#     response.close()

# # Function to handle incoming HTTP requests from the React Native app
# def handle_client(client_socket):
#     global user_expoPushToken
#     request = client_socket.recv(1024)
#     request = request.decode('utf-8')  # Ensure request is decoded properly
#     print("Full Request:", request)  # Debugging: print the full request to check its structure

#     # Look for a POST request to /post-expoPushToken
#     if "POST /post-expoPushToken" in request:
#         try:
#             if "\r\n\r\n" in request:
#                 # Split and extract the JSON part of the body
#                 json_data = request.split("\r\n\r\n")[1]
#                 print("Raw JSON data:", json_data)  # Debug: Print the raw JSON data before parsing

#                 # Try parsing the JSON
#                 try:
#                     expoPushToken_data = ujson.loads(json_data)  # Parse the JSON
#                     print("Parsed expoPushToken_data:", expoPushToken_data)  # Debugging

#                     # Check if 'token' is in the received JSON data
#                     if 'token' in expoPushToken_data:
#                         user_expoPushToken = expoPushToken_data['token']  # Capture the expoPushToken
#                         print(f"Received expoPushToken: {user_expoPushToken}")

#                         # Send response to client
#                         response = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{\"status\": \"expoPushToken received\"}"
#                     else:
#                         response = "HTTP/1.1 400 Bad Request\r\n\r\n{\"error\": \"Invalid token format\"}"

#                 except ValueError as e:
#                     print(f"JSON parsing error: {e}")  # If JSON is invalid, show error
#                     response = "HTTP/1.1 400 Bad Request\r\n\r\n{\"error\": \"Invalid JSON\"}"
#             else:
#                 response = "HTTP/1.1 400 Bad Request\r\n\r\n{\"error\": \"No JSON body found\"}"
#         except Exception as e:
#             print(f"Error processing request: {e}")
#             response = "HTTP/1.1 500 Internal Server Error\r\n\r\n{\"error\": \"Failed to process request\"}"
#     else:
#         # If not the expected request, send 404 Not Found
#         response = "HTTP/1.1 404 Not Found\r\n\r\n"
    
#     client_socket.send(response)
#     client_socket.close()

# # Main function to handle Wi-Fi connection and sensor data processing
# def main():
#     if wm.is_connected():
#         print("Connected to WiFi")

#         # Set up the server to listen for connections
#         server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         server_socket.bind(('0.0.0.0', 80))
#         server_socket.listen(5)
#         print("Server listening on port 80")

#         client_socket, addr = server_socket.accept()
#         handle_client(client_socket)  

#         while True:
#             # print("Waiting for client connection...")
#             # client_socket, addr = server_socket.accept()
#             # handle_client(client_socket)  # Handle incoming request

#             # Check if we have received the expoPushToken
#             if user_expoPushToken:
#                 try:
#                     # Measure temperature and humidity
#                     sensor.measure()
#                     temp = sensor.temperature()  # Temperature in Celsius
#                     humidity = sensor.humidity()  # Humidity percentage
#                     moisture_level = moisture_sensor_pin.read()  # Moisture level (0 to 1023)

#                     # Prepare the data to send
#                     sensor_data = {
#                         "temperature": temp,
#                         "humidity": humidity,
#                         "moisture_level": moisture_level,
#                         "timestamp": time.time(),
#                         "expoPushToken": user_expoPushToken
#                     }

#                     # Send data to Firebase
#                     send_to_firebase(sensor_data, user_expoPushToken)
                    
#                     # Sleep for a while before measuring again (e.g., 10 seconds)
#                     time.sleep(10)

#                 except OSError as e:
#                     print('Failed to read sensor:', e)
#             else:
#                 print("Waiting for expoPushToken from the React Native app...")

#     else:
#         print("Failed to connect to WiFi.")
#         machine.reset()

# # Run the main function
# if __name__ == "__main__":
#     main()

import urequests
import ujson
import time
import machine
import dht
from wifimgr import WifiManager
from machine import Pin, ADC
import socket

# Backend server configuration
BACKEND_URL = "http://104.194.105.145:5001/predict"  # Change <your_backend_ip> to your backend's IP address

# Variable to store the received expoPushToken
user_expoPushToken = None

# Set up the sensor
dht_pin = machine.Pin(2)  # Assuming DHT22 sensor is connected to GPIO 2
sensor = dht.DHT22(dht_pin)

moisture_sensor_pin = machine.ADC(0)  # Assuming analog pin for moisture sensor



# Initialize WiFi Manager
wm = WifiManager()
wm.connect()

# Function to send data to the backend using the expoPushToken
def send_to_backend(data, expoPushToken):
    headers = {
        "Content-Type": "application/json"
    }
    # Prepare the payload to send
    payload = ujson.dumps({
        "input_value": [data["temperature"], data["moisture_level"]],
        "expo_push_token": expoPushToken
    })
    
    # Send a POST request to the backend
    response = urequests.post(BACKEND_URL, data=payload, headers=headers)
    print("Backend Response:", response.text)
    response.close()

# Function to handle incoming HTTP requests from the React Native app
def handle_client(client_socket):
    global user_expoPushToken
    request = client_socket.recv(1024)
    request = request.decode('utf-8')  # Ensure request is decoded properly
    print("Full Request:", request)  # Debugging: print the full request to check its structure

    # Look for a POST request to /post-expoPushToken
    if "POST /post-expoPushToken" in request:
        try:
            if "\r\n\r\n" in request:
                # Split and extract the JSON part of the body
                json_data = request.split("\r\n\r\n")[1]
                print("Raw JSON data:", json_data)  # Debug: Print the raw JSON data before parsing

                # Try parsing the JSON
                try:
                    expoPushToken_data = ujson.loads(json_data)  # Parse the JSON
                    print("Parsed expoPushToken_data:", expoPushToken_data)  # Debugging

                    # Check if 'token' is in the received JSON data
                    if 'token' in expoPushToken_data:
                        user_expoPushToken = expoPushToken_data['token']  # Capture the expoPushToken
                        print(f"Received expoPushToken: {user_expoPushToken}")

                        # Send response to client
                        response = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{\"status\": \"expoPushToken received\"}"
                    else:
                        response = "HTTP/1.1 400 Bad Request\r\n\r\n{\"error\": \"Invalid token format\"}"

                except ValueError as e:
                    print(f"JSON parsing error: {e}")  # If JSON is invalid, show error
                    response = "HTTP/1.1 400 Bad Request\r\n\r\n{\"error\": \"Invalid JSON\"}"
            else:
                response = "HTTP/1.1 400 Bad Request\r\n\r\n{\"error\": \"No JSON body found\"}"
        except Exception as e:
            print(f"Error processing request: {e}")
            response = "HTTP/1.1 500 Internal Server Error\r\n\r\n{\"error\": \"Failed to process request\"}"
    else:
        # If not the expected request, send 404 Not Found
        response = "HTTP/1.1 404 Not Found\r\n\r\n"
    
    client_socket.send(response)
    client_socket.close()

# Main function to handle Wi-Fi connection and sensor data processing
def main():
    if wm.is_connected():
        print("Connected to WiFi")

        # Set up the server to listen for connections
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', 80))
        server_socket.listen(5)
        print("Server listening on port 80")

        sensor.measure()
        temp = sensor.temperature()  # Temperature in Celsius
        humidity = sensor.humidity()  # Humidity percentage
        moisture_level = moisture_sensor_pin.read()
        # temp = 40.0
        # moisture_level = 150
        # humidity = 60   

        print("Moisture Level:", moisture_level)
        print('Temperature: {:.2f}°C'.format(temp))
        print('Humidity: {:.2f}%'.format(humidity))

        client_socket, addr = server_socket.accept()
        handle_client(client_socket)  

        while True:
            # Check if we have received the expoPushToken
            if user_expoPushToken:
                try:
                    # Measure temperature and humidity
                    sensor.measure()
                    temp = sensor.temperature()  # Temperature in Celsius
                    humidity = sensor.humidity()  # Humidity percentage
                    moisture_level = moisture_sensor_pin.read()  # Moisture level (0 to 1023)

                    # temp = 40.0
                    # moisture_level = 150
                    # humidity = 60   

                    # Prepare the data to send
                    sensor_data = {
                        "temperature": temp,
                        "humidity": humidity,
                        "moisture_level": moisture_level,
                        "timestamp": time.time(),
                    }

                    print("Sensor Data:", sensor_data)  # Debugging

                    # Send data to backend
                    send_to_backend(sensor_data, user_expoPushToken)
                    
                    # Sleep for a while before measuring again (e.g., 10 seconds)
                    time.sleep(10)

                except OSError as e:
                    print('Failed to read sensor:', e)
            # else:
            #     print("Waiting for expoPushToken from the React Native app...")

    else:
        print("Failed to connect to WiFi.")
        machine.reset()

# Run the main function
if __name__ == "__main__":
    main()