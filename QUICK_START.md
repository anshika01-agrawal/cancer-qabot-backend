# 🚀 Quick Start Guide

**Last Updated:** November 15, 2025

## Start Server

```bash
uvicorn main:app --reload --port 8000
```

Server will start at: **http://localhost:8000**

---

## 🌐 Access the Application

| Page | URL | Description |
|------|-----|-------------|
| **Landing** | http://localhost:8000/ | Main website |
| **Dashboard** | http://localhost:8000/dashboard | AI Chatbot & Features |
| **Auth** | http://localhost:8000/auth | Login/Signup |

---

## 💬 Test AI Chatbot

### Via Dashboard UI:
1. Open http://localhost:8000/dashboard
2. Type in the chatbot:
   - "I need oncologist in Mumbai"
   - "Show me endocrinologists in Bangalore"
   - "What are symptoms of diabetes?"

### Via API:
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "I need oncologist in Mumbai"}'
```

---

## 🏥 Doctor Search Examples

| Query | Response |
|-------|----------|
| "I need oncologist in Mumbai" | Dr. Neeraj Mehta (Tata Memorial, 4.9★) |
| "Show me endocrinologists" | "Which city? Indore, Bangalore, Mumbai" |
| "diabetes doctor in Indore" | 2 endocrinologists with details |
| "doctors in Bangalore" | Top 5 doctors (all specialties) |

**Available Cities:** Indore, Bangalore, Mumbai  
**Specialties:** Oncologist, Endocrinologist, General Physician

---

## 🧪 Test Disease Prediction

### Via API:
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"symptoms": "persistent cough, chest pain"}'
```

**Response:** Disease prediction with 83.33% accuracy

---

## 🔑 Environment Setup

Create `.env` file:
```bash
GOOGLE_API_KEY=your_google_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_key_here
```

**Get API Keys:**
- Google Gemini: https://ai.google.dev/ (FREE, 60 req/min)
- Hugging Face: https://huggingface.co/settings/tokens (backup)

---

## 📊 Available Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Landing page |
| `/dashboard` | GET | Dashboard UI |
| `/auth` | GET | Login/Signup |
| `/chat` | POST | AI chatbot + doctor search |
| `/predict` | POST | ML disease prediction |

---

## 🎯 Key Features

✅ **AI Chatbot** - Google Gemini 2.0 Flash  
✅ **Doctor Search** - Location-based recommendations  
✅ **Disease Prediction** - ML with 83.33% accuracy  
✅ **Knowledge Base** - 15 medical topics  
✅ **Modern UI** - Purple gradient theme  
✅ **Responsive** - Works on all devices  

---

## 🐛 Troubleshooting

**Server not starting?**
```bash
pip install -r requirements.txt
```

**AI not working?**
- Check `.env` file has `GOOGLE_API_KEY`
- Verify API key is valid

**ML model error?**
```bash
python train_model.py
```

**Doctor search not working?**
- Check `data/doctors.json` exists
- Server logs should show "✓ Doctor database loaded"

---

## 📚 More Documentation

- **SYSTEM_STATUS.md** - Complete system overview
- **DOCTOR_RECOMMENDATION_DEMO.md** - Doctor search guide
- **AI_ML_REQUIREMENTS.md** - AI integration guide (685 lines)
- **README.md** - Full project documentation

---

## 🎊 You're All Set!

Visit http://localhost:8000 and start using your AI medical assistant!

**Questions?** Check SYSTEM_STATUS.md for detailed information.
