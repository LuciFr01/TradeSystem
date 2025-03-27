# TradeSystem

## Overview
TradeSystem is a project aimed at implementing market parameter checks and suggesting the best possible option strategies. It is designed to fetch live Nifty 50 market data minute-wise, cache it, and continuously update as new data is received.

---

## 🚀 Features Implemented So Far

### ✅ Git Setup & Remote Configuration
- Initialized Git repository
- Set up remote repository on GitHub
- Configured `.gitignore` to exclude unnecessary files (`node_modules/`, `package-lock.json`)
- Committed and pushed project files

### ✅ Dependency Management
- Created `requirements.txt` using `pip freeze`
- Ensured easy installation of dependencies with `pip install -r requirements.txt`

### ✅ Real-Time Stock Data Fetching
- Started fetching Nifty 50 market data
- Implemented caching mechanism for last 20 days of minute-wise data
- Automated continuous data updates

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/LuciFr01/TradeSystem.git
cd TradeSystem
```

### 2️⃣ Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Ignore Unnecessary Files (Ensure `.gitignore` contains:)
```
node_modules/
package-lock.json
__pycache__/
.env
```

### 4️⃣ Configure Git Remote (If needed)
```bash
git remote set-url origin https://github.com/LuciFr01/TradeSystem.git
```

### 5️⃣ Commit and Push Code
```bash
git add .
git commit -m "Your commit message"
git push origin main
```

---

## 📅 Next Steps
- Implementing **real-time stock price analysis** using Angel Smart API
- Developing **market parameter analysis** for option strategies
- Optimizing backend performance for **faster processing**
- Improving UI for **better visualization**


