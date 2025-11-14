// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Navbar scroll effect
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.07)';
    }
});

// Feature cards animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.feature-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(30px)';
    card.style.transition = 'all 0.6s ease-out';
    observer.observe(card);
});

// Contact form submission
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            subject: document.getElementById('subject').value,
            message: document.getElementById('message').value
        };
        
        // In production, this would send to backend
        console.log('Form submitted:', formData);
        
        // Show success message
        alert('Thank you for contacting us! We\'ll get back to you soon.');
        contactForm.reset();
    });
}

// Animate stats on scroll
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const statNumbers = entry.target.querySelectorAll('.stat-number');
            statNumbers.forEach(stat => {
                const finalValue = stat.textContent;
                animateValue(stat, finalValue);
            });
            statsObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

const teamStats = document.querySelector('.team-stats');
if (teamStats) {
    statsObserver.observe(teamStats);
}

function animateValue(element, finalValue) {
    const text = finalValue;
    const hasPlus = text.includes('+');
    const hasPercent = text.includes('%');
    const numericValue = parseInt(text.replace(/[^0-9]/g, ''));
    
    let current = 0;
    const increment = numericValue / 50;
    const timer = setInterval(() => {
        current += increment;
        if (current >= numericValue) {
            clearInterval(timer);
            current = numericValue;
        }
        
        let displayValue = Math.floor(current);
        
        // Format large numbers
        if (numericValue >= 1000) {
            displayValue = (Math.floor(current / 100) / 10).toFixed(1) + 'K';
        } else if (numericValue >= 1000000) {
            displayValue = (Math.floor(current / 100000) / 10).toFixed(1) + 'M';
        }
        
        element.textContent = displayValue + (hasPlus ? '+' : '') + (hasPercent ? '%' : '');
    }, 30);
}
