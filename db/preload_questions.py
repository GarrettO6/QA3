import sqlite3

sample_data = {
    "international_marketing": [
        ("What is the primary goal of international marketing?", "To increase local brand awareness", "To improve HR policies", "To develop global markets", "To reduce product costs", "C"),
        ("Which factor most influences cultural differences in global markets?", "Economic growth", "Language and values", "Distribution channels", "Local laws", "B"),
        ("Which element is critical when entering a foreign market?", "Time zone", "Currency symbols", "Legal regulations", "National holidays", "C"),
        ("What does localization involve?", "Translating code", "Changing headquarters", "Adapting to local culture", "Switching suppliers", "C"),
        ("Which is an entry strategy into international markets?", "Foreign direct investment", "Internal hiring", "Blog marketing", "Subcontracting", "A"),
        ("Why is pricing challenging in global marketing?", "Too many laws", "Currency fluctuations", "Marketing budget limits", "Government bans", "B"),
        ("What is global branding?", "Creating unique local names", "Standardizing marketing across markets", "Hiring international staff", "Designing new packaging", "B"),
        ("A 'glocal' strategy is best described as:", "Going global without change", "Only local efforts", "Global vision with local adaptation", "Ignoring international differences", "C"),
        ("Which organization regulates international trade?", "WTO", "NASA", "NATO", "WHO", "A"),
        ("Market segmentation in global marketing is based on:", "Usernames", "Nationality alone", "Cultural, geographic, economic factors", "Blood type", "C"),
    ],
    "business_app_dev": [
        ("Which language is commonly used for web development?", "Python", "JavaScript", "C++", "Excel", "B"),
        ("What is a wireframe in app development?", "Code snippet", "Database tool", "Blueprint for UI", "Framework plugin", "C"),
        ("What is version control?", "Cloud backup", "Tool for testing apps", "Managing changes to source code", "User authentication", "C"),
        ("Which is NOT a backend technology?", "Django", "Flask", "Node.js", "Figma", "D"),
        ("Which one is a frontend library?", "React", "PostgreSQL", "MySQL", "Django", "A"),
        ("What does CRUD stand for?", "Create, Read, Update, Delete", "Copy, Run, Upload, Deploy", "Code, Render, Undo, Debug", "Create, Reuse, Update, Design", "A"),
        ("Which protocol is commonly used in APIs?", "HTML", "FTP", "HTTP", "SMTP", "C"),
        ("What is a framework?", "Tool to track time", "A structured way to build software", "Hardware simulator", "A type of spreadsheet", "B"),
        ("What does debugging involve?", "Writing tests", "Removing bugs from code", "Installing software", "Translating code", "B"),
        ("In software development, an IDE is:", "A database system", "A design framework", "Integrated Development Environment", "A graphic editor", "C"),
    ],
    "business_db_mgmt": [
        ("Which SQL statement is used to update data?", "CHANGE", "MODIFY", "UPDATE", "ALTER", "C"),
        ("What is a foreign key?", "A key from another table", "A secure password", "Primary key backup", "A table label", "A"),
        ("Which clause limits query results?", "WHERE", "HAVING", "LIMIT", "TOP", "C"),
        ("What does normalization do?", "Deletes old data", "Reduces redundancy", "Encrypts records", "Changes schema", "B"),
        ("Which database is relational?", "MongoDB", "PostgreSQL", "Redis", "Neo4j", "B"),
        ("What does SELECT * do?", "Deletes everything", "Selects all columns", "Renames table", "Sorts records", "B"),
        ("In ER diagrams, what is an entity?", "Attribute", "Table column", "Real-world object or concept", "Foreign key", "C"),
        ("What is the function of a primary key?", "Generate invoices", "Track login attempts", "Ensure unique identity of rows", "Join all tables", "C"),
        ("What is a transaction in databases?", "Data duplication", "Sequence of operations executed as a unit", "Backup restore", "Report summary", "B"),
        ("Which command removes a table?", "DELETE TABLE", "DROP", "ERASE", "CLEAR", "B"),
    ],
    "prog_logic_analytic_thinking": [
        ("What is a flowchart used for?", "Database design", "Displaying program logic", "Defining variables", "None of the above", "B"),
        ("Which keyword begins a loop?", "if", "loop", "for", "return", "C"),
        ("Which type of logic gate returns true if both inputs are true?", "AND", "OR", "NOT", "NAND", "A"),
        ("What is a variable?", "Fixed value", "Storage location for data", "Output device", "Compiler", "B"),
        ("Which of the following is a decision structure?", "if-else", "while", "import", "input", "A"),
        ("What is an algorithm?", "A flowchart symbol", "Step-by-step instructions", "UI layout", "Data set", "B"),
        ("Which data type holds decimals?", "int", "float", "bool", "char", "B"),
        ("Which logic gate inverts the input?", "AND", "OR", "NOT", "XOR", "C"),
        ("What does a loop do?", "Deletes data", "Repeats instructions", "Saves files", "Exits program", "B"),
        ("Which is NOT a valid operator?", "+", "==", "if", "%", "C"),
    ],
    "intro_managerial_finance": [
        ("What is capital budgeting?", "Marketing strategy", "Deciding long-term investments", "Stock pricing", "Sales forecasting", "B"),
        ("Which is a source of long-term financing?", "Credit card", "Trade payable", "Bonds", "Short-term loans", "C"),
        ("Which statement shows a firm's profitability?", "Balance Sheet", "Cash Flow", "Income Statement", "Equity Report", "C"),
        ("What does liquidity refer to?", "Profitability", "Ability to repay long-term debt", "Ease of converting assets to cash", "Amount of revenue", "C"),
        ("What is the time value of money?", "Money has the same value over time", "Future money is worth more", "Present money is worth more", "Interest never matters", "C"),
        ("Which ratio measures debt risk?", "P/E ratio", "Debt-to-equity", "ROI", "EPS", "B"),
        ("What does diversification do?", "Increases risk", "Reduces risk", "Increases taxes", "Reduces interest", "B"),
        ("What is working capital?", "Assets minus revenue", "Assets plus equity", "Current assets - current liabilities", "Equity - liabilities", "C"),
        ("Which cost is not affected by production?", "Variable cost", "Fixed cost", "Direct cost", "Labor cost", "B"),
        ("Who are stakeholders?", "Only shareholders", "Employees only", "Any party affected by the firm", "Vendors only", "C"),
    ]
}

def insert_unique_questions():
    conn = sqlite3.connect("quiz_bowl.db")
    cursor = conn.cursor()

    for table, questions in sample_data.items():
        added_count = 0
        for q in questions:
            cursor.execute(f'''
                SELECT COUNT(*) FROM {table}
                WHERE question = ?
            ''', (q[0],))
            exists = cursor.fetchone()[0]

            if not exists:
                cursor.execute(f'''
                    INSERT INTO {table} (question, option_a, option_b, option_c, option_d, correct_option)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', q)
                added_count += 1

        print(f"✅ {added_count} new question(s) added to {table}")

    conn.commit()
    conn.close()
    print("🎉 Done checking and inserting unique questions!")

if __name__ == "__main__":
    insert_unique_questions()
