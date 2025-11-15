# 🚀 Hugging Face Setup - Complete Karne Ke Steps

## ✅ Maine Kya Kar Diya (Already Done)

1. **Security files created**:
   - `.env.example` - Template file
   - `.gitignore` - API key ko safe rakhne ke liye
   - `config.py` - Configuration management

2. **AI Chatbot code created**:
   - `ml_model/ai_chatbot.py` - Hugging Face integration
   - Medical-specific prompts
   - Safety disclaimers
   - Fallback system

3. **Updated files**:
   - `requirements.txt` - Added Hugging Face SDK
   - `main.py` - Integrated AI chatbot with /chat endpoint

4. **Test script created**:
   - `test_huggingface.py` - Test AI before using

---

## 📝 Tum Kya Karo (Your Turn - 3 Steps)

### Step 1: Get Hugging Face Token (2 minutes)

**A. Account banao:**
```
https://huggingface.co/join
```
- Email ya Google se signup
- Email verify karo

**B. Token banao:**
1. Login karo: https://huggingface.co/
2. Right top pe **profile icon** → **Settings**
3. Left sidebar me **Access Tokens** click
4. **New token** button click
5. Token name do: `cancer-bot`
6. Type: **Read** select karo
7. **Generate token** click
8. Token **copy** karo (looks like: `hf_AbCdEf123...`)

---

### Step 2: Create .env File (30 seconds)

**In your project folder, create file named `.env`**

```bash
# File: .env
HUGGINGFACE_API_KEY=hf_your_actual_token_here
HUGGINGFACE_MODEL=microsoft/BioGPT-Large
MAX_TOKENS=500
TEMPERATURE=0.7
```

**⚠️ IMPORTANT**: 
- Replace `hf_your_actual_token_here` with your REAL token
- Don't use quotes around the token
- Save the file

**Example:**
```
HUGGINGFACE_API_KEY=hf_AbCdEf123XyZ456
HUGGINGFACE_MODEL=microsoft/BioGPT-Large
```

---

### Step 3: Install Dependencies (1 minute)

```bash
pip install -r requirements.txt
```

This will install:
- `huggingface-hub` - Hugging Face API client
- `python-dotenv` - Environment variable loader

---

## 🧪 Test Karo (Before Using)

### Test 1: Check Token
```bash
python test_huggingface.py
```

**Expected output:**
```
============================================================
🤖 Hugging Face AI Chatbot Test
============================================================

[1] Initializing AI Chatbot...
✓ Configuration loaded successfully
✓ AI Chatbot initialized with model: microsoft/BioGPT-Large
✅ Success! Using model: microsoft/BioGPT-Large

[2] Testing AI Responses...
------------------------------------------------------------

📝 Question 1: What are the early warning signs of lung cancer?
------------------------------------------------------------
🤖 AI Response (huggingface):
[AI will provide detailed medical information...]
```

**If error:**
```
❌ Failed: Check your HUGGINGFACE_API_KEY in .env file
```
→ Double check `.env` file has correct token

---

### Test 2: Start Server
```bash
# Kill old server if running
pkill -f uvicorn

# Start fresh
uvicorn main:app --reload
```

**Expected output:**
```
Loading ML models...
✓ Configuration loaded successfully
✓ Symptom checker loaded
✓ Medical knowledge base loaded
✓ AI Chatbot initialized (Hugging Face)
INFO: Application startup complete.
```

---

### Test 3: Test API Endpoint
```bash
# In new terminal
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What are lung cancer symptoms?"}'
```

**Expected response:**
```json
{
  "response": "Lung cancer symptoms include persistent cough...",
  "source": "ai",
  "model": "microsoft/BioGPT-Large",
  "powered_by": "Hugging Face"
}
```

---

## 🎯 Models Available (Choose in .env)

### 1. microsoft/BioGPT-Large (RECOMMENDED ✅)
```env
HUGGINGFACE_MODEL=microsoft/BioGPT-Large
```
- **Best for**: Medical text generation
- **Quality**: ⭐⭐⭐⭐⭐
- **Speed**: Medium
- **Use case**: General medical Q&A

### 2. google/flan-t5-large (FAST ⚡)
```env
HUGGINGFACE_MODEL=google/flan-t5-large
```
- **Best for**: Quick responses
- **Quality**: ⭐⭐⭐⭐
- **Speed**: Fast
- **Use case**: Simple questions

### 3. dmis-lab/biobert-base-cased-v1.2 (ACCURATE 🎯)
```env
HUGGINGFACE_MODEL=dmis-lab/biobert-base-cased-v1.2
```
- **Best for**: Medical accuracy
- **Quality**: ⭐⭐⭐⭐⭐
- **Speed**: Slow
- **Use case**: Detailed medical info

---

## 💰 Cost & Limits

### Free Tier (No Credit Card)
- **Requests**: ~1000 per month
- **Rate limit**: ~30 requests per minute
- **Cost**: FREE ✅

### If Exceeded
- Upgrade to Pro: **$9/month**
- Unlimited requests
- Faster responses

**Reality**: Free tier bohot hai for development/testing

---

## 🔧 Troubleshooting

### Error 1: "HUGGINGFACE_API_KEY not found"
**Solution:**
```bash
# Check if .env file exists
ls -la .env

# If not, create it:
echo "HUGGINGFACE_API_KEY=hf_your_token" > .env
```

### Error 2: "Invalid token"
**Solution:**
- Token copy karte waqt space to nahi aa gaya?
- Token active hai na Hugging Face pe?
- Try regenerating token

### Error 3: "Rate limit exceeded"
**Solution:**
- Free tier limit ho gayi
- 1 minute wait karo
- Ya Pro subscription lo

### Error 4: Model not loading
**Solution:**
```env
# Try simpler model
HUGGINGFACE_MODEL=google/flan-t5-base
```

---

## 📊 Working Example

**.env file:**
```
HUGGINGFACE_API_KEY=hf_AbCdEf123XyZ789
HUGGINGFACE_MODEL=microsoft/BioGPT-Large
```

**Test:**
```bash
python test_huggingface.py
```

**Result:**
```
✅ Success! Using model: microsoft/BioGPT-Large

📝 Question 1: What are lung cancer symptoms?
🤖 AI Response (huggingface):
Early warning signs of lung cancer include persistent cough 
lasting more than 3 weeks, chest pain, shortness of breath, 
coughing up blood, unexplained weight loss, and fatigue...
⚠️ Disclaimer: This is educational information only...
```

---

## ✅ Success Checklist

- [ ] Hugging Face account banaya
- [ ] Token generate kiya
- [ ] `.env` file create ki with token
- [ ] `pip install -r requirements.txt` run kiya
- [ ] `python test_huggingface.py` successfully run hua
- [ ] Server start kiya (`uvicorn main:app --reload`)
- [ ] `/chat` endpoint test kiya
- [ ] AI responses aa rahe hain ✅

---

## 🎉 Next Steps After Setup

1. **Dashboard me integrate karo** - Frontend se `/chat` endpoint call karo
2. **Test with users** - Real questions try karo
3. **Monitor usage** - Hugging Face dashboard pe quota check karo
4. **Optimize** - Agar slow hai to model change karo

---

## 💬 Muje Batao Status

**Jab complete ho:**
```
"Setup complete! AI responses aa rahe hain ✅"
```

**Agar problem:**
```
"Error aa raha: [paste error message]"
```

**Agar help chahiye:**
```
"Step X pe stuck hu, help karo"
```

Main help karunga! 🚀
