# 📝 Flask To-Do List App

A simple and interactive **To-Do List web application** built with **Flask**, **SQLAlchemy**, and **HTML/CSS**.  
Users can **add**, **toggle**, and **delete** tasks — all stored in a local database.

---

## 🚀 Features

✅ Add new tasks  
✅ Mark tasks as completed or pending  
✅ Delete tasks  
✅ Clean and responsive user interface  
✅ Uses SQLite for persistent storage  

## 🧩 Project Structure


```
flask-todo-list/
│
├── app/
│   ├── **init**.py           # Flask app initialization
│   ├── models.py             # Database models (Task class)
│   ├── routes/               # Route blueprints
│   ├── static/               # CSS and JS files
│   ├── templates/            # HTML templates (Jinja2)
│   └── instance/             # SQLite DB and config (auto-created)
│
├── run.py                    # Main entry point to run Flask app
├── requirements.txt          # Python dependencies
├── sample.css                # Extra style file (optional)
└── README.md                 # Documentation file

````

---

## ⚙️ Installation and Setup

### 1️⃣ Clone this repository

```bash
git clone https://github.com/anu-0035/To-Do-App.git
cd To-Do-App
````

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

### 3️⃣ Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Flask app

```bash
python run.py
```

Now visit 👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** in your browser.

---

## 🗄️ Database

* Uses **SQLite** via **SQLAlchemy ORM**
* Default database file is auto-created in the `instance/` folder
  (e.g., `instance/site.db`)

---

## 🧰 Technologies Used

* **Python 3**
* **Flask**
* **Flask SQLAlchemy**
* **Jinja2 Templates**
* **HTML5 / CSS3 / Bootstrap**


---

## 👨‍💻 Author

**Anubhav Prasad**
GitHub: [@anu-0035](https://github.com/anu-0035)

---

## 🪪 License

This project is open source and available under the [MIT License](LICENSE).




