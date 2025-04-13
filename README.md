
### I added the subject Finance to the quiz bowl since I only have 4 classes this semester


# QA3
#  Quiz Bowl Application

This Python-based Quiz Bowl application provides two interactive user interfaces:

 **Administrator Interface**: For adding, viewing, editing, and deleting quiz questions (password-protected).
 **Quiz Taker Interface**: For students to take quizzes by selecting a category and answering multiple-choice questions.

Built with **Python** and **Tkinter**, backed by an **SQLite** database.

---
##  How to Navigate the Quiz Bowl GUI

Here is a step-by-step guide for navigating and using the GUI:

---

###  Main Menu (main.py)

When you launch the app, you will see:

- **"Administrator Login"** button
- **"Take a Quiz"** button

🖱 Click one with your mouse  
⌨ Or press `Tab` to switch between buttons and `Enter` to select

---

###  Administrator Dashboard

After entering the admin password (`admin123`), you’ll see:

- ➕ Add New Question  
- 📋 View Questions  
- 🛠️ Edit/Delete Questions  
- 🚪 Logout

Use your **mouse to click** a function, or:
- Press `Tab` to highlight a button
- Press `Enter` to open it

---

###  Add New Question

1. Select a course category:
   - 🖱 Use the dropdown menu
   - ⌨ Press `Tab` to focus it, use `Down/Up Arrow` keys to choose, then press `Enter`

2. Fill in the fields:
   - Use `Tab` to move between "Question", "Option A", etc.
   - Type your content using the keyboard

3. Submit:
   - Tab to the **"Submit"** button and press `Enter`
   - Tab to **"Back"** and press `Enter` to return to the dashboard

---

###  Edit/Delete Questions

1. Select a category from the dropdown (as above)
2. Click or press `Enter` on **Load Questions**
3. Use your **mouse** or **arrow keys** to select a question in the list
4. After selecting, the fields below will auto-fill
5. Edit the content by tabbing through the entries
6. Use:
   - **Update Question** to save changes
   - **Delete Selected Question** to remove it
   - **Back** to return

---

###  View Questions

1. Select a category
2. Click **Load Questions**
3. A scrollable text area shows all questions for that course
4. Click **Back** to return

---

###  Taking a Quiz

1. From the main menu, click or press `Tab` to highlight **"Take a Quiz"**, then `Enter`
2. Select a course from the dropdown (use mouse or arrow keys)
3. Click or tab to **"Start Quiz"**, press `Enter`
4. Each question screen shows:
   - The question
   - Four radio buttons (A–D) for answer options

5. To answer:
   - Click your choice OR
   - Press `Tab` to highlight an option, use `Space` or `Enter` to select

6. Click or tab to **"Submit Answer"** and press `Enter`
7. You will see feedback after each question
8. After all questions, you’ll see your final score
9. Click **Take Another Quiz** or **Exit**

---

📝 Note: Popups like “Correct!” or “Error” must be closed manually by clicking “OK” or pressing `Enter`.



