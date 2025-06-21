
📅 Appointment Manager

A Django-based web application designed to help businesses efficiently schedule and manage client appointments.
-----------------------------------------------------------

🔍 Overview
Appointment Manager is a simple yet powerful system that allows users to register, log in, and manage appointments with clients. The app supports adding clients, scheduling appointments without time conflicts, searching through appointments, and editing or deleting existing entries.
---------------------------------------------------------
✨ Features
•	👤 User registration and authentication using Django's built-in system.
•	👥 Add, view, and manage clients.
•	📆 Schedule appointments with date, start/end times, and comments.
•	⛔ Conflict detection to prevent overlapping appointments.
•	📋 Paginated appointment listings with search functionality.
•	✏️ Edit and delete appointments with confirmation prompts.
•	📱 Responsive design using Bootstrap 5.
•	🔔 Reminder notifications for upcoming appointments (placeholder for future integration).

------------------------------------------------------
🛠 Technologies
•	🐍 Python 3.x
•	🌐 Django Web Framework
•	🎨 Bootstrap 5 (frontend styling)
•	🗃 SQLite (default database)
-----------------------------------------------------

🚀 Setup and Installation

1.	Clone the repository:
  git clone https://github.com/BoraZeneli/appointment-manager.git
  cd appointment-manager

2.	Create and activate a virtual environment:
  python -m venv env
  On Windows: env\Scripts\activate
  On macOS/Linux: source env/bin/activate

3.	Install dependencies:
  pip install -r requirements.txt

4.	Apply database migrations:
  python manage.py migrate

5.	Create a superuser:
  python manage.py createsuperuser

6.	Run the development server:
  python manage.py runserver

7.	Access the application:
  Application: http://127.0.0.1:8000/
  Admin panel: http://127.0.0.1:8000/admin/

---------------------------------------------------------

📝 Usage
•	Register or log in to your account.
•	Add new clients with their contact details.
•	Schedule appointments ensuring no time conflicts.
•	Search appointments by client name.
•	Edit or delete appointments as needed.
•	Use the admin panel for advanced management.

----------------------------------------------------------------

💾 Database

Default: SQLite
Suitable for development and small-scale deployments.
Easily replaceable with PostgreSQL or MySQL in production by updating settings.py.

----------------------------------------------------------------------------------

🔮 Future Improvements
•	✉️ Implement email/SMS notifications for appointment reminders.
•	📅 Add calendar view for easier appointment visualization.
•	👤 Allow client profile management and history tracking.
•	🔐 Add role-based permissions and an admin dashboard.

----------------------------------------------------------------------------------
🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, open an issue first to discuss your ideas.

----------------------------------------------------------------------------

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
