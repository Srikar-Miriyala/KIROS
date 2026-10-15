import os

base_dir = r"d:\KIROS-web_v1\assets\home"
os.makedirs(base_dir, exist_ok=True)

# 1. Home Hero
home_hero = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <linearGradient id="hero-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fdfbf7" />
            <stop offset="50%" stop-color="#f0f4f8" />
            <stop offset="100%" stop-color="#e6efe8" />
        </linearGradient>
        <linearGradient id="solar-glow" x1="50%" y1="0%" x2="50%" y2="100%">
            <stop offset="0%" stop-color="#ffffff" stop-opacity="0.8"/>
            <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
        </linearGradient>
        <filter id="blur" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="60" />
        </filter>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="20" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>
    
    <!-- Background -->
    <rect width="100%" height="100%" fill="url(#hero-grad)" />
    
    <!-- Atmospheric Orbs -->
    <circle cx="1400" cy="200" r="400" fill="#fefcfa" filter="url(#blur)" opacity="0.9" />
    <circle cx="400" cy="800" r="500" fill="#e2f0e6" filter="url(#blur)" opacity="0.6" />
    <circle cx="1600" cy="900" r="600" fill="#e8f4fc" filter="url(#blur)" opacity="0.5" />
    
    <!-- Technical Grid -->
    <g stroke="rgba(255,255,255,0.6)" stroke-width="1" opacity="0.3">
        <!-- Horizontal -->
        <line x1="0" y1="200" x2="1920" y2="200" />
        <line x1="0" y1="400" x2="1920" y2="400" />
        <line x1="0" y1="600" x2="1920" y2="600" />
        <line x1="0" y1="800" x2="1920" y2="800" />
        <!-- Vertical -->
        <line x1="400" y1="0" x2="400" y2="1080" />
        <line x1="800" y1="0" x2="800" y2="1080" />
        <line x1="1200" y1="0" x2="1200" y2="1080" />
        <line x1="1600" y1="0" x2="1600" y2="1080" />
    </g>
    
    <!-- Organic Biological Forms -->
    <path d="M -200 600 C 400 300, 800 900, 1400 400 S 2100 700, 2100 700" fill="none" stroke="url(#solar-glow)" stroke-width="120" filter="url(#blur)" opacity="0.7" />
    <path d="M 0 800 C 500 700, 900 1100, 1600 600 S 2000 900, 2000 900" fill="none" stroke="#dcf0e2" stroke-width="60" filter="url(#blur)" opacity="0.8" />
    <path d="M 200 1000 C 700 800, 1000 1200, 1800 700" fill="none" stroke="#ffffff" stroke-width="2" filter="url(#glow)" opacity="0.5" />
    <path d="M 400 1100 C 800 900, 1200 1100, 1900 800" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.3" />
    
    <!-- Geometric Accents -->
    <circle cx="1400" cy="400" r="10" fill="#38A169" filter="url(#glow)" opacity="0.8" />
    <circle cx="1400" cy="400" r="40" fill="none" stroke="#38A169" stroke-width="1" opacity="0.4" />
    
    <circle cx="1600" cy="600" r="6" fill="#3182CE" filter="url(#glow)" opacity="0.6" />
    <circle cx="1600" cy="600" r="24" fill="none" stroke="#3182CE" stroke-width="1" opacity="0.3" />
</svg>"""

# 2. Home System
home_system = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <radialGradient id="bg-grad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#ffffff" />
            <stop offset="100%" stop-color="#f4f7f6" />
        </radialGradient>
        <filter id="soft-glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="30" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>
    <rect width="100%" height="100%" fill="url(#bg-grad)" />
    
    <!-- Central Node -->
    <circle cx="960" cy="540" r="200" fill="#fdfcfb" stroke="#e2e8f0" stroke-width="2" filter="url(#soft-glow)" />
    <circle cx="960" cy="540" r="180" fill="none" stroke="#edf2f7" stroke-width="1" />
    <circle cx="960" cy="540" r="160" fill="#f0fdf4" opacity="0.5" filter="url(#soft-glow)" />
    
    <!-- Orbital Rings -->
    <circle cx="960" cy="540" r="350" fill="none" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="4 8" />
    <circle cx="960" cy="540" r="500" fill="none" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="2 12" />
    
    <!-- Connection Lines -->
    <path d="M 610 540 L 400 540" stroke="#cbd5e0" stroke-width="2" />
    <path d="M 1310 540 L 1520 540" stroke="#cbd5e0" stroke-width="2" />
    <path d="M 960 190 L 960 340" stroke="#cbd5e0" stroke-width="2" />
    
    <!-- Outer Nodes -->
    <circle cx="400" cy="540" r="60" fill="#fff" stroke="#e2e8f0" stroke-width="2" filter="url(#soft-glow)" />
    <circle cx="1520" cy="540" r="60" fill="#fff" stroke="#e2e8f0" stroke-width="2" filter="url(#soft-glow)" />
    <circle cx="960" cy="190" r="60" fill="#fff" stroke="#e2e8f0" stroke-width="2" filter="url(#soft-glow)" />
    
    <!-- Biological Elements inside center -->
    <path d="M 880 540 Q 960 460, 1040 540 T 960 620 T 880 540" fill="none" stroke="#38A169" stroke-width="4" filter="url(#soft-glow)" opacity="0.6"/>
</svg>"""

# 3. Home Biology
home_biology = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080" width="1080" height="1080">
    <defs>
        <linearGradient id="bio-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fdfdfd" />
            <stop offset="100%" stop-color="#e6f2eb" />
        </linearGradient>
        <filter id="cell-glow">
            <feGaussianBlur stdDeviation="40" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>
    <rect width="100%" height="100%" fill="url(#bio-grad)" />
    
    <!-- Abstract Cellular structures -->
    <g opacity="0.6" filter="url(#cell-glow)">
        <circle cx="300" cy="300" r="250" fill="#d1e8da" />
        <circle cx="800" cy="400" r="300" fill="#dbeadd" />
        <circle cx="500" cy="800" r="350" fill="#e2f0e6" />
        <circle cx="900" cy="900" r="200" fill="#e6f2eb" />
    </g>
    
    <!-- Engineering Overlay -->
    <g stroke="rgba(255,255,255,0.8)" stroke-width="1.5" fill="none" opacity="0.5">
        <polygon points="300,100 500,200 400,400 200,300" />
        <polygon points="800,200 1000,400 900,600 700,400" />
        <polygon points="400,600 700,700 600,1000 300,900" />
    </g>
    
    <g fill="#ffffff" opacity="0.9">
        <circle cx="300" cy="100" r="4" />
        <circle cx="500" cy="200" r="4" />
        <circle cx="400" cy="400" r="4" />
        <circle cx="200" cy="300" r="4" />
        
        <circle cx="800" cy="200" r="4" />
        <circle cx="1000" cy="400" r="4" />
        <circle cx="900" cy="600" r="4" />
        <circle cx="700" cy="400" r="4" />
    </g>
</svg>"""

# 4. Home Module
home_module = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#ffffff" />
            <stop offset="100%" stop-color="#f0f4f8" />
        </linearGradient>
        <linearGradient id="glass" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="rgba(255,255,255,0.8)" />
            <stop offset="15%" stop-color="rgba(255,255,255,0.1)" />
            <stop offset="85%" stop-color="rgba(255,255,255,0.1)" />
            <stop offset="100%" stop-color="rgba(255,255,255,0.5)" />
        </linearGradient>
        <linearGradient id="algae" x1="0%" y1="100%" x2="0%" y2="0%">
            <stop offset="0%" stop-color="#276749" />
            <stop offset="70%" stop-color="#48bb78" />
            <stop offset="100%" stop-color="rgba(72,187,120,0)" />
        </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#bg)" />
    
    <!-- Shadows -->
    <ellipse cx="960" cy="980" rx="200" ry="20" fill="rgba(0,0,0,0.05)" />
    <ellipse cx="960" cy="980" rx="100" ry="10" fill="rgba(0,0,0,0.1)" />
    
    <!-- Algae Liquid -->
    <rect x="840" y="250" width="240" height="700" rx="120" fill="url(#algae)" opacity="0.8" />
    
    <!-- Bubbles -->
    <g fill="rgba(255,255,255,0.6)">
        <circle cx="880" cy="800" r="4" />
        <circle cx="920" cy="750" r="6" />
        <circle cx="960" cy="650" r="5" />
        <circle cx="1020" cy="850" r="3" />
        <circle cx="900" cy="500" r="7" />
        <circle cx="980" cy="550" r="4" />
        <circle cx="940" cy="400" r="5" />
    </g>
    
    <!-- Glass Cylinder -->
    <rect x="820" y="200" width="280" height="750" rx="140" fill="url(#glass)" stroke="rgba(255,255,255,0.9)" stroke-width="4" />
    
    <!-- Metal Fittings Top -->
    <rect x="800" y="150" width="320" height="60" rx="30" fill="#e2e8f0" stroke="#cbd5e0" stroke-width="2" />
    <rect x="860" y="100" width="200" height="50" rx="10" fill="#edf2f7" />
    
    <!-- Metal Fittings Bottom -->
    <rect x="800" y="930" width="320" height="60" rx="30" fill="#e2e8f0" stroke="#cbd5e0" stroke-width="2" />
    
    <!-- Sensor Lines -->
    <path d="M 1100 400 L 1300 350 L 1400 350" fill="none" stroke="#a0aec0" stroke-width="2" />
    <circle cx="1400" cy="350" r="4" fill="#a0aec0" />
    
    <path d="M 1100 700 L 1300 750 L 1400 750" fill="none" stroke="#a0aec0" stroke-width="2" />
    <circle cx="1400" cy="750" r="4" fill="#a0aec0" />
</svg>"""

# 5. Home Process
home_process = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#ffffff" />
            <stop offset="100%" stop-color="#f8fafc" />
        </linearGradient>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="15" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>
    <rect width="100%" height="100%" fill="url(#bg)" />
    
    <!-- Flow paths -->
    <path d="M 300 540 C 600 540, 600 340, 960 340" fill="none" stroke="#cbd5e0" stroke-width="4" stroke-dasharray="10 10" />
    <path d="M 300 540 C 600 540, 600 740, 960 740" fill="none" stroke="#cbd5e0" stroke-width="4" stroke-dasharray="10 10" />
    <path d="M 960 340 C 1300 340, 1300 540, 1620 540" fill="none" stroke="#cbd5e0" stroke-width="4" stroke-dasharray="10 10" />
    <path d="M 960 740 C 1300 740, 1300 540, 1620 540" fill="none" stroke="#cbd5e0" stroke-width="4" stroke-dasharray="10 10" />
    
    <!-- Flow Particles -->
    <circle cx="600" cy="425" r="6" fill="#38A169" filter="url(#glow)" />
    <circle cx="600" cy="655" r="6" fill="#3182CE" filter="url(#glow)" />
    <circle cx="1300" cy="425" r="6" fill="#38A169" filter="url(#glow)" />
    
    <!-- Nodes -->
    <rect x="200" y="440" width="200" height="200" rx="40" fill="#fff" stroke="#e2e8f0" stroke-width="2" filter="url(#glow)" />
    <rect x="860" y="240" width="200" height="200" rx="40" fill="#fff" stroke="#e2e8f0" stroke-width="2" filter="url(#glow)" />
    <rect x="860" y="640" width="200" height="200" rx="40" fill="#fff" stroke="#e2e8f0" stroke-width="2" filter="url(#glow)" />
    <rect x="1520" y="440" width="200" height="200" rx="40" fill="#fff" stroke="#e2e8f0" stroke-width="2" filter="url(#glow)" />
</svg>"""

# 6. Home Research
home_research = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fdfbf7" />
            <stop offset="100%" stop-color="#edf2f7" />
        </linearGradient>
        <filter id="blur">
            <feGaussianBlur stdDeviation="20" />
        </filter>
    </defs>
    <rect width="100%" height="100%" fill="url(#bg)" />
    
    <!-- Data Waves -->
    <path d="M -100 400 Q 400 200, 960 540 T 2000 600" fill="none" stroke="#a0aec0" stroke-width="2" opacity="0.3" />
    <path d="M -100 500 Q 400 300, 960 640 T 2000 700" fill="none" stroke="#a0aec0" stroke-width="1" opacity="0.2" />
    <path d="M -100 600 Q 400 400, 960 740 T 2000 800" fill="none" stroke="#a0aec0" stroke-width="1" opacity="0.2" />
    <path d="M -100 700 Q 400 500, 960 840 T 2000 900" fill="none" stroke="#a0aec0" stroke-width="2" opacity="0.3" />
    
    <!-- Floating Data Points -->
    <circle cx="400" cy="340" r="8" fill="#4299e1" opacity="0.6" />
    <circle cx="800" cy="460" r="6" fill="#48bb78" opacity="0.6" />
    <circle cx="1200" cy="580" r="12" fill="#4299e1" opacity="0.4" />
    <circle cx="1600" cy="660" r="8" fill="#48bb78" opacity="0.6" />
    
    <!-- Soft abstract cell in background -->
    <circle cx="1400" cy="300" r="400" fill="#ffffff" filter="url(#blur)" opacity="0.8" />
    <circle cx="500" cy="800" r="300" fill="#ffffff" filter="url(#blur)" opacity="0.6" />
    
    <!-- UI Grid Overlay -->
    <rect x="200" y="200" width="1520" height="680" rx="20" fill="none" stroke="#ffffff" stroke-width="2" opacity="0.5" />
    <line x1="200" y1="260" x2="1720" y2="260" stroke="#ffffff" stroke-width="2" opacity="0.5" />
</svg>"""

# 7. Home Applications
home_applications = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#ffffff" />
            <stop offset="100%" stop-color="#e2e8f0" />
        </linearGradient>
        <filter id="fog">
            <feGaussianBlur stdDeviation="60" />
        </filter>
    </defs>
    <rect width="100%" height="100%" fill="url(#bg)" />
    
    <!-- Atmospheric fog layers -->
    <path d="M 0 600 L 1920 400 L 1920 1080 L 0 1080 Z" fill="#ffffff" filter="url(#fog)" opacity="0.7" />
    
    <!-- Geometric Architecture (Industrial blocks) -->
    <rect x="200" y="500" width="300" height="600" fill="#cbd5e0" opacity="0.4" />
    <rect x="600" y="300" width="400" height="800" fill="#cbd5e0" opacity="0.3" />
    <rect x="1100" y="450" width="250" height="700" fill="#cbd5e0" opacity="0.4" />
    <rect x="1500" y="200" width="300" height="900" fill="#cbd5e0" opacity="0.2" />
    
    <!-- Highlight Layer (Carbon Capture Integration) -->
    <rect x="650" y="700" width="300" height="400" fill="#ffffff" opacity="0.8" />
    <circle cx="800" cy="700" r="100" fill="#f0fdf4" opacity="0.9" filter="url(#fog)" />
    
    <!-- Sun/Light -->
    <circle cx="400" cy="200" r="150" fill="#ffffff" filter="url(#fog)" opacity="0.9" />
</svg>"""

# 8. Home Vision
home_vision = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#ffffff" />
            <stop offset="100%" stop-color="#f0f4f8" />
        </linearGradient>
        <filter id="glow">
            <feGaussianBlur stdDeviation="20" />
        </filter>
    </defs>
    <rect width="100%" height="100%" fill="url(#bg)" />
    
    <!-- Isometric Grid -->
    <g stroke="#cbd5e0" stroke-width="1" opacity="0.3" transform="translate(960, 200) scale(1, 0.5) rotate(45)">
        <line x1="-1000" y1="0" x2="1000" y2="0" />
        <line x1="-1000" y1="200" x2="1000" y2="200" />
        <line x1="-1000" y1="400" x2="1000" y2="400" />
        <line x1="-1000" y1="-200" x2="1000" y2="-200" />
        <line x1="-1000" y1="-400" x2="1000" y2="-400" />
        
        <line x1="0" y1="-1000" x2="0" y2="1000" />
        <line x1="200" y1="-1000" x2="200" y2="1000" />
        <line x1="400" y1="-1000" x2="400" y2="1000" />
        <line x1="-200" y1="-1000" x2="-200" y2="1000" />
        <line x1="-400" y1="-1000" x2="-400" y2="1000" />
    </g>
    
    <!-- Infrastructure Nodes -->
    <g transform="translate(960, 540)">
        <!-- Center Cluster -->
        <circle cx="0" cy="0" r="40" fill="#ffffff" stroke="#a0aec0" stroke-width="2" />
        <circle cx="0" cy="0" r="80" fill="#38A169" opacity="0.2" filter="url(#glow)" />
        
        <circle cx="-200" cy="-100" r="30" fill="#ffffff" stroke="#a0aec0" stroke-width="2" />
        <circle cx="200" cy="100" r="30" fill="#ffffff" stroke="#a0aec0" stroke-width="2" />
        <circle cx="200" cy="-100" r="30" fill="#ffffff" stroke="#a0aec0" stroke-width="2" />
        <circle cx="-200" cy="100" r="30" fill="#ffffff" stroke="#a0aec0" stroke-width="2" />
        
        <!-- Connections -->
        <line x1="0" y1="0" x2="-200" y2="-100" stroke="#cbd5e0" stroke-width="2" />
        <line x1="0" y1="0" x2="200" y2="100" stroke="#cbd5e0" stroke-width="2" />
        <line x1="0" y1="0" x2="200" y2="-100" stroke="#cbd5e0" stroke-width="2" />
        <line x1="0" y1="0" x2="-200" y2="100" stroke="#cbd5e0" stroke-width="2" />
    </g>
    
    <!-- Giant atmospheric gradients behind -->
    <circle cx="400" cy="200" r="400" fill="#fdfbf7" filter="url(#glow)" opacity="0.8" />
    <circle cx="1500" cy="800" r="500" fill="#f0f4f8" filter="url(#glow)" opacity="0.6" />
</svg>"""

files = {
    "home_hero.svg": home_hero,
    "home_system.svg": home_system,
    "home_biology.svg": home_biology,
    "home_module.svg": home_module,
    "home_process.svg": home_process,
    "home_research.svg": home_research,
    "home_applications.svg": home_applications,
    "home_vision.svg": home_vision
}

for name, content in files.items():
    with open(os.path.join(base_dir, name), "w", encoding="utf-8") as f:
        f.write(content)

print("Generated SVGs successfully.")
