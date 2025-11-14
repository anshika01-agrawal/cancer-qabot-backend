# MediCare AI - Medical Disease Predictor & Health Assistant

A comprehensive medical chatbot platform with disease prediction, treatment recommendations, doctor/hospital finder, and health management dashboard.

## 🚀 Features

### 🤖 AI Chatbot
- Natural language symptom input
- Disease prediction based on symptoms
- Real-time conversational interface
- Quick-action symptom chips for faster input

### 💊 Health Management
- **Treatment Plans**: Personalized treatment recommendations
- **Medicine Database**: Medication information and dosages
- **Health Reports**: Track and view medical history
- **Critical Detection**: Automatic identification of emergency conditions

### 🏥 Healthcare Finder
- **Find Doctors**: Search specialists by specialty and location
- **Nearby Hospitals**: Location-based hospital finder with distance
- **Ratings & Reviews**: Doctor ratings and experience
- **Services**: Hospital facilities and available treatments

### 📊 Dashboard
- Clean, modern interface with sidebar navigation
- Multiple sections: Chatbot, Recommendations, Treatment, Medicines, Doctors, Hospitals, Reports, History
- Responsive design for all devices
- Real-time updates and notifications

### 🔐 Authentication
- User login and signup
- Profile management
- Secure session handling

## 📁 Project Structure

```
cancer-qabot-backend/
├── main.py                    # FastAPI backend server
├── requirements.txt           # Python dependencies
├── Procfile                   # Railway deployment config
├── AI_ML_REQUIREMENTS.md      # Complete AI/ML implementation guide
├── static/
│   ├── landing.html          # Homepage with features & CTA
│   ├── landing.css           # Landing page styles
│   ├── landing.js            # Landing page interactions
│   ├── dashboard.html        # Main dashboard interface
│   ├── dashboard.css         # Dashboard styling
│   ├── dashboard.js          # Dashboard functionality & chat
│   ├── login.html            # User login page
│   └── signup.html           # User registration page
└── README.md                  # This file
```

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **Uvicorn**: ASGI server
- **Pydantic**: Data validation

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients, animations
- **JavaScript**: Vanilla JS for interactivity
- **SVG**: Scalable vector graphics for icons

### Design
- **Inter Font**: Clean, professional typography
- **Gradient Theme**: Purple-blue gradient (#667eea to #764ba2)
- **Responsive**: Mobile-first design approach
- **Animations**: Smooth transitions and hover effects

## 🚦 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository** (if using Git):
```bash
git clone <repository-url>
cd cancer-qabot-backend
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the application**:
```bash
python main.py
```

4. **Open in browser**:
Navigate to `http://localhost:8000`

## 📡 API Endpoints

### Web Pages
- `GET /` - Landing page
- `GET /dashboard` - Dashboard interface
- `GET /login` - Login page
- `GET /signup` - Signup page

### API Routes
- `GET /ask?query=<text>` - Legacy endpoint for simple queries
- `POST /predict` - Disease prediction from symptoms

#### POST /predict Example
```json
Request:
{
  "symptoms": "I have a headache and fever"
}

Response:
{
  "disease": "Common Cold or Flu",
  "severity": "mild",
  "treatment": "Rest, hydration, over-the-counter medications",
  "recommendations": [
    "Take acetaminophen for fever",
    "Drink plenty of fluids",
    "Get adequate rest"
  ]
}
```

## 🎨 Features Overview

### Landing Page
- Hero section with animated robot illustration
- 6 key feature cards:
  - AI-Powered Chatbot
  - Disease Prediction
  - Treatment Plans
  - Find Doctors
  - Location Services
  - Health Reports
- How It Works section (3-step process)
- Call-to-action buttons
- Comprehensive footer with links

### Dashboard Sections

1. **AI Chatbot**
   - Welcome message with quick-action chips
   - Real-time message exchange
   - Typing indicators
   - Scroll-to-bottom on new messages

2. **Recommendations**
   - Empty state with call-to-action
   - Placeholder for personalized health tips

3. **Treatment Plans**
   - Disease-specific treatment protocols
   - Medication schedules
   - Follow-up reminders

4. **Medicines**
   - Searchable medicine database
   - Dosage information
   - Side effects and contraindications

5. **Find Doctors**
   - Search by specialty or name
   - Doctor cards with ratings
   - Years of experience
   - Location information

6. **Nearby Hospitals**
   - Location-based finder
   - Distance calculation
   - Available services
   - 24/7 indicator

7. **Health Reports**
   - Upload and view medical reports
   - History tracking
   - Lab results

8. **History**
   - Previous consultations
   - Chat history
   - Treatment timeline

## 🔧 Current Implementation Status

### ✅ Completed
- Complete landing page with animations
- Full dashboard HTML structure
- Responsive CSS styling for all pages
- JavaScript navigation and chat functionality
- Login/Signup pages with validation
- Backend API with placeholder prediction logic
- Static file serving
- Multiple page routes

### 🔄 In Progress (Requires AI/ML Implementation)
- Actual disease prediction model (currently keyword-based)
- NLP for symptom extraction
- Treatment recommendation engine
- Doctor/hospital database integration
- User authentication backend
- Session management

### 📋 TODO (See AI_ML_REQUIREMENTS.md)
- Train machine learning model on medical dataset
- Implement BioBERT or ClinicalBERT for NLP
- Create disease knowledge base
- Integrate geolocation services
- Add appointment scheduling
- Implement HIPAA compliance
- Multi-language support

## 🤖 AI/ML Implementation

The current `/predict` endpoint uses simple keyword matching. For production-ready disease prediction, see **AI_ML_REQUIREMENTS.md** which includes:

- NLP preprocessing strategies
- ML model architectures (classification, deep learning)
- Training data sources and requirements
- Knowledge base schemas
- Critical condition detection algorithms
- Conversational AI options (Rasa, GPT-4)
- Cost estimates and timelines
- Compliance considerations

**Estimated implementation**: 3-6 months for full AI/ML features

## 🌐 Deployment

### Railway (Recommended)
1. Connect GitHub repository to Railway
2. Railway auto-detects `Procfile`
3. Environment variables are set automatically
4. Deploy with one click

### Manual Deployment
```bash
# Ensure PORT environment variable is set
export PORT=8000

# Run production server
uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Docker (Optional)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

## ⚠️ Important Disclaimers

### Medical Disclaimer
**This chatbot provides general health information only and is NOT a substitute for professional medical advice, diagnosis, or treatment.**

- Always consult a qualified healthcare provider for medical concerns
- Never disregard professional medical advice
- In medical emergencies, call 911 immediately
- This system is for informational purposes only

### Development Status
This is a **prototype/educational project**. Before deploying to production:

1. Implement proper ML models (see AI_ML_REQUIREMENTS.md)
2. Validate with medical professionals
3. Ensure HIPAA compliance if handling patient data
4. Add proper error handling and logging
5. Implement security best practices
6. Consider medical malpractice insurance
7. Consult legal advisors regarding FDA regulations

## 📄 License

[Specify your license here - MIT, Apache 2.0, etc.]

## 👥 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📞 Support

For questions or issues:
- Open a GitHub issue
- Contact: [Your contact information]

## 🙏 Acknowledgments

- Medical data sources: [List sources]
- Design inspiration: Modern healthcare platforms
- Icons: SVG custom illustrations
- Fonts: Google Fonts (Inter)

---

**Built with ❤️ for better healthcare accessibility**

**Version**: 1.0.0 (MVP)  
**Last Updated**: 2024
