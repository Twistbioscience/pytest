# pytest
Twist Python Challenge

This pytest project is actually a small event management program. where you can create parties, and then add/remove friends in general, and specifically to parties. As a challenge we give you a broken partial project to boot.

Each friend should specify an image_url leading to an image which will be his avatar, the django server then goes ahead and downloads the url contents and saves it for later use.

Please follow these steps to complete the process:
1. Make the code run using manage.py runserver (fix all dependency, compilation and runtime errors).
2. Add additional endpoints to the API to support adding/removing friends from parties.
3. Assuming users send links that are slow or even very slow, download the image using web application best
   practices. support urls such as:
   http://slowwly.robertomurray.co.uk/delay/10000/url/http://synbiobeta.com/wp-content/uploads/sites/4/2014/05/Twist-Bioscience-1.jpg
4. Add permissions so only admin users can create parties.
5. Add a feature to send each friend an email when they've joined a party.
6. Build a Dockerfile for your project and provide the commands for running the application using docker-compose (or similar).
7. Document relevant design and architecture decisions in the README
8. Provide instructions on how to run the app from scratch in the README (and how to setup the system dependencies if needed).
9. Verify that all the endpoints work using CLI tools such as httpie or cURL
10. Good luck, see you on the other side!

Notes:
- Python interpreter should be version 3.5 or later
- Adding extra system dependencies (like redis or rabbitmq) is OK if needed.
- Changing the database is OK if needed
- In order to submit the solution either send us a link to your fork of this repo (preferred way) or send a zip file with the source code
