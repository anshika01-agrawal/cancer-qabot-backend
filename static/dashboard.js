// Navigation and Section Management
function showSection(sectionName) {
    // Hide all sections
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => section.classList.remove('active'));
    
    // Show selected section
    const targetSection = document.getElementById(sectionName + '-section');
    if (targetSection) {
        targetSection.classList.add('active');
    }
    
    // Update active menu item
    const menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('href') === '#' + sectionName) {
            item.classList.add('active');
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const menuItems = document.querySelectorAll('.menu-item');
    const sections = document.querySelectorAll('.content-section');
    
    // Section navigation
    menuItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const sectionId = this.getAttribute('data-section');
            
            // Update active menu item
            menuItems.forEach(mi => mi.classList.remove('active'));
            this.classList.add('active');
            
            // Update active section
            sections.forEach(s => s.classList.remove('active'));
            document.getElementById(sectionId).classList.add('active');
        });
    });
    
    // Chat functionality
    setupChat();
    
    // Quick action chips
    setupQuickActions();
    
    // Doctor search
    setupDoctorSearch();
});

// Chat Setup
let chatInputGlobal, chatMessagesGlobal;

function setupChat() {
    chatInputGlobal = document.getElementById('chatInput');
    const sendBtn = document.getElementById('sendBtn');
    chatMessagesGlobal = document.getElementById('chatMessages');
    
    if (sendBtn) {
        sendBtn.addEventListener('click', sendMessage);
    }
    if (chatInputGlobal) {
        chatInputGlobal.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }
}

// Global sendMessage function
function sendMessage() {
    const chatInput = chatInputGlobal || document.getElementById('chatInput');
    const chatMessages = chatMessagesGlobal || document.getElementById('chatMessages');
    
    if (!chatInput) return;
    
    const message = chatInput.value.trim();
    if (!message) return;
    
    // Add user message
    addMessage(message, 'user');
    chatInput.value = '';
    
    // Show typing indicator
    showTypingIndicator();
    
    // Send to backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ symptoms: message })
    })
    .then(response => response.json())
    .then(data => {
        removeTypingIndicator();
        
        // Format response
        let responseText = '';
        if (data.disease) {
            responseText = `Based on your symptoms, you might have **${data.disease}**.\n\n`;
            
            if (data.treatment) {
                responseText += `**Recommended Treatment:**\n${data.treatment}\n\n`;
            }
            
            if (data.severity === 'critical') {
                responseText += `⚠️ **Critical Condition Detected!**\nPlease consult a doctor immediately. Check the "Find Doctors" section for specialists near you.`;
            } else {
                responseText += `💊 You can also check the "Medicines" section for recommended medications.`;
            }
        } else {
            responseText = data.message || "I'm analyzing your symptoms. Could you provide more details?";
        }
        
        addMessage(responseText, 'bot');
    })
    .catch(error => {
        removeTypingIndicator();
        addMessage('Sorry, I encountered an error. Please try again.', 'bot');
        console.error('Error:', error);
    });
}

// Global sendQuick function for quick action chips
function sendQuick(message) {
    const chatInput = chatInputGlobal || document.getElementById('chatInput');
    if (chatInput) {
        chatInput.value = message;
        sendMessage();
    }
}

// Global handleKeyPress function
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function addMessage(text, type) {
    const chatMessages = chatMessagesGlobal || document.getElementById('chatMessages');
    if (!chatMessages) return;
    
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    
    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.innerHTML = type === 'bot' 
        ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/><line x1="8" y1="16" x2="8" y2="16"/><line x1="16" y1="16" x2="16" y2="16"/></svg>'
        : 'U';
    
    const bubble = document.createElement('div');
    bubble.className = 'message-bubble';
    bubble.textContent = text;
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(bubble);
    
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function showTypingIndicator() {
    const chatMessages = chatMessagesGlobal || document.getElementById('chatMessages');
    if (!chatMessages) return;
    
    const indicator = document.createElement('div');
    indicator.className = 'message bot typing-indicator';
    indicator.id = 'typingIndicator';
    indicator.innerHTML = `
        <div class="message-avatar">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="11" width="18" height="10" rx="2"/>
                <circle cx="12" cy="5" r="2"/>
                <path d="M12 7v4"/>
                <line x1="8" y1="16" x2="8" y2="16"/>
                <line x1="16" y1="16" x2="16" y2="16"/>
            </svg>
        </div>
        <div class="message-bubble">Typing...</div>
    `;
    chatMessages.appendChild(indicator);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function removeTypingIndicator() {
    const indicator = document.getElementById('typingIndicator');
    if (indicator) {
        indicator.remove();
    }
}

// Quick Action Chips
function setupQuickActions() {
    const quickChips = document.querySelectorAll('.quick-chips button');
    const chatInput = document.getElementById('chatInput');
    
    quickChips.forEach(chip => {
        chip.addEventListener('click', function() {
            chatInput.value = this.textContent;
            chatInput.focus();
        });
    });
}

// Doctor Search
function setupDoctorSearch() {
    const searchInput = document.getElementById('doctorSearch');
    const doctorCards = document.querySelectorAll('.doctor-card');
    
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase();
            
            doctorCards.forEach(card => {
                const name = card.querySelector('h3').textContent.toLowerCase();
                const specialty = card.querySelector('.specialty').textContent.toLowerCase();
                
                if (name.includes(query) || specialty.includes(query)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }
}

// Get user location for hospitals
function getUserLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            position => {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                updateLocationInfo(lat, lon);
            },
            error => {
                console.error('Location error:', error);
            }
        );
    }
}

function updateLocationInfo(lat, lon) {
    // This would call a geocoding API to get address
    // For now, just update the UI
    const locationInfo = document.querySelector('.location-info p');
    if (locationInfo) {
        locationInfo.textContent = `Lat: ${lat.toFixed(2)}, Lon: ${lon.toFixed(2)}`;
    }
}

// Initialize location on page load
getUserLocation();
