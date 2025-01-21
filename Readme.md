# CSV Data Aggregation Web Application

## Description
This is a Django-based web application that allows users to upload a CSV file, store its data in a database, and perform aggregations (sum, average, min, max) on selected columns via the UI.

## Tech Stack
- Backend: Django
- Frontend: HTML, JavaScript
- Database: PostgreSQL

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the database in `settings.py`.
5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Start the server:
   ```bash
   python manage.py runserver
   ```

## How to Use
1. Upload a CSV file via the "Upload" form on the home page.
2. Use the dropdowns to select columns and an aggregation type.
3. Click "Compute" to view the result.

## Sample Test Data
Example CSV file format:
```
column1,column2
10,20
30,40
50,60
```