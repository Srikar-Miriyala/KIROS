/* ═══════════════════════════════════════════════════════════════
   KIROS — World-Class Landing Page
   JavaScript: Animations, Interactions, Particle System
   ═══════════════════════════════════════════════════════════════ */

(function () {
    'use strict';

    let animationId = null;

    // ──────────────────────────────────────────────
    // PRELOADER & SESSION MANAGEMENT
    // ──────────────────────────────────────────────
    let isVisited = false;
    try {
        isVisited = !!sessionStorage.getItem('kiros_visited');
    } catch (e) {
        isVisited = false;
    }

    const preloader = document.getElementById('preloader');

    if (isVisited) {
        // Internal page navigation within same session:
        // Immediately suppress preloader without waiting for window.load
        document.documentElement.classList.add('kiros-visited');
        document.documentElement.style.setProperty('--preloader-display', 'none');
        if (preloader) {
            preloader.classList.add('hidden');
            preloader.style.display = 'none';
        }
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initAnimations, { once: true });
        } else {
            initAnimations();
        }
    } else {
        // Initial first visit of session:
        const runFirstVisitPreloader = () => {
            try {
                sessionStorage.setItem('kiros_visited', 'true');
            } catch (e) {}

            setTimeout(() => {
                if (preloader) {
                    preloader.classList.add('hidden');
                }
                setTimeout(() => {
                    if (preloader) {
                        preloader.style.display = 'none';
                    }
                    document.documentElement.classList.add('kiros-visited');
                    initAnimations();
                }, 500); // Wait for fade out
            }, 1200);
        };

        if (document.readyState === 'complete') {
            runFirstVisitPreloader();
        } else {
            window.addEventListener('load', runFirstVisitPreloader, { once: true });
        }
    }

    // Handle browser Back/Forward navigation (bfcache)
    window.addEventListener('pageshow', (event) => {
        let visited = false;
        try {
            visited = !!sessionStorage.getItem('kiros_visited');
        } catch (e) {}
        if (visited) {
            document.documentElement.classList.add('kiros-visited');
            document.documentElement.style.setProperty('--preloader-display', 'none');
            const p = document.getElementById('preloader');
            if (p) {
                p.classList.add('hidden');
                p.style.display = 'none';
            }
        }
    });

    // ──────────────────────────────────────────────
    // SCROLL PROGRESS BAR
    // ──────────────────────────────────────────────
    const scrollProgress = document.getElementById('scrollProgress');
    if (scrollProgress) {
        window.addEventListener('scroll', () => {
            const scrollTop = window.scrollY;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            if (docHeight > 0) {
                const progress = (scrollTop / docHeight) * 100;
                scrollProgress.style.width = progress + '%';
            }
        }, { passive: true });
    }

    // ──────────────────────────────────────────────
    // FLOATING NAVBAR (Dynamic Island / Capsule Pill)
    // ──────────────────────────────────────────────
    const navbar = document.getElementById('navbar');
    if (navbar) {
        const updateNavbarScroll = () => {
            const currentScroll = window.scrollY;
            if (currentScroll > 40) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        };
        updateNavbarScroll();
        window.addEventListener('scroll', updateNavbarScroll, { passive: true });
    }

    // Mobile Menu & Backdrop
    const hamburger = document.getElementById('navHamburger');
    const navMenu = document.getElementById('navMenu');
    const menuBackdrop = document.getElementById('menuBackdrop');
    const navDrawerClose = document.getElementById('navDrawerClose');

    const closeMobileMenu = () => {
        if (hamburger) {
            hamburger.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
        }
        if (navMenu) navMenu.classList.remove('open');
        if (menuBackdrop) menuBackdrop.classList.remove('active');
        document.body.classList.remove('menu-locked');
    };

    const toggleMobileMenu = () => {
        if (!navMenu || !hamburger) return;
        const isOpen = navMenu.classList.toggle('open');
        hamburger.classList.toggle('active', isOpen);
        hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        if (menuBackdrop) menuBackdrop.classList.toggle('active', isOpen);
        if (isOpen) {
            document.body.classList.add('menu-locked');
        } else {
            document.body.classList.remove('menu-locked');
        }
    };

    if (hamburger) {
        hamburger.setAttribute('aria-expanded', 'false');
        hamburger.addEventListener('click', toggleMobileMenu);
    }

    if (navDrawerClose) {
        navDrawerClose.addEventListener('click', closeMobileMenu);
    }

    if (menuBackdrop) {
        menuBackdrop.addEventListener('click', closeMobileMenu);
    }

    // Close menu with Escape key
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && navMenu && navMenu.classList.contains('open')) {
            closeMobileMenu();
        }
    });

    // ──────────────────────────────────────────────
    // MEGA MENU INTERACTION (Desktop)
    // ──────────────────────────────────────────────
    const navLinksData = document.querySelectorAll('.nav-links a[data-menu]');
    const megaMenuPanels = document.querySelectorAll('.mega-menu-panel');
    const megaMenuWrapper = document.getElementById('megaMenuWrapper');

    let menuTimeout;
    let activePanel = null;
    let activeLink = null;

    const openMenu = (menuId, linkEl) => {
        if (window.innerWidth <= 1024) return;
        clearTimeout(menuTimeout);
        
        if (activePanel && activePanel.id !== menuId) {
            activePanel.classList.remove('active');
            if (activeLink) activeLink.classList.remove('active');
        }

        const panel = document.getElementById(menuId);
        if (panel) {
            panel.classList.add('active');
            linkEl.classList.add('active');
            if (menuBackdrop) menuBackdrop.classList.add('active');
            if (megaMenuWrapper) megaMenuWrapper.style.pointerEvents = 'auto';
            if (navbar) navbar.classList.add('menu-open');
            activePanel = panel;
            activeLink = linkEl;
        }
    };

    const closeMenu = () => {
        if (window.innerWidth <= 1024) return;
        menuTimeout = setTimeout(() => {
            if (activePanel) activePanel.classList.remove('active');
            if (activeLink) activeLink.classList.remove('active');
            if (menuBackdrop && (!navMenu || !navMenu.classList.contains('open'))) {
                menuBackdrop.classList.remove('active');
            }
            if (megaMenuWrapper) megaMenuWrapper.style.pointerEvents = 'none';
            if (navbar) navbar.classList.remove('menu-open');
            activePanel = null;
            activeLink = null;
        }, 120); 
    };

    navLinksData.forEach(link => {
        link.addEventListener('mouseenter', () => {
            const menuId = link.getAttribute('data-menu');
            if (menuId) openMenu(menuId, link);
        });
        link.addEventListener('mouseleave', () => {
            closeMenu();
        });
    });

    megaMenuPanels.forEach(panel => {
        panel.addEventListener('mouseenter', () => {
            clearTimeout(menuTimeout);
        });
        panel.addEventListener('mouseleave', () => {
            closeMenu();
        });
    });

    // ──────────────────────────────────────────────
    // MOBILE NAVIGATION DRAWER
    // ──────────────────────────────────────────────
    // On mobile, all items are direct links. Close drawer on navigation.
    document.querySelectorAll('.nav-links a, .nav-actions a').forEach(item => {
        item.addEventListener('click', () => {
            if (window.innerWidth <= 1024) {
                closeMobileMenu();
            }
        });
    });

    // ──────────────────────────────────────────────
    // HERO CANVAS — Particle System (Guarded)
    // ──────────────────────────────────────────────
    const canvas = document.getElementById('heroCanvas');
    if (canvas && canvas.getContext) {
        const ctx = canvas.getContext('2d');
        let width, height;
        let particles = [];

        function resize() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
            initParticles();
        }
        window.addEventListener('resize', resize, { passive: true });

        class Particle {
            constructor() {
                this.reset();
                this.y = Math.random() * (height || 500);
            }

            reset() {
                this.isLeft = Math.random() > 0.5;
                const dWidth = Math.min(180, width * 0.15);

                if (this.isLeft) {
                    this.x = Math.random() * dWidth;
                } else {
                    this.x = width - (Math.random() * dWidth);
                }

                this.y = (height || 500) + 50;
                this.size = Math.random() * 14 + 10;
                this.speedY = (Math.random() * 0.6 + 0.3) * -1;
                this.speedX = (Math.random() - 0.5) * 0.2;
                this.opacity = 0;
                this.maxOpacity = Math.random() * 0.4 + 0.15;
                this.type = Math.random() > 0.3 ? 'text' : 'bubble';
            }

            update() {
                this.x += this.speedX;
                this.y += this.speedY;

                if (this.y > height - 100 && this.opacity < this.maxOpacity) {
                    this.opacity += 0.02;
                } else if (this.y < 100) {
                    this.opacity -= 0.015;
                } else if (this.opacity < this.maxOpacity) {
                    this.opacity += 0.02;
                }

                if (this.y < -20 || this.opacity <= 0) {
                    this.reset();
                }
            }

            draw() {
                ctx.save();
                if (this.type === 'text') {
                    ctx.fillStyle = `rgba(24, 24, 27, ${Math.max(0, this.opacity)})`;
                    ctx.font = `600 ${this.size}px Inter, sans-serif`;
                    ctx.fillText('CO₂', this.x, this.y);
                } else {
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size / 3, 0, Math.PI * 2);
                    ctx.fillStyle = `rgba(16, 185, 129, ${Math.max(0, this.opacity * 0.5)})`;
                    ctx.fill();
                }
                ctx.restore();
            }
        }

        function initParticles() {
            particles = [];
            const particleCount = width < 768 ? 20 : 45;
            for (let i = 0; i < particleCount; i++) {
                particles.push(new Particle());
            }
        }

        function drawDShapes() {
            const dWidth = Math.min(180, width * 0.15);
            const dHeight = height;

            ctx.beginPath();
            ctx.moveTo(0, 0);
            ctx.lineTo(0, dHeight);
            ctx.bezierCurveTo(dWidth * 1.4, dHeight, dWidth * 1.4, 0, 0, 0);

            ctx.moveTo(width, 0);
            ctx.lineTo(width, dHeight);
            ctx.bezierCurveTo(width - dWidth * 1.4, dHeight, width - dWidth * 1.4, 0, width, 0);
            ctx.closePath();
        }

        function animate() {
            ctx.clearRect(0, 0, width, height);

            ctx.save();
            drawDShapes();
            ctx.fillStyle = 'rgba(24, 24, 27, 0.012)';
            ctx.fill();
            ctx.strokeStyle = 'rgba(24, 24, 27, 0.04)';
            ctx.lineWidth = 1;
            ctx.stroke();
            ctx.restore();

            ctx.save();
            drawDShapes();
            ctx.clip();

            particles.forEach(particle => {
                particle.update();
                particle.draw();
            });

            ctx.restore();
            animationId = requestAnimationFrame(animate);
        }

        resize();
        animate();
    }

    // ──────────────────────────────────────────────
    // HERO MOUSE GLOW
    // ──────────────────────────────────────────────
    const heroGlow = document.getElementById('heroGlow');
    const hero = document.querySelector('.hero');

    if (heroGlow && hero) {
        hero.addEventListener('mousemove', (e) => {
            const rect = hero.getBoundingClientRect();
            const x = e.clientX - rect.left - 300;
            const y = e.clientY - rect.top - 300;
            heroGlow.style.transform = `translate(${x}px, ${y}px)`;
        });
    }

    // ──────────────────────────────────────────────
    // MAGNETIC BUTTONS
    // ──────────────────────────────────────────────
    document.querySelectorAll('.btn-magnetic').forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            btn.style.transform = `translate(${x * 0.15}px, ${y * 0.15}px)`;
        });

        btn.addEventListener('mouseleave', () => {
            btn.style.transform = 'translate(0, 0)';
        });
    });

    // ──────────────────────────────────────────────
    // GSAP ANIMATIONS
    // ──────────────────────────────────────────────
    function initAnimations() {
        if (typeof gsap === 'undefined') return;
        if (typeof ScrollTrigger !== 'undefined') {
            gsap.registerPlugin(ScrollTrigger);
        }

        const cinematicEase = "power4.out";
        const cinematicDuration = 1.4;
        const startTrigger = "top 90%";

        // Base reveal
        gsap.utils.toArray('.reveal').forEach((el, i) => {
            gsap.fromTo(el,
                { opacity: 0, y: 50 },
                {
                    opacity: 1,
                    y: 0,
                    duration: cinematicDuration,
                    ease: cinematicEase,
                    scrollTrigger: {
                        trigger: el,
                        start: startTrigger,
                        toggleActions: 'play none none none'
                    },
                    delay: (i % 3) * 0.08
                }
            );
        });

        // Directional reveals (Left)
        gsap.utils.toArray('.reveal-left').forEach(el => {
            gsap.fromTo(el,
                { opacity: 0, x: -40 },
                {
                    opacity: 1,
                    x: 0,
                    duration: cinematicDuration,
                    ease: cinematicEase,
                    scrollTrigger: {
                        trigger: el,
                        start: 'top 85%',
                        toggleActions: 'play none none none'
                    }
                }
            );
        });

        // Directional reveals (Right)
        gsap.utils.toArray('.reveal-right').forEach(el => {
            gsap.fromTo(el,
                { opacity: 0, x: 40 },
                {
                    opacity: 1,
                    x: 0,
                    duration: cinematicDuration,
                    ease: cinematicEase,
                    scrollTrigger: {
                        trigger: el,
                        start: 'top 85%',
                        toggleActions: 'play none none none'
                    }
                }
            );
        });

        // Scale reveals
        gsap.utils.toArray('.reveal-scale').forEach(el => {
            gsap.fromTo(el,
                { opacity: 0, scale: 0.96 },
                {
                    opacity: 1,
                    scale: 1,
                    duration: 1.5,
                    ease: cinematicEase,
                    scrollTrigger: {
                        trigger: el,
                        start: 'top 85%',
                        toggleActions: 'play none none none'
                    }
                }
            );
        });

        // Staggered configs guarded for page availability
        const staggerConfig = {
            opacity: 1,
            y: 0,
            x: 0,
            scale: 1,
            duration: cinematicDuration,
            ease: cinematicEase,
            stagger: 0.12
        };

        if (document.querySelector('.solution-step') && document.querySelector('.solution-steps')) {
            gsap.fromTo('.solution-step',
                { opacity: 0, y: 40 },
                { ...staggerConfig, scrollTrigger: { trigger: '.solution-steps', start: 'top 85%' } }
            );
        }

        if (document.querySelector('.tech-module') && document.querySelector('.tech-diagram')) {
            gsap.fromTo('.tech-module',
                { opacity: 0, y: 40 },
                { ...staggerConfig, scrollTrigger: { trigger: '.tech-diagram', start: 'top 85%' } }
            );
        }

        if (document.querySelector('.application-card') && document.querySelector('.applications-grid')) {
            gsap.fromTo('.application-card',
                { opacity: 0, y: 40, scale: 0.98 },
                { ...staggerConfig, scrollTrigger: { trigger: '.applications-grid', start: 'top 85%' } }
            );
        }

        if (document.querySelector('.impact-metric') && document.querySelector('.impact-grid')) {
            gsap.fromTo('.impact-metric',
                { opacity: 0, y: 30 },
                { ...staggerConfig, scrollTrigger: { trigger: '.impact-grid', start: 'top 85%' } }
            );
        }

        if (document.querySelector('.timeline-node') && document.querySelector('.timeline')) {
            gsap.fromTo('.timeline-node',
                { opacity: 0, x: -24 },
                { ...staggerConfig, scrollTrigger: { trigger: '.timeline', start: 'top 85%' } }
            );
        }

        if (document.querySelector('.roadmap-stage') && document.querySelector('.roadmap-track')) {
            gsap.fromTo('.roadmap-stage',
                { opacity: 0, y: 24 },
                { ...staggerConfig, scrollTrigger: { trigger: '.roadmap-track', start: 'top 90%' } }
            );
        }

        if (document.querySelector('.prototype-progress')) {
            ScrollTrigger.create({
                trigger: '.prototype-progress',
                start: 'top 85%',
                onEnter: () => {
                    const fill = document.querySelector('.prototype-progress-fill');
                    if (fill && fill.dataset.progress) {
                        fill.style.width = fill.dataset.progress + '%';
                    }
                }
            });
        }

        if (document.querySelector('.comparison-table')) {
            ScrollTrigger.create({
                trigger: '.comparison-table',
                start: 'top 80%',
                onEnter: () => {
                    document.querySelectorAll('.comparison-bar-fill').forEach(bar => {
                        if (bar.dataset.width) {
                            bar.style.width = bar.dataset.width + '%';
                        }
                    });
                }
            });
        }

        // Animated Counters
        if (document.querySelector('.climate-problem')) {
            initCounters('.climate-stat-number', '.climate-problem');
        }
        if (document.querySelector('.impact')) {
            initCounters('.impact-metric-number', '.impact');
        }
    }

    // ──────────────────────────────────────────────
    // ANIMATED COUNTERS
    // ──────────────────────────────────────────────
    function initCounters(selector, triggerSelector) {
        if (typeof gsap === 'undefined') return;
        const counters = document.querySelectorAll(selector);
        if (!counters.length) return;

        ScrollTrigger.create({
            trigger: triggerSelector,
            start: 'top 70%',
            onEnter: () => {
                counters.forEach(counter => {
                    if (counter.dataset.animated) return;
                    counter.dataset.animated = 'true';

                    const target = parseInt(counter.dataset.count, 10);
                    const prefix = counter.dataset.prefix || '';
                    const suffix = counter.dataset.suffix || '';
                    const duration = target > 1000 ? 2.2 : 1.8;

                    gsap.to({ val: 0 }, {
                        val: target,
                        duration: duration,
                        ease: 'power2.out',
                        onUpdate: function () {
                            const current = Math.floor(this.targets()[0].val);
                            counter.textContent = prefix + current.toLocaleString() + suffix;
                        },
                        onComplete: function () {
                            counter.textContent = prefix + target.toLocaleString() + suffix;
                        }
                    });
                });
            }
        });
    }

    // ──────────────────────────────────────────────
    // TECHNOLOGY MODULE EXPAND
    // ──────────────────────────────────────────────
    document.querySelectorAll('.tech-module').forEach(module => {
        module.addEventListener('click', () => {
            const isActive = module.classList.contains('active');
            document.querySelectorAll('.tech-module').forEach(m => {
                m.classList.remove('active');
            });
            if (!isActive) {
                module.classList.add('active');
            }
        });
    });

    // ──────────────────────────────────────────────
    // TIMELINE NODE EXPAND
    // ──────────────────────────────────────────────
    document.querySelectorAll('.timeline-node[data-expand]').forEach(node => {
        node.addEventListener('click', () => {
            const isActive = node.classList.contains('active');
            document.querySelectorAll('.timeline-node').forEach(n => {
                n.classList.remove('active');
            });
            if (!isActive) {
                node.classList.add('active');
            }
        });
    });

    // ──────────────────────────────────────────────
    // SMOOTH SCROLL for in-page anchor links
    // ──────────────────────────────────────────────
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (!href || href === '#' || href.length <= 1) return;
            try {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    const offset = 90; // Account for fixed navbar
                    const targetPos = target.getBoundingClientRect().top + window.scrollY - offset;
                    window.scrollTo({
                        top: targetPos,
                        behavior: 'smooth'
                    });
                }
            } catch (err) {
                // Ignore querySelector syntax errors if invalid selector
            }
        });
    });

    // ──────────────────────────────────────────────
    // REDUCE MOTION — respect user preference
    // ──────────────────────────────────────────────
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        if (animationId) {
            cancelAnimationFrame(animationId);
        }
        document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale').forEach(el => {
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
    }

})();
