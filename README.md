<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</div>

<h1 align="center">💡 Guidance Hub 🧭</h1>

<p align="center">
  A dynamic web application built with Django to provide engineering students with structured, clear, and interactive career roadmaps.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="License">
</p>

---

### 🎯 Project Aim

The journey through an engineering degree is filled with choices, but often lacks a clear, consolidated guide on how to translate academic knowledge into a successful career. Students frequently struggle to understand the vast array of job roles available, the specific skills required for each, and the logical steps to acquire them.

**Guidance Hub** was created to solve this problem. It serves as a centralized, step-by-step guide that demystifies career paths across all major engineering disciplines. By providing detailed, hierarchical roadmaps, the platform empowers students to make informed decisions, and build a solid foundation for their professional future with confidence and clarity.

---

### ✨ Features

* **Comprehensive Roadmap Structure:** The core of the application is a deeply nested content system that guides users from a general **Branch** (e.g., Computer Engineering) to a specialized **Domain** (e.g., Software & Web Development), then to a specific **Job Role** (e.g., Frontend Developer), and finally through a detailed timeline of **Roadmap Steps**.
* **Dynamic Content Management:** All content, including branches, domains, job roles, and roadmap steps, is managed entirely through the Django Admin Panel. This allows for easy updates, maintenance, and expansion without touching the source code.
* **User Authentication and Profiles:** A complete and secure system for user registration, login, and logout. Each user has a personal profile where they can add and update their details, including their full name, academic information, and a profile picture.
* **Modern and Responsive UI:** The entire website is built with Tailwind CSS for a clean, professional, and fully responsive design that works seamlessly on desktops, tablets, and mobile devices. It features a rich user interface with a dynamic stardust background and a light/dark mode theme selector.

---

### 🚀 Technologies Used

* **Backend:**
    * [Python](https://www.python.org/)
    * [Django](https://www.djangoproject.com/) (Web Framework)
* **Frontend:**
    * HTML5
    * [Tailwind CSS](https://tailwindcss.com/) (CSS Framework)
    * JavaScript
* **Database:**
    * SQLite (Default Django development database)
* **Data Import:**
    * Beautiful Soup (for scraping static HTML files)

---

### ⚙️ Installation & Setup (Local Development)

Follow these steps to get a local copy of the project up and running on your machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/hemanthdareddy/GuidanceHub.git](https://github.com/hemanthdareddy/GuidanceHub.git)
    cd GuidanceHub
    ```
   
2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install django beautifulsoup4
    ```

5.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create your admin credentials.

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8.  Open your web browser and go to `http://127.0.0.1:8000/`.

---

### 📸 Screenshots
---

### 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or find any bugs, please open an issue or submit a pull request.

---

### 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

### 📧 Contact

Hemanth Dareddy - [hemanthdareddy@gmail.com](mailto:hemanthdareddy@gmail.com)

Project Link: [https://github.com/hemanthdareddy/GuidanceHub](https://github.com/hemanthdareddy/GuidanceHub)

LinkedIn - [https://www.linkedin.com/in/hemanth-dareddy](https://www.linkedin.com/in/hemanth-dareddy?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
```eof
