PROJECT OVERVIEW

The system exists to support individuals in understanding and improving their emotional well-being by tracking key daily activities like sleep, exercise, and meditation. The primary goal of the system is to provide personalized mood predictions based on these activities, helping users gain insights into how their lifestyle choices impact their emotional state.
By logging data such as the number of hours slept, the type and duration of exercise, and time spent meditating, the system analyzes patterns in the user’s behavior and predicts their mood. This allows users to take proactive steps toward improving their mental and physical health. In terms of supporting the organization’s mission, this system aligns with the goal of promoting health and well-being. It empowers users to track and adjust their daily habits, encouraging healthier lifestyles. 

Included Features:
User Registration & Login: Users can create an account or log into an existing one using a username and password.
Data Entry for Mood Prediction: Once logged in, users can input data about their sleep hours, exercise minutes, exercise type and intensity, and meditation minutes.
Mood Prediction: Based on the entered data, the system predicts the user's mood (e.g., "Happy", "Stressed", "Calm", etc.).
Data Persistence: The system stores user data, such as login credentials and daily data (sleep, exercise, meditation), in a local JSON file.
Error Handling: The system ensures that inputs are valid (e.g., no negative numbers or invalid data), and provides error messages if incorrect data is entered.

Excluded Features:
Social Features: The system does not include features like social interaction, sharing of data, or interaction with other users.
Advanced Mood Analysis: Mood prediction is based on simple conditions, and it does not analyze complex psychological data or provide in-depth mental health insights.
Real-time Data Sync: Data is saved locally and is not synchronized across devices or users.
Customizable User Profiles: The system does not allow for extensive customization of user profiles, such as avatars or personalized settings beyond the basic login credentials.

Target Users:
General Users: Individuals looking to track and predict their mood based on their daily health and wellness activities, such as students, employees, or anyone interested in understanding how sleep, exercise, and meditation affect their mood.
New Users: People who may be unfamiliar with mood-tracking applications and prefer a straightforward, easy-to-use interface to track their daily health metrics.
Specific, Measurable Outcomes (SMART Goals)
Specific: The project will create a user-friendly application that allows individuals to track their sleep, exercise, and meditation data to predict their mood. The app will include features like user registration, data input, and mood prediction.


Measurable:
The application will have at least 500 active users within the first 6 months of launch.
Users will input daily data (sleep, exercise, meditation) at least 3 times per week on average.
The mood prediction feature will correctly analyze user input and predict mood with 90% accuracy based on predefined criteria.
Achievable: The app will be designed with simple and intuitive user interfaces, using existing technologies such as Python (Tkinter for GUI and JSON for data storage). Given the availability of the necessary resources (time, technology, and team), achieving these outcomes is feasible.


Relevant: The project addresses the growing need for people to understand the relationship between their physical and mental health. It provides a tool for individuals to track and improve their well-being by offering a simple way to monitor their habits and mood.


Time-bound:
The app will be fully developed and ready for initial testing within 3 months.
After the first 3 months, user feedback will be collected to refine the application.
By the end of 6 months, the app will be promoted to a larger user base, aiming for 500 active users.


PYTHON CONCEPTS AND LIBRARIES

Python Tkinter
Tkinter's Role in My Application:
Creating the GUI Structure: Tkinter is used to build the primary windows and dialog boxes that the user interacts with. This includes the welcome window, login/register window, and data input window.
User Input: Tkinter’s widgets like Entry(), Combobox(), and Button() allow users to input their data (username, password, exercise details) and submit it for processing.
Event Handling: Tkinter helps in managing user interactions through event handlers attached to buttons, such as the registration, login, and submit buttons.
User Feedback: Tkinter's messagebox is used to provide feedback to the user, including error messages, confirmation of successful actions, and the mood prediction result.
Navigation Between Windows: Tkinter's Toplevel() widget is used to create separate windows for data input and mood prediction, allowing smooth transitions between different stages of the application.
Key Tkinter Widgets and Functions:
Tk(): Creates the main window for the application (open_welcome_window()).
Toplevel(): Creates new windows, like the data input window after login.
Label(): Displays text or instructions (e.g., "Welcome to VibeTrack!").
Entry(): Collects input from the user, such as the username, password, and other data (sleep hours, exercise minutes).
Button(): Executes commands when clicked (e.g., register, login, or submit data).
Combobox(): Allows the user to choose from a list of options (exercise type, exercise intensity).
messagebox: Displays error or information pop-ups (e.g., when there are login errors or when data is successfully submitted).
pack(): Organizes widgets within a window (it controls widget layout).
config(): Sets window background color and other attributes.
mainloop(): Starts the Tkinter event loop to keep the application running.




SUSTAINABLE DEVELOPMENT GOALS
This project is connected to Sustainable Development Goal (SDG) 3: Good Health and Well-being, which focuses on helping people live healthier and happier lives. The application, VibeTrack, encourages users to take care of their mental and physical health by tracking everyday activities like sleep, exercise, and meditation. It predicts moods based on these habits, making it easier for users to understand their well-being and take steps to improve it.
VibeTrack supports SDG 3 by focusing on three main areas:
Sleep: Sleep is essential for feeling refreshed and staying healthy. The app helps users keep track of how much they sleep, encouraging good rest habits.
Exercise: Physical activity is important for both the body and the mind. By tracking exercise type, duration, and intensity, the app helps users stay active and understand how exercise impacts their mood.
Meditation: Practicing mindfulness or meditation can reduce stress and improve emotional balance. The app encourages this by tracking meditation time as part of daily habits.
This project is designed to be simple and easy to use, so anyone can benefit from it. By promoting healthy daily routines, VibeTrack helps people feel better and supports the global goal of improving health and well-being for everyone.




PROGRAM/SYSTEM INSTRUCTIONS
Key Features:
User Registration and Login:
Users can register by providing a username and password.
Login is required for accessing the mood tracking features. The credentials are validated against the data stored in a JSON file.
Mood Prediction:
The system predicts the user's mood based on their input, which includes hours of sleep, minutes of exercise, meditation minutes, and exercise intensity.
The mood prediction considers various conditions, like the amount of sleep and exercise, and offers moods like "Happy", "Stressed", "Calm", etc.
GUI Layout:
The app uses tkinter to create a friendly interface with labels, buttons, and input fields for users to enter their daily data.
The data is saved locally in a JSON file, allowing for persistent storage across sessions.
Data Validation:
The application checks that the entered data falls within acceptable ranges (e.g., sleep hours between 0 and 24) and validates that the exercise intensity and type are correct.
Error Handling:
If any required information is missing or if the data input is invalid, an error message is shown to the user.

Flow of the application:
Welcome Screen:
The user is greeted with a welcome message and a "Start" button. When the user clicks "Start," it opens the next window where they can either register or log in.
Login/Registration:
The user is presented with fields to enter a username and password.
Registration: If the user doesn't have an account, they can click "Register" to create one. The system checks if the username is already taken and ensures the password meets the required length.
Login: If the user already has an account, they can log in by entering their credentials. The system verifies that the username exists and the password matches.
Data Input:
After a successful login, the user is taken to a new window where they can enter their daily health data:
Sleep hours: How many hours they slept that day.
Exercise type: The type of exercise they did (Aerobic, Strength Training, etc.).
Exercise minutes: How long they exercised.
Exercise intensity: How intense the exercise was (Low, Moderate, High).
Meditation minutes: How much time they spent meditating.
The user must fill in these fields, and the system ensures the data entered is valid (e.g., sleep hours between 0 and 24, exercise minutes as a positive number).
Mood Prediction:
Once the data is submitted, the system analyzes the input and predicts the user's mood based on predefined criteria (such as sleep, exercise, and meditation levels).
The possible moods include "Stressed", "Happy", "Calm", "Energized", or "Neutral". A message box will show the predicted mood.
Saving Data:
The user’s data is saved locally in a JSON file, so they can access it later. The file contains the user's name, password, and the health data entered.
Error Handling:
Throughout the process, if the user enters invalid data (such as negative numbers or missing fields), an error message will appear, prompting the user to correct the issue.





