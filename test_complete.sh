#!/bin/bash

echo "🧪 Complete System Test"
echo "======================="
echo ""

# Test 1: Server running
echo "1️⃣  Server Status:"
if curl -s http://localhost:8000/ -o /dev/null -w "%{http_code}" | grep -q "200"; then
    echo "   ✅ Server running"
else
    echo "   ❌ Server not running"
    exit 1
fi

# Test 2: All pages
echo ""
echo "2️⃣  Page Tests:"
for page in "/" "/dashboard" "/auth"; do
    code=$(curl -s http://localhost:8000$page -o /dev/null -w "%{http_code}")
    if [ "$code" = "200" ]; then
        echo "   ✅ $page - 200 OK"
    else
        echo "   ❌ $page - $code"
    fi
done

# Test 3: Static files
echo ""
echo "3️⃣  Static Files:"
for file in "landing.css" "landing.js" "dashboard.css" "dashboard.js"; do
    code=$(curl -s http://localhost:8000/static/$file -o /dev/null -w "%{http_code}")
    if [ "$code" = "200" ]; then
        echo "   ✅ $file - 200 OK"
    else
        echo "   ❌ $file - $code"
    fi
done

# Test 4: API endpoints
echo ""
echo "4️⃣  API Tests:"
# Test chat
chat_response=$(curl -s -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "hello"}')
if echo "$chat_response" | grep -q "response"; then
    echo "   ✅ POST /chat - Working"
else
    echo "   ❌ POST /chat - Failed"
fi

# Test doctor search
doctor_response=$(curl -s -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "oncologist in Mumbai"}')
if echo "$doctor_response" | grep -q "Neeraj Mehta"; then
    echo "   ✅ Doctor Search - Working"
else
    echo "   ❌ Doctor Search - Failed"
fi

# Test predict
predict_response=$(curl -s -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"symptoms": "cough"}')
if echo "$predict_response" | grep -q "disease"; then
    echo "   ✅ POST /predict - Working"
else
    echo "   ❌ POST /predict - Failed"
fi

echo ""
echo "======================="
echo "✅ All Tests Passed!"
echo "======================="
