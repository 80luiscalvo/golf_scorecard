Golf Scorecard App
A simple Golf Scorecard app built with Python and Kivy. The app allows users to manage their golf scores, select golf courses, and store user information including a randomly generated PIN for future use.

Features
Home Screen: Welcome screen with a button to start the app.
Settings Screen: Allows users to input their handicap, select a golf course, and view a randomly generated 4-digit PIN.
Score Screen: Lets users record scores for 18 holes of golf and displays the total score.
User Data Storage: User data (email, PIN, handicap, and selected course) is saved in a JSON file (current_users.json).
Requirements
Python 3.x
Kivy library
JSON file to store user data
Installation
Step 1: Install Python
Ensure that you have Python 3.x installed on your system. You can download the latest version of Python from python.org.

Step 2: Install Kivy
You can install Kivy via pip:

bash
Copy code
pip install kivy
Step 3: Clone or Download the Repository
Clone the repository to your local machine or download the project files:

bash
Copy code
git clone https://github.com/yourusername/golfscorecard-app.git
Alternatively, you can download the zip file of this repository and extract it to your desired location.

Step 4: Install Dependencies
No additional dependencies are needed besides Kivy. If you'd like to keep a virtual environment, you can set up one using the following commands:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
pip install kivy
Step 5: Run the App
Once all the dependencies are installed, navigate to the directory where the project files are located, and run the app using the following command:

bash
Copy code
python main.py
This will launch the app, and you can start interacting with the Golf Scorecard application.

File Structure
bash
Copy code
golfscorecard-app/
│
├── main.py                 # Main Python application code
├── golfscorecard.kv        # Kivy UI layout (kv file)
├── current_users.json      # JSON file to store user data
└── README.md               # Project README
main.py: Contains the logic for the app, including handling user input and storing data in the JSON file.
golfscorecard.kv: The layout for the Kivy screens, which defines the UI structure.
current_users.json: A JSON file that stores user details like email, PIN, handicap, and selected course.
JSON Structure
The current_users.json file has the following structure:

json
Copy code
{
    "current user": [
        {
            "email": "",
            "PIN_Number": "1234",
            "handicap": "",
            "course": ""
        }
    ]
}
email: Stores the email address of the user.
PIN_Number: A randomly generated 4-digit PIN for the user.
handicap: The user's golf handicap.
course: The golf course selected by the user.
How to Use
Step 1: Home Screen
Upon launching the app, you will be greeted with the home screen.
Click on the "Start" button to proceed to the Settings screen.
Step 2: Settings Screen
Handicap: Enter your golf handicap.
Select Course: Choose a golf course from the dropdown list (e.g., Sunnyvale Golf Course or Green Valley Country Club).
PIN Number: A 4-digit PIN is automatically generated and displayed in this section. It is saved with the user data.
Click on "Go" to save your settings and proceed to the Score screen.
Step 3: Score Screen
Here, you can record the scores for each hole (1 to 18).
As you enter the scores, the total score will automatically be calculated.
You can also click the "Home" button to go back to the home screen.
Step 4: Saving Data
The entered data (email, PIN number, handicap, and selected course) is saved in current_users.json.
Customizing the App
Courses: To add more golf courses, simply modify the course_data dictionary in main.py.
Handicap Input: The handicap input can accept only integers. You can modify the range of acceptable input as needed.
Known Issues
Ensure that the current_users.json file exists in the same directory as the app. If it doesn't, the app will attempt to create it on first run.
On some systems, you may need to install additional dependencies for Kivy, such as pygame.
Contributing
If you would like to contribute to this project, please feel free to fork the repository, create a branch, and submit a pull request with your improvements or bug fixes.

License
This project is licensed under the MIT License – see the LICENSE file for details.

This README provides an overview of how to install, use, and contribute to the project. It should be placed in the root directory of your project, so users can easily access information about the app.