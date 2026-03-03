# 🚀 Project Management System (Python CLI)

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/madoyakimberley/project_management_python)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-green?style=for-the-badge&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)


A professional terminal-based **Project Management System** built with Python and the Rich library.

This project demonstrates strong Object-Oriented Programming (OOP) design combined with a clean and styled command-line interface.

---

## 🌟 Key Features

- 👤 User Management – Create and manage user profiles.
- 📁 Project Tracking – Organize work into projects with metadata.
- ✅ Task Management – Assign tasks and track progress.
- 💾 Persistent Storage – Data stored automatically in JSON.
- 🎨 Beautiful CLI – Styled interface using the Rich library.
- 🗑 Data Control – Delete users, projects, or tasks easily.

---

## 🏗 Project Structure

```
project_management_python/
│
├── main.py
├── requirements.txt
├── data/
│   └── data.json
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── project.py
│   └── task.py
│
└── utils/
    ├── __init__.py
    └── helpers.py
```

---

## 🛠 Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/madoyakimberley/project_management_python.git
cd project_management_python
```

### Create Virtual Environment (Recommended)

Mac / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is missing:

```bash
pip install rich pytest
```

---

## ▶️ Running the Application and tests

```bash
python main.py
```

```bash
pytest
```

---

## 💾 Data Persistence

Data is stored automatically in:

```
data/data.json
```

---

## 👨‍💻 Author

Kimberley
GitHub: https://github.com/madoyakimberley

---

## 📜 License

MIT License
