/**
 * SkillHub - Main JavaScript
 * Interactive features for the AI Agent Skills Shop
 */

// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', function() {
    initNavigation();
    initSmoothScroll();
    initScrollAnimations();
    initInteractiveElements();
});

/**
 * Navigation functionality
 * Handles sticky nav, mobile menu, and scroll effects
 */
function initNavigation() {
    const nav = document.querySelector('nav');
    let lastScroll = 0;
    let ticking = false;

    // Scroll handler with requestAnimationFrame for performance
    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(function() {
                const currentScroll = window.pageYOffset;

                // Add/remove background blur based on scroll
                if (currentScroll > 50) {
                    nav.classList.add('shadow-lg');
                } else {
                    nav.classList.remove('shadow-lg');
                }

                lastScroll = currentScroll;
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });
}

/**
 * Smooth scroll for anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();

                const navHeight = document.querySelector('nav').offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Scroll-triggered animations
 * Uses Intersection Observer for performance
 */
function initScrollAnimations() {
    // Elements to animate on scroll
    const animatedElements = document.querySelectorAll('.card-hover, .group');

    // Check if IntersectionObserver is supported
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            root: null,
            rootMargin: '0px 0px -50px 0px',
            threshold: 0.1
        });

        animatedElements.forEach(el => observer.observe(el));
    }
}

/**
 * Interactive elements
 * Buttons, hover effects, etc.
 */
function initInteractiveElements() {
    // All buttons with hover sound effect (optional, can be enabled)
    const buttons = document.querySelectorAll('button');

    buttons.forEach(button => {
        // Add click ripple effect
        button.addEventListener('click', function(e) {
            const rect = button.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const ripple = document.createElement('span');
            ripple.style.cssText = `
                position: absolute;
                background: rgba(255, 255, 255, 0.4);
                border-radius: 50%;
                transform: scale(0);
                animation: ripple 0.6s ease-out;
                pointer-events: none;
                left: ${x}px;
                top: ${y}px;
                width: 100px;
                height: 100px;
                margin-left: -50px;
                margin-top: -50px;
            `;

            button.style.position = 'relative';
            button.style.overflow = 'hidden';
            button.appendChild(ripple);

            setTimeout(() => ripple.remove(), 600);
        });
    });

    // Counter animation for stats
    animateCounters();
}

/**
 * Animate counters on scroll
 */
function animateCounters() {
    const stats = [
        { selector: '.stat-skills', target: 128, suffix: '+' },
        { selector: '.stat-creators', target: 50, suffix: '+' },
    ];

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Find the number element within this entry
                const numberEl = entry.target.querySelector('span, .number');
                if (numberEl && !numberEl.classList.contains('animated')) {
                    const finalNumber = parseInt(numberEl.textContent) || 128;
                    animateNumber(numberEl, 0, finalNumber, 1500);
                    numberEl.classList.add('animated');
                }
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    // Observe all stat containers
    document.querySelectorAll('.stat-item, [class*="stat-"]').forEach(stat => {
        observer.observe(stat);
    });
}

/**
 * Animate a number from start to end
 */
function animateNumber(element, start, end, duration) {
    const startTime = performance.now();

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);

        // Easing function (ease-out-cubic)
        const easeOut = 1 - Math.pow(1 - progress, 3);
        const current = Math.floor(start + (end - start) * easeOut);

        element.textContent = current + '+';

        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }

    requestAnimationFrame(update);
}

// Add ripple keyframes
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Console welcome message
console.log('%c🚀 SkillHub', 'font-size: 24px; font-weight: bold; color: #FB923C;');
console.log('%cWelcome to the AI Agent Skills Shop!', 'font-size: 14px; color: #666;');
