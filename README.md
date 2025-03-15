# 📊 Smart Health Assistant Project - Full Stack (FastAPI + HTML/JS/CSS)

## 📂 Project Structure
```
dashboard/                # Frontend Folder
├── index.html             # Main Dashboard UI
├── dashboard.js           # Fetches and displays reports from backend

backend/                    # Backend Folder (FastAPI)
├── main.py                  # FastAPI application
```

---

## 🏠 Prerequisites

### ⚡ Backend
- Python 3.9+
- FastAPI
- Uvicorn

### 🌐 Frontend
- Modern browser (Chrome, Firefox, etc.)
- Local development server (recommended, see below)

---

## 🚀 How to Run

### 1️⃣ Start the Backend (FastAPI)

Navigate to `backend` folder and run:
```bash
uvicorn backend.main:app --reload
```

Backend will start at:
```
http://localhost:8000 (locally) 
```
But as we are running the backend in render.com so no need to specify any port.

### 2️⃣ Start the Frontend (HTML Dashboard)

Navigate to `dashboard` folder and use one of these methods:

#### Option A: Python HTTP Server (Quickest)
```bash
python -m http.server 8080
```
Open browser at:
```
http://localhost:8080/index.html (locally)
```
Here also we are directly deploying from Github so no need to specify any port like - 8080. 

#### Option B: VS Code Live Server (Recommended for VS Code Users)
- Install **Live Server** extension.
- Right-click `index.html` and choose "Open with Live Server".

#### Option C: Node.js Serve (If you have Node.js installed)
```bash
npx serve
```
Open browser at the URL shown (usually something like `http://localhost:3000`).

---

## 🔗 Backend API Endpoint

| Method | Endpoint          | Description                   |
|---|---|---|
| GET   | `/reports`   | Fetches all reports for dashboard  |

---

## ⚙️ Example Fetch Code (in `dashboard.js`)

```javascript
fetch('http://localhost:8000/reports') (locally)
    .then(response => response.json())
    .then(data => {
        // Populate dashboard with data
    })
    .catch(error => console.error('Error fetching reports:', error));
```

---

## 💁 Folder Structure Example
```
project-root/
├── backend/
│   ├── main.py              # FastAPI backend
├── dashboard/
│   ├── index.html            # Dashboard UI
│   ├── dashboard.js          # Fetch and display logic
```

---

## ✅ Important Notes
- **Backend must run before frontend tries to fetch data.**
- Make sure backend runs at `http://localhost:8000`, otherwise change `dashboard.js`.
- Use **a proper local server** (like `http.server` or `Live Server`). Don't just double-click the HTML file directly, or fetch won't work due to CORS issues.

---




