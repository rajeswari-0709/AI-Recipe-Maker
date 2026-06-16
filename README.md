# 🍳 AI Recipe Maker – Snap, Speak & Cook

An AI-powered full-stack web application that generates recipes from ingredient images, text input, or voice input.

The project uses a PyTorch-based YOLOv8 model for ingredient/object detection and GPT-based language models for recipe generation.

---

## 🚀 Features

- User Registration & Login
- Ingredient Input through Text
- Voice Input using Speech Recognition
- Ingredient Image Upload
- YOLOv8 Object Detection
- AI Recipe Generation using GPT
- Recipe History Tracking
- SQLite Database
- Responsive UI

---

## 🛠️ Tech Stack

### Backend
- Python
- Django

### AI / Machine Learning
- PyTorch
- YOLOv8 (Ultralytics)
- OpenAI/OpenRouter API

### Frontend
- HTML
- CSS
- JavaScript

### Database
- SQLite

---

## 📂 Project Structure

```text
AI_Recipe_Maker/
│
├── manage.py
├── requirements.txt
├── .env
│
├── recipe_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── recipe_app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── ingredient_detector.py
│   │
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── history.html
│   │
│   └── static/
│       ├── style.css
│       └── script.js
│
└── media/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Recipe-Maker.git

cd AI-Recipe-Maker
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root folder:

```env
OPENAI_API_KEY=YOUR_API_KEY
```

For OpenRouter:

```env
OPENAI_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxx
```

---

## 🗄️ Database Setup

```bash
python manage.py makemigrations

python manage.py migrate
```

Create admin user:

```bash
python manage.py createsuperuser
```

---

## ▶️ Run Project

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## 📸 Application Workflow

### Image-Based Recipe Generation

1. Upload ingredient image
2. YOLOv8 detects objects
3. Detected ingredients are extracted
4. GPT generates recipe
5. Recipe is stored in database

### Voice-Based Recipe Generation

1. Click "Speak Ingredients"
2. Speak ingredients
3. Speech is converted to text
4. GPT generates recipe
5. Recipe is saved in history

---

## 🤖 AI Workflow

```text
Image Upload / Voice Input
            ↓
      Ingredient Detection
            ↓
      Ingredient Extraction
            ↓
         GPT Model
            ↓
      Recipe Generation
            ↓
        SQLite DB
            ↓
       History Page
```

---

## 🔮 Future Improvements

- Better food-specific ingredient detection
- Nutrition analysis
- Calorie estimation
- Recipe recommendations
- Dark mode
- Docker deployment
- Cloud hosting

---

## 👨‍💻 Author

Developed as an AI-powered full-stack project using Django, PyTorch, YOLOv8, GPT APIs, HTML, CSS, and JavaScript.
