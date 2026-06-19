import re

with open('/home/aayush/Downloads/Salething/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove light mode CSS
content = re.sub(r'^[ \t]*html\.light.*$\n?', '', content, flags=re.MULTILINE)

# 2. Remove theme storage script in head
content = re.sub(r'<script>\s*if \(localStorage\.getItem\(\'theme\'\).*?</script>\s*', '', content, flags=re.DOTALL)

# 3. Remove theme toggle button
content = re.sub(r'<button class="icon-btn theme-toggle" id="themeToggle".*?</button>\s*', '', content, flags=re.DOTALL)

# 4. Remove theme toggle JS
content = re.sub(r'// ─── THEME TOGGLE ───.*?themeToggle\.innerHTML.*?;\s*', '', content, flags=re.DOTALL)

# 5. Remove .logo-light HTML
content = re.sub(r'<img src="salething%20black%20\.png" alt="Salething Logo" class="logo-light">\s*', '', content)
content = re.sub(r'<img src="salething%20black%20\.png" alt="Salething" class="logo-light">\s*', '', content)

# 6. Remove logo-light CSS
content = re.sub(r'^[ \t]*\.logo-light\s*{.*?}\s*$\n?', '', content, flags=re.MULTILINE)

# 7. Add Caveat font
font_link_target = "family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap"
font_link_replacement = "family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&family=Caveat:wght@500;600;700&display=swap"
content = content.replace(font_link_target, font_link_replacement)

# 8. Add background animation CSS and cursive style
css_addition = """
        /* Enhanced Animated Background */
        body {
            background: linear-gradient(-45deg, #05020a, #150a21, #080312, #180a29);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
        }
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Cursive & Handwriting Animation */
        .cursive {
            font-family: 'Caveat', cursive !important;
            letter-spacing: 2px !important;
            text-transform: none !important;
            font-weight: 600 !important;
        }

        .handwriting {
            display: inline-block;
            overflow: hidden;
            white-space: nowrap;
            border-right: 3px solid var(--purple-light);
            animation: smoothReveal 3s ease-in-out forwards, blink 0.8s step-end infinite;
            max-width: 0;
            padding-right: 6px;
            vertical-align: bottom;
        }

        @keyframes smoothReveal {
            from { max-width: 0; }
            to { max-width: 800px; }
        }
        @keyframes blink {
            50% { border-color: transparent; }
        }
"""
content = content.replace('/* NAVBAR */', css_addition + '\n        /* NAVBAR */')

# 9. Modify hero title to use cursive and typewriter on the accent
hero_title_target = '<span class="accent">Smarter & Faster</span>'
hero_title_replace = '<span class="accent cursive handwriting" style="font-size: 1.1em;">Smarter & Faster</span>'
content = content.replace(hero_title_target, hero_title_replace)

# 10. Update section eyebrows to be cursive
content = content.replace('class="section-eyebrow"', 'class="section-eyebrow cursive" style="font-size: 1.75rem;"')

# 11. Enhance hero-eyebrow
hero_eyebrow_target = 'class="hero-eyebrow"'
hero_eyebrow_replace = 'class="hero-eyebrow cursive" style="font-size: 1.6rem;"'
content = content.replace(hero_eyebrow_target, hero_eyebrow_replace)

with open('/home/aayush/Downloads/Salething/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
