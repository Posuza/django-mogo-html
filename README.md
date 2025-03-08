# Django MongoDB Chat Application

A web application built with Django and MongoDB that appears to include chat functionality and user management.

## Overview

This project is a web application that combines Django's powerful web framework capabilities with MongoDB's flexible document database. The application includes chat functionality and user profile management.

## Requirements

- Python 3.x
- Django 4.2.5
- MongoDB
- pymongo 4.5.0
- dnspython 2.4.2
- Other dependencies as listed in `requirement.txt`

## Installation

1. Clone the repository:
  ```bash
  git clone cd django-mogo-html-main
  ```



2. Install the required packages:
  ```python
    pip install -r requirement.txt
  ```

3. Configure your MongoDB connection in the project settings.

4. Run migrations:

   ```python
     python manage.py migrate
   ```
5. Start the development server:
   ```python
    python manage.py runserver
   ```
## Features

- **User Management**: Create, update, and delete user profiles
- **Chat Interface**: Real-time chat functionality between users
- **Profile Viewing**: View other users' profiles with details like name, email, phone, and bio

## Project Structure

  - `app1/`: Main application directory
  - `templates/`: HTML templates
  - `index.html`: Home page template
  - `chats.html`: Chat interface template
  - `tests.py`: Test cases for the application

## Usage

 - After starting the server, navigate to `http://localhost:8000` in your web browser to access the application.

## Contributing

  1. Fork the repository
  2. Create your feature branch (`git checkout -b feature/amazing-feature`)
  3. Commit your changes (`git commit -m 'Add some amazing feature'`)
  4. Push to the branch (`git push origin feature/amazing-feature`)
  5. Open a Pull Request

## License

[Include license information here]

## Contact

  - posu0009@gmail.com

