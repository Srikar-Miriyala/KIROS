import os

base_dir = r"d:\KIROS-web_v1\assets\home"
os.makedirs(base_dir, exist_ok=True)

# 1. Home Hero (Rich, Deep, Atmospheric)
home_hero = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <radialGradient id="bg-grad" cx="70%" cy="30%" r="80%">
            <stop offset="0%" stop-color="#0F2027" />
            <stop offset="50%" stop-color="#203A43" />
            <stop offset="100%" stop-color="#2C5364" />
        </radialGradient>
        <radialGradient id="sun-flare" cx="80%" cy="20%" r="50%">
            <stop offset="0%" stop-color="#f6e05e" stop-opacity="0.6"/>
            <stop offset="30%" stop-color="#ecc94b" stop-opacity="0.3"/>
            <stop offset="100%" stop-color="#2C5364" stop-opacity="0"/>
        </radialGradient>
        <linearGradient id="bio-flow" x1="0%" y1="100%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#22543d" stop-opacity="0.9"/>
            <stop offset="50%" stop-color="#38a169" stop-opacity="0.6"/>
            <stop offset="100%" stop-color="#9ae6b4" stop-opacity="0.1"/>
        </linearGradient>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="40" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="light-glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="15" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>
    
    <!-- Base Background -->
    <rect width="100%" height="100%" fill="url(#bg-grad)" />
    
    <!-- Solar Flare -->
    <rect width="100%" height="100%" fill="url(#sun-flare)" filter="url(#glow)" />
    
    <!-- Engineering Geometry (Translucent) -->
    <g stroke="rgba(255,255,255,0.15)" stroke-width="2" fill="none">
        <polygon points="1200,100 1600,300 1400,600 1000,400" />
        <polygon points="1600,300 2000,500 1800,800 1400,600" />
        <polygon points="1000,400 1400,600 1200,900 800,700" />
        <!-- Grid lines -->
        <line x1="800" y1="700" x2="2000" y2="700" opacity="0.5"/>
        <line x1="1200" y1="100" x2="1200" y2="900" opacity="0.5"/>
    </g>
    
    <!-- Biological Fluid Forms -->
    <path d="M-200 1080 C 400 900, 600 600, 1000 700 S 1400 200, 2000 0" fill="none" stroke="url(#bio-flow)" stroke-width="180" filter="url(#glow)" />
    <path d="M-100 1100 C 500 850, 700 550, 1100 650 S 1500 150, 2100 -50" fill="none" stroke="#48bb78" stroke-width="40" filter="url(#light-glow)" opacity="0.7"/>
    <path d="M0 1120 C 600 800, 800 500, 1200 600 S 1600 100, 2200 -100" fill="none" stroke="#9ae6b4" stroke-width="10" filter="url(#light-glow)" opacity="0.9"/>
    
    <!-- CO2 Particles -->
    <g fill="#ffffff" filter="url(#light-glow)" opacity="0.6">
        <circle cx="900" cy="800" r="8" />
        <circle cx="1100" cy="500" r="12" />
        <circle cx="1300" cy="300" r="6" />
        <circle cx="1500" cy="150" r="10" />
        <circle cx="700" cy="900" r="15" />
    </g>
</svg>"""

# 2. Home System (Platform)
home_system = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#1A202C" />
            <stop offset="100%" stop-color="#2D3748" />
        </linearGradient>
        <radialGradient id="node-glow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#38A169" stop-opacity="1"/>
            <stop offset="100%" stop-color="#38A169" stop-opacity="0"/>
        </radialGradient>
        <filter id="heavy-blur">
            <feGaussianBlur stdDeviation="50" />
        </filter>
        <filter id="soft-glow">
            <feGaussianBlur stdDeviation="15" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>
    
    <rect width="100%" height="100%" fill="url(#bg)" />
    <circle cx="960" cy="540" r="400" fill="url(#node-glow)" filter="url(#heavy-blur)" opacity="0.4" />
    
    <!-- Data rings -->
    <circle cx="960" cy="540" r="300" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
    <circle cx="960" cy="540" r="450" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="4" stroke-dasharray="10 20" />
    <circle cx="960" cy="540" r="600" fill="none" stroke="rgba(56,161,105,0.2)" stroke-width="1" stroke-dasharray="5 5" />
    
    <!-- Connections -->
    <path d="M 460 540 L 1460 540" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
    <path d="M 960 140 L 960 940" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
    <path d="M 606 186 L 1313 893" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
    <path d="M 1313 186 L 606 893" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="2" />
    
    <!-- Central Node -->
    <circle cx="960" cy="540" r="100" fill="#2F855A" filter="url(#soft-glow)" />
    <circle cx="960" cy="540" r="60" fill="#48BB78" />
    
    <!-- Surrounding Nodes -->
    <g filter="url(#soft-glow)">
        <circle cx="460" cy="540" r="40" fill="#ECC94B" /> <!-- Solar -->
        <circle cx="960" cy="140" r="40" fill="#E2E8F0" /> <!-- CO2 -->
        <circle cx="1460" cy="540" r="40" fill="#3182CE" /> <!-- Water -->
        <circle cx="960" cy="940" r="40" fill="#805AD5" /> <!-- Monitoring -->
    </g>
    
    <!-- Floating particles -->
    <g fill="#ffffff" opacity="0.6">
        <circle cx="700" cy="540" r="4" />
        <circle cx="1200" cy="540" r="4" />
        <circle cx="960" cy="340" r="4" />
        <circle cx="960" cy="740" r="4" />
    </g>
</svg>"""

# 3. Home Module (Bioreactor)
home_module = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#E2E8F0" />
            <stop offset="100%" stop-color="#CBD5E0" />
        </linearGradient>
        <linearGradient id="glass" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="rgba(255,255,255,0.9)" />
            <stop offset="20%" stop-color="rgba(255,255,255,0.2)" />
            <stop offset="80%" stop-color="rgba(255,255,255,0.2)" />
            <stop offset="100%" stop-color="rgba(255,255,255,0.7)" />
        </linearGradient>
        <linearGradient id="algae-core" x1="0%" y1="100%" x2="0%" y2="0%">
            <stop offset="0%" stop-color="#1C4532" />
            <stop offset="60%" stop-color="#2F855A" />
            <stop offset="100%" stop-color="#68D391" />
        </linearGradient>
        <filter id="shadow">
            <feDropShadow dx="0" dy="40" stdDeviation="30" flood-opacity="0.2" />
        </filter>
        <filter id="glass-blur">
            <feGaussianBlur stdDeviation="4" />
        </filter>
    </defs>
    
    <rect width="100%" height="100%" fill="url(#bg)" />
    
    <!-- Floor reflection / shadow -->
    <ellipse cx="960" cy="980" rx="300" ry="30" fill="rgba(0,0,0,0.15)" filter="url(#shadow)" />
    <ellipse cx="960" cy="980" rx="150" ry="15" fill="rgba(0,0,0,0.3)" />
    
    <!-- Reactor Core Algae -->
    <rect x="760" y="250" width="400" height="700" rx="200" fill="url(#algae-core)" />
    
    <!-- Bubble Columns -->
    <g fill="rgba(255,255,255,0.4)" filter="url(#glass-blur)">
        <path d="M 820 900 C 840 700, 800 500, 860 300" stroke="rgba(255,255,255,0.2)" stroke-width="40" fill="none" />
        <path d="M 1100 900 C 1080 700, 1120 500, 1060 300" stroke="rgba(255,255,255,0.1)" stroke-width="60" fill="none" />
    </g>
    
    <!-- Bubbles -->
    <g fill="#ffffff" opacity="0.8">
        <circle cx="850" cy="800" r="8" />
        <circle cx="890" cy="700" r="12" />
        <circle cx="950" cy="600" r="15" />
        <circle cx="1020" cy="850" r="10" />
        <circle cx="1080" cy="500" r="14" />
        <circle cx="980" cy="350" r="12" />
    </g>
    
    <!-- Outer Glass Tube -->
    <rect x="740" y="200" width="440" height="750" rx="220" fill="url(#glass)" stroke="#ffffff" stroke-width="4" filter="url(#shadow)" />
    
    <!-- Engineered Metal Base -->
    <rect x="700" y="880" width="520" height="100" rx="50" fill="#4A5568" />
    <rect x="720" y="880" width="480" height="20" fill="#2D3748" />
    <rect x="800" y="980" width="320" height="40" rx="20" fill="#2D3748" />
    
    <!-- Engineered Metal Top -->
    <rect x="700" y="150" width="520" height="100" rx="50" fill="#4A5568" />
    <rect x="720" y="230" width="480" height="20" fill="#2D3748" />
    
    <!-- Sensor Hardware -->
    <rect x="1160" y="450" width="80" height="140" rx="10" fill="#2D3748" />
    <circle cx="1200" cy="490" r="20" fill="#F6E05E" />
    <path d="M 1180 500 L 1150 500" stroke="#1A202C" stroke-width="4" />
    
    <rect x="680" y="600" width="60" height="100" rx="10" fill="#2D3748" />
    <circle cx="710" cy="650" r="15" fill="#E53E3E" />
</svg>"""

# 4. Home Research
home_research = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#090A0F" />
            <stop offset="100%" stop-color="#141E30" />
        </linearGradient>
        <radialGradient id="cell-glow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#38A169" stop-opacity="0.8"/>
            <stop offset="50%" stop-color="#3182CE" stop-opacity="0.3"/>
            <stop offset="100%" stop-color="#141E30" stop-opacity="0"/>
        </radialGradient>
        <filter id="dof-blur">
            <feGaussianBlur stdDeviation="12" />
        </filter>
        <filter id="dof-blur-heavy">
            <feGaussianBlur stdDeviation="24" />
        </filter>
    </defs>
    
    <rect width="100%" height="100%" fill="url(#bg)" />
    
    <!-- Heavy blurred background elements -->
    <circle cx="400" cy="300" r="300" fill="url(#cell-glow)" filter="url(#dof-blur-heavy)" opacity="0.6" />
    <circle cx="1500" cy="800" r="400" fill="url(#cell-glow)" filter="url(#dof-blur-heavy)" opacity="0.4" />
    
    <!-- Microscopic cellular structures (in focus) -->
    <g stroke="rgba(72,187,120,0.8)" stroke-width="3" fill="rgba(72,187,120,0.1)">
        <polygon points="900,400 1000,350 1100,400 1100,500 1000,550 900,500" />
        <polygon points="1000,550 1100,500 1200,550 1200,650 1100,700 1000,650" />
        <polygon points="800,550 900,500 1000,550 1000,650 900,700 800,650" />
        <polygon points="900,700 1000,650 1100,700 1100,800 1000,850 900,800" />
    </g>
    
    <g fill="#48BB78">
        <circle cx="1000" cy="450" r="15" />
        <circle cx="1100" cy="600" r="20" />
        <circle cx="900" cy="600" r="10" />
        <circle cx="1000" cy="750" r="25" />
    </g>
    
    <!-- Slightly blurred foreground elements -->
    <g stroke="rgba(49,130,206,0.6)" stroke-width="6" fill="none" filter="url(#dof-blur)">
        <circle cx="600" cy="800" r="150" />
        <circle cx="1400" cy="300" r="100" />
    </g>
    
    <!-- Data overlay -->
    <g fill="#ffffff" font-family="monospace" font-size="14" opacity="0.5">
        <text x="200" y="200">ANALYSIS: BIO_YIELD_0.84</text>
        <text x="200" y="230">PHOTON_FLUX: OPTIMAL</text>
        <text x="200" y="260">CO2_UPTAKE: 42.1g/L/d</text>
        
        <rect x="200" y="300" width="200" height="2" fill="#ffffff" opacity="0.2" />
        <rect x="200" y="300" width="140" height="2" fill="#48BB78" />
        
        <rect x="200" y="320" width="200" height="2" fill="#ffffff" opacity="0.2" />
        <rect x="200" y="320" width="180" height="2" fill="#3182CE" />
    </g>
</svg>"""

# 5. Home Applications
home_applications = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <linearGradient id="sky" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#E2E8F0" />
            <stop offset="100%" stop-color="#FFFFFF" />
        </linearGradient>
        <linearGradient id="fog" x1="0%" y1="100%" x2="0%" y2="0%">
            <stop offset="0%" stop-color="#FFFFFF" stop-opacity="1"/>
            <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
        </linearGradient>
        <filter id="heavy-fog">
            <feGaussianBlur stdDeviation="40" />
        </filter>
        <filter id="light-fog">
            <feGaussianBlur stdDeviation="10" />
        </filter>
    </defs>
    
    <rect width="100%" height="100%" fill="url(#sky)" />
    
    <!-- Background Industrial Blocks -->
    <g fill="#A0AEC0" filter="url(#heavy-fog)" opacity="0.5">
        <rect x="200" y="400" width="300" height="800" />
        <rect x="1400" y="300" width="400" height="900" />
        <rect x="800" y="200" width="200" height="1000" />
    </g>
    
    <!-- Midground Blocks -->
    <g fill="#CBD5E0" filter="url(#light-fog)">
        <rect x="400" y="500" width="400" height="700" />
        <rect x="1100" y="450" width="350" height="750" />
    </g>
    
    <!-- Foreground Carbon Capture Integration (Clean, Geometric, Green accents) -->
    <g fill="#F7FAFC">
        <rect x="650" y="650" width="600" height="450" rx="20" />
        <rect x="680" y="700" width="150" height="400" rx="10" fill="#EDF2F7" />
        <rect x="870" y="700" width="150" height="400" rx="10" fill="#EDF2F7" />
        <rect x="1060" y="700" width="150" height="400" rx="10" fill="#EDF2F7" />
    </g>
    
    <!-- Glowing green integration nodes -->
    <g fill="#48BB78">
        <rect x="730" y="630" width="50" height="10" rx="5" />
        <rect x="920" y="630" width="50" height="10" rx="5" />
        <rect x="1110" y="630" width="50" height="10" rx="5" />
    </g>
    
    <!-- Fog layer overlay -->
    <rect width="100%" height="100%" fill="url(#fog)" opacity="0.8" />
    
    <!-- Sunlight -->
    <circle cx="300" cy="200" r="150" fill="#FFFFFF" filter="url(#heavy-fog)" opacity="0.9" />
</svg>"""

# 6. Home Vision
home_vision = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <radialGradient id="bg" cx="50%" cy="50%" r="70%">
            <stop offset="0%" stop-color="#1A202C" />
            <stop offset="100%" stop-color="#0D1117" />
        </radialGradient>
        <filter id="glow">
            <feGaussianBlur stdDeviation="8" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <filter id="bright-glow">
            <feGaussianBlur stdDeviation="15" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>
    
    <rect width="100%" height="100%" fill="url(#bg)" />
    
    <!-- Isometric Perspective Transform -->
    <g transform="translate(960, 540) scale(1, 0.5) rotate(45)">
        
        <!-- Base Grid -->
        <g stroke="rgba(255,255,255,0.05)" stroke-width="2">
            <!-- generate grid 2000x2000 -->
            <rect x="-1000" y="-1000" width="2000" height="2000" fill="none" />
            <!-- Inner grid lines omitted for brevity, represented abstractly -->
            <path d="M -1000 -600 L 1000 -600 M -1000 -200 L 1000 -200 M -1000 200 L 1000 200 M -1000 600 L 1000 600" />
            <path d="M -600 -1000 L -600 1000 M -200 -1000 L -200 1000 M 200 -1000 L 200 1000 M 600 -1000 L 600 1000" />
        </g>
        
        <!-- Connected Network of Modules -->
        <g stroke="#38A169" stroke-width="4" filter="url(#glow)">
            <line x1="-200" y1="-200" x2="200" y2="-200" />
            <line x1="-200" y1="200" x2="200" y2="200" />
            <line x1="-200" y1="-200" x2="-200" y2="200" />
            <line x1="200" y1="-200" x2="200" y2="200" />
            
            <line x1="200" y1="-200" x2="600" y2="-200" />
            <line x1="-200" y1="200" x2="-200" y2="600" />
        </g>
        
        <!-- Glowing Nodes -->
        <g fill="#48BB78" filter="url(#bright-glow)">
            <circle cx="-200" cy="-200" r="30" />
            <circle cx="200" cy="-200" r="30" />
            <circle cx="-200" cy="200" r="30" />
            <circle cx="200" cy="200" r="40" fill="#68D391" /> <!-- Primary node -->
            
            <circle cx="600" cy="-200" r="25" />
            <circle cx="-200" cy="600" r="25" />
        </g>
        
        <!-- Architecture footprints -->
        <g fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.2)" stroke-width="2">
            <rect x="150" y="150" width="100" height="100" />
            <rect x="-250" y="-250" width="100" height="100" />
        </g>
        
    </g>
    
</svg>"""

files = {
    "home_hero.svg": home_hero,
    "home_system.svg": home_system,
    "home_module.svg": home_module,
    "home_research.svg": home_research,
    "home_applications.svg": home_applications,
    "home_vision.svg": home_vision
}

for name, content in files.items():
    with open(os.path.join(base_dir, name), "w", encoding="utf-8") as f:
        f.write(content)

print("Generated rich SVGs successfully.")
