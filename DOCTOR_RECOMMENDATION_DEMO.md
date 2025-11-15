# 🏥 Location-Based Doctor Recommendation System

## ✅ Status: LIVE & WORKING

Your AI chatbot now intelligently recommends doctors based on location and specialty!

---

## 🎯 Features

✅ **Smart Location Detection** - Automatically detects city from user queries  
✅ **Specialty Search** - Finds oncologists, endocrinologists, general physicians  
✅ **Location Prompts** - Asks for city if not specified  
✅ **Detailed Information** - Name, hospital, address, phone, fees, timings, ratings  
✅ **AI-Powered Responses** - Gemini provides friendly introductions to recommendations  

---

## 📍 Available Locations

- **Indore** (7 doctors)
- **Bangalore** (3 doctors)  
- **Mumbai** (1 doctor)

---

## 🔍 How It Works

### Scenario 1️⃣: Doctor + City Specified
**User:** "Show me oncologists in Bangalore"

**AI Response:**
```
Okay, here are a couple of highly-rated oncologists in Bangalore who might be a good fit for you.

Recommended Oncologists in Bangalore:

1. Dr. Suresh Kumar
   Specialty: Medical Oncologist
   Hospital: Manipal Hospital, Bangalore
   Address: 98, HAL Airport Road, Bangalore - 560017
   Phone: +91 80 25023333
   Experience: 22 years
   Consultation Fee: ₹1200
   Timings: Mon-Sat: 10:00 AM - 5:00 PM
   Rating: ⭐⭐⭐⭐ (4.8/5)

2. Dr. Priya Desai
   Specialty: Surgical Oncologist
   Hospital: Columbia Asia Hospital, Bangalore
   Address: Kirloskar Business Park, Hebbal, Bangalore - 560024
   Phone: +91 80 66144444
   Experience: 15 years
   Consultation Fee: ₹1000
   Timings: Mon-Fri: 9:00 AM - 4:00 PM
   Rating: ⭐⭐⭐⭐ (4.7/5)
```

---

### Scenario 2️⃣: Doctor Without City
**User:** "I need an endocrinologist"

**AI Response:**
```
I'd be happy to help you find a doctor! Which city are you looking for? 
I have doctor information for: Indore, Bangalore, Mumbai
```

---

### Scenario 3️⃣: All Doctors in a City
**User:** "Show me doctors in Indore"

**AI Response:**
```
Here are some highly-rated doctors in Indore! (Shows top 5 across all specialties)

1. Dr. Rajesh Sharma - Medical Oncologist, Bombay Hospital
2. Dr. Priya Mehta - Surgical Oncologist, CHL Hospital
3. Dr. Anil Gupta - Radiation Oncologist, Choithram Hospital
4. Dr. Sunita Verma - Endocrinologist, Medanta Hospital
5. Dr. Vikram Singh - Endocrinologist, Apollo Hospital
```

---

### Scenario 4️⃣: Regular Medical Query (Non-Doctor)
**User:** "What are symptoms of diabetes?"

**AI Response:**
```
Oh, I understand you're curious about the symptoms of diabetes. 
That's a great question to ask and shows you're being proactive about your health!

[...empathetic medical information from Gemini AI...]
```

---

## 🧪 Test Commands

### Test via Python:
```python
from ml_model.ai_chatbot import AIChatbot

chatbot = AIChatbot()

# Test 1: Specific search
result = chatbot.chat("I need oncologist in Mumbai")
print(result['response'])

# Test 2: Location prompt
result = chatbot.chat("Find me a good doctor")
print(result['response'])

# Test 3: Specialty search
result = chatbot.chat("diabetes doctor in Indore")
print(result['response'])
```

### Test via API:
```bash
# Search for cancer doctor in Mumbai
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "I need a cancer doctor in Mumbai"}'

# Ask for endocrinologist without location
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "Show me endocrinologists"}'

# Find all doctors in Bangalore
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "doctors in Bangalore"}'
```

---

## 📊 Sample Data Structure

**data/doctors.json:**
```json
{
  "indore": {
    "oncologists": [
      {
        "name": "Rajesh Sharma",
        "specialty": "Medical Oncologist",
        "hospital": "Bombay Hospital, Indore",
        "address": "Scheme No. 94, Ring Road, Indore - 452010",
        "phone": "+91 731 4242100",
        "experience": "18 years",
        "fee": 1000,
        "timings": "Mon-Sat: 10:00 AM - 6:00 PM",
        "rating": 4.8
      }
      // ... more doctors
    ],
    "endocrinologists": [...],
    "general_physicians": [...]
  },
  "bangalore": {...},
  "mumbai": {...}
}
```

---

## 🎨 Specialty Detection Keywords

| Keyword | Maps To |
|---------|---------|
| oncologist, cancer | oncologists |
| endocrinologist, diabetes, thyroid | endocrinologists |
| general, physician | general_physicians |

---

## 🔮 Future Enhancements

🔹 Add more cities (Delhi, Chennai, Hyderabad, etc.)  
🔹 Real-time availability checking  
🔹 Online appointment booking integration  
🔹 User reviews and ratings system  
🔹 Filter by fee range, experience, hospital  
🔹 Map integration for hospital locations  
🔹 Telemedicine availability indicator  

---

## 🚀 How to Add More Doctors

Edit `data/doctors.json`:

```json
{
  "delhi": {
    "oncologists": [
      {
        "name": "Doctor Name",
        "specialty": "Medical Oncologist",
        "hospital": "Hospital Name, Delhi",
        "address": "Full address with pincode",
        "phone": "+91 11 XXXXXXXX",
        "experience": "XX years",
        "fee": 1500,
        "timings": "Mon-Sat: 10:00 AM - 6:00 PM",
        "rating": 4.5
      }
    ]
  }
}
```

**No code changes needed!** AI will automatically detect new cities.

---

## ✅ Tested & Verified

- ✅ Location detection (Indore, Bangalore, Mumbai)
- ✅ Specialty search (oncologist, endocrinologist, physician)
- ✅ Location prompt when city missing
- ✅ AI-powered friendly introductions
- ✅ Full contact details display
- ✅ Emoji ratings rendering (⭐⭐⭐⭐)
- ✅ API endpoint integration
- ✅ Committed to git (commit 8b068c6)
- ✅ Pushed to GitHub

---

## 📞 Example User Flows

### Flow 1: Quick Search
1. User: "cancer doctor bangalore"
2. AI: Shows 2-3 oncologists in Bangalore with details

### Flow 2: Interactive Search
1. User: "I need diabetes specialist"
2. AI: "Which city? I have info for: Indore, Bangalore, Mumbai"
3. User: "Indore"
4. AI: Shows endocrinologists in Indore

### Flow 3: Mixed Query
1. User: "I have persistent cough and need doctor in Mumbai"
2. AI: Provides health advice + shows general physicians in Mumbai

---

**🎉 Your AI chatbot is now a complete medical assistant with doctor recommendations!**
