import sqlite3

# Custom course table names (sanitized)
COURSE_CATEGORIES = [
    'international_marketing',
    'business_app_dev',
    'business_db_mgmt',
    'prog_logic_analytic_thinking',
    'intro_managerial_finance'
]

def create_tables():
    # Connect to the SQLite database (will create it if it doesn't exist)
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()

    # Loop through course list and create each table
    for course in COURSE_CATEGORIES:
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {course} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                option_a TEXT NOT NULL,
                option_b TEXT NOT NULL,
                option_c TEXT NOT NULL,
                option_d TEXT NOT NULL,
                correct_option TEXT NOT NULL
            );
        ''')
        print(f"Table created: {course}")

    conn.commit()
    conn.close()
    print("✅ All tables created successfully.")

if __name__ == "__main__":
    create_tables()
