# 📊 Dashboard Project - Full Stack (FastAPI + HTML/JS/CSS)

## 📂 Project Structure
```
dashboard/                # Frontend Folder
├── index.html             # Main Dashboard UI
├── dashboard.js           # Fetches and displays reports from backend
├── styles.css              # Simple and clean CSS for UI

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
uvicorn main:app --reload
```

Backend will start at:
```
http://localhost:8000
```

### 2️⃣ Start the Frontend (HTML Dashboard)

Navigate to `dashboard` folder and use one of these methods:

#### Option A: Python HTTP Server (Quickest)
```bash
python -m http.server 8080
```
Open browser at:
```
http://localhost:8080/index.html
```

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
fetch('http://localhost:8000/reports')
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
│   ├── styles.css             # Styling
```

---

## ✅ Important Notes
- **Backend must run before frontend tries to fetch data.**
- Make sure backend runs at `http://localhost:8000`, otherwise change `dashboard.js`.
- Use **a proper local server** (like `http.server` or `Live Server`). Don't just double-click the HTML file directly, or fetch won't work due to CORS issues.

---

## 💬 Need Help?
If you want, I can also create a starter pack zip with all these files + a working example of `main.py`, `index.html`, `dashboard.js`, and `styles.css`. Want me to generate that for you? 😎

