/**
 * COSMOS Platform - Main JavaScript Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. SCROLL REVEAL ANIMATION
    const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
    
    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    revealElements.forEach(el => revealObserver.observe(el));

    // 2. ANIMATED COUNTERS
    const counters = document.querySelectorAll('.counter');
    
    const countUp = (el) => {
        const target = +el.getAttribute('data-target');
        const duration = 2000;
        const start = performance.now();
        
        const update = (timestamp) => {
            const elapsed = timestamp - start;
            const progress = Math.min(elapsed / duration, 1);
            // easeOutExpo easing
            const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
            
            el.innerText = Math.floor(easeProgress * target);
            
            if (progress < 1) {
                requestAnimationFrame(update);
            } else {
                el.innerText = target;
            }
        };
        
        requestAnimationFrame(update);
    };

    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                countUp(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => counterObserver.observe(counter));

    // 3. NAVBAR BEHAVIOR
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('nav-toggle');
    const navLinks = document.getElementById('nav-links');
    const navItems = document.querySelectorAll('.nav-links a');
    const sections = document.querySelectorAll('section');

    // Scrolled class
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Mobile toggle
    navToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });

    // Close mobile menu on link click
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            navLinks.classList.remove('active');
        });
    });

    // Active section highlighting
    const navObserver = new IntersectionObserver((entries) => {
        let currentSectionId = '';
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                currentSectionId = entry.target.id;
            }
        });

        if (currentSectionId) {
            navItems.forEach(item => {
                item.classList.remove('active');
                if (item.getAttribute('href') === `#${currentSectionId}`) {
                    item.classList.add('active');
                }
            });
        }
    }, { threshold: 0.3, rootMargin: "-10% 0px -50% 0px" });

    sections.forEach(section => {
        if (section.id) {
            navObserver.observe(section);
        }
    });

    // Smooth scroll for nav links (handled natively by CSS scroll-behavior, but good to have JS fallback or override if needed. Using CSS for now).

    // 4. ACCORDION (10 Principles)
    const accordionItems = document.querySelectorAll('.accordion-item');
    
    accordionItems.forEach(item => {
        const trigger = item.querySelector('.accordion-trigger');
        const content = item.querySelector('.accordion-content');
        
        trigger.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            
            // Close all others
            accordionItems.forEach(otherItem => {
                otherItem.classList.remove('active');
                otherItem.querySelector('.accordion-content').style.maxHeight = null;
            });
            
            // Open clicked if it wasn't active
            if (!isActive) {
                item.classList.add('active');
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    });

    // 5. LISI DONUT CHART ANIMATION
    const lisiRing = document.getElementById('lisi-chart');
    if (lisiRing) {
        const chartObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        
        chartObserver.observe(lisiRing);
    }

    // 6. CONTACT FORM
    const form = document.getElementById('demo-form');
    const formSuccess = document.getElementById('form-success');
    
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            // Basic validation is handled by HTML5 'required' attributes
            
            // Simulate submission
            form.style.display = 'none';
            formSuccess.classList.add('visible');
        });
    }

    // 7. PARALLAX EFFECT
    const heroGlows = document.querySelectorAll('.hero-glow, .hero-glow-2');
    
    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        // Only run if near top
        if (scrollY < window.innerHeight) {
            requestAnimationFrame(() => {
                heroGlows.forEach((glow, index) => {
                    const factor = index === 0 ? 0.3 : -0.2;
                    glow.style.transform = `translateY(${scrollY * factor}px)`;
                });
            });
        }
    });

    // 8. CONSTELLATION BACKGROUND (Hero)
    const canvas = document.getElementById('hero-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width, height;
        let particles = [];
        
        const initCanvas = () => {
            width = canvas.width = canvas.parentElement.offsetWidth;
            height = canvas.height = canvas.parentElement.offsetHeight;
        };
        
        window.addEventListener('resize', () => {
            initCanvas();
            initParticles();
        });
        
        class Particle {
            constructor() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.vx = (Math.random() - 0.5) * 0.5;
                this.vy = (Math.random() - 0.5) * 0.5;
                this.radius = Math.random() * 1.5 + 0.5;
            }
            
            update() {
                this.x += this.vx;
                this.y += this.vy;
                
                if (this.x < 0 || this.x > width) this.vx *= -1;
                if (this.y < 0 || this.y > height) this.vy *= -1;
            }
            
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(72, 202, 228, 0.4)';
                ctx.fill();
            }
        }
        
        const initParticles = () => {
            particles = [];
            const numParticles = Math.min(Math.floor(width * height / 20000), 80); // scale with screen size
            for (let i = 0; i < numParticles; i++) {
                particles.push(new Particle());
            }
        };
        
        const drawLines = () => {
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const distance = Math.sqrt(dx * dx + dy * dy);
                    
                    if (distance < 120) {
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        const opacity = 1 - (distance / 120);
                        ctx.strokeStyle = `rgba(72, 202, 228, ${opacity * 0.15})`;
                        ctx.lineWidth = 0.5;
                        ctx.stroke();
                    }
                }
            }
        };
        
        const animate = () => {
            ctx.clearRect(0, 0, width, height);
            
            particles.forEach(p => {
                p.update();
                p.draw();
            });
            
            drawLines();
            
            requestAnimationFrame(animate);
        };
        
        initCanvas();
        initParticles();
        animate();
    }
});
