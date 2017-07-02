# pytest
Twist Python Challenge
This pytest project is actually a small event management program. where you can create parties, and then add/remove friends in general, and specifically to parties. As a challenge we give you a broken partial project to boot.

Each friend should specifies an image_url leading to an image which will be his avatar, the django server then goes ahead and downloads the url contents and saves it for later use.

Please follow these steps to complete the process:
1. Make the code run using manage.py runserver (fix all dependency, compilation and runtime errors).
2. Add additional endpoints to the API to support add/removing friends from parties.
3. Assuming users send links that are slow or even very slow, download the image in the background using django best
   practices. urls such as:
   http://slowwly.robertomurray.co.uk/delay/10000/url/http://synbiobeta.com/wp-content/uploads/sites/4/2014/05/Twist-Bioscience-1.jpg
5. Add permissions so only django users can create parties.
6. Add a feature to send each friend an email when they've joined a party.
4. document your steps in steps.txt
5. Good luck, see you on the other side!