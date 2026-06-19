import json

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Salething — The Digital Marketplace</title>
    
    <!-- SEO Meta Tags -->
    <meta name="description" content="Discover, buy, and sell premium digital goods. Built for creators." />
    <meta property="og:title" content="Salething — The Digital Marketplace" />
    <meta property="og:description" content="Discover, buy, and sell premium digital goods. Built for creators." />
    <meta property="og:image" content="https://via.placeholder.com/1200x630" />
    <meta name="twitter:card" content="summary_large_image" />

    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap"></noscript>
    
    <script>
        if (localStorage.getItem('theme') === 'light') {
            document.documentElement.classList.add('light');
        }
    </script>
    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        :root {
            --bg: #080808;
            --bg2: #101010;
            --bg3: #161616;
            --surface: rgba(255, 255, 255, 0.04);
            --surface-hover: rgba(255, 255, 255, 0.08);
            --border: rgba(255, 255, 255, 0.08);
            --border-accent: rgba(139, 92, 246, 0.4);
            --purple: #8b5cf6;
            --purple-light: #a78bfa;
            --purple-dark: #6d28d9;
            --glow: rgba(139, 92, 246, 0.25);
            --text: #f0f0f0;
            --muted: #888;
            --subtle: #444;
            --font-display: 'Space Grotesk', sans-serif;
            --font-body: 'Inter', sans-serif;
        }

        html.light {
            --bg: #f8f7ff;
            --bg2: #f0eeff;
            --bg3: #e8e4ff;
            --text: #0f0a1e;
            --muted: #6b6b80;
            --border: rgba(0,0,0,0.08);
            --surface: rgba(139,92,246,0.06);
            --surface-hover: rgba(139,92,246,0.12);
        }

        html { scroll-behavior: smooth; }
        body {
            background: var(--bg); color: var(--text);
            font-family: var(--font-body); font-size: 16px; line-height: 1.6;
            overflow-x: hidden;
        }
        
        *:focus-visible {
            outline: 2px solid rgba(139, 92, 246, 0.7);
            outline-offset: 3px;
        }

        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: var(--bg); }
        ::-webkit-scrollbar-thumb { background: var(--subtle); border-radius: 3px; }

        /* NAVBAR */
        nav {
            position: fixed; top: 0; left: 0; right: 0; z-index: 100;
            padding: 0 2rem; height: 68px; display: flex; align-items: center; justify-content: space-between;
            background: rgba(8, 8, 8, 0.3); backdrop-filter: blur(24px); border-bottom: 1px solid var(--border);
            transition: background 0.3s;
        }
        html.light nav { background: rgba(248, 247, 255, 0.3); }
        nav.scrolled { background: rgba(8, 8, 8, 0.85); border-bottom-color: rgba(139, 92, 246, 0.2); }
        html.light nav.scrolled { background: rgba(248, 247, 255, 0.85); }

        .nav-logo { font-family: var(--font-display); font-size: 1.5rem; font-weight: 700; color: var(--text); text-decoration: none; letter-spacing: -0.02em; text-shadow: 0 0 30px rgba(139, 92, 246, 0.7); }
        .nav-links { display: flex; align-items: center; gap: 2rem; list-style: none; }
        .nav-links a { position: relative; color: var(--muted); text-decoration: none; font-size: 0.9rem; font-weight: 500; transition: color 0.2s; letter-spacing: 0.02em; }
        .nav-links a:hover { color: var(--text); }
        .nav-links a::after { content: ''; position: absolute; bottom: -4px; left: 0; width: 100%; height: 2px; background: var(--purple-light); transform: scaleX(0); transform-origin: left; transition: transform 0.3s ease; }
        .nav-links a:hover::after { transform: scaleX(1); }

        .nav-actions { display: flex; align-items: center; gap: 1rem; }
        
        .search-container { position: relative; display: flex; align-items: center; }
        .search-input { width: 0; opacity: 0; border: none; background: var(--surface); color: var(--text); padding: 0; border-radius: 100px; transition: all 0.3s ease; font-family: var(--font-body); font-size: 0.85rem; outline: none; }
        .search-input.active { width: 240px; opacity: 1; padding: 0.4rem 2rem 0.4rem 1rem; border: 1px solid var(--border-accent); }
        .search-toggle { background: none; border: none; color: var(--text); cursor: pointer; display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%; transition: background 0.2s; }
        .search-toggle:hover { background: var(--surface-hover); }
        .search-clear { position: absolute; right: 10px; background: none; border: none; color: var(--muted); cursor: pointer; display: none; }
        .search-input.active + .search-toggle + .search-clear { display: block; }

        .icon-btn { background: var(--surface); border: 1px solid var(--border); border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; cursor: pointer; color: var(--text); transition: all 0.2s; position: relative; }
        .icon-btn:hover { background: var(--surface-hover); border-color: var(--border-accent); }
        .cart-badge { position: absolute; top: -4px; right: -4px; background: var(--purple); color: #fff; font-size: 0.65rem; font-weight: bold; width: 16px; height: 16px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }

        .nav-cta { background: linear-gradient(135deg, var(--purple), var(--purple-dark)); color: #fff !important; padding: 0.55rem 1.4rem; border-radius: 100px; font-weight: 600; font-size: 0.875rem !important; transition: box-shadow 0.3s, transform 0.2s !important; box-shadow: 0 0 0 0 var(--glow); border: none; cursor: pointer; text-decoration: none;}
        .nav-cta:hover { box-shadow: 0 0 24px var(--glow), 0 0 48px rgba(139, 92, 246, 0.15) !important; transform: translateY(-1px); color: #fff !important; }
        .nav-cta::after { display: none; }

        .hamburger { display: none; flex-direction: column; gap: 5px; cursor: pointer; padding: 4px; background: none; border: none; }
        .hamburger span { display: block; width: 22px; height: 2px; background: var(--text); border-radius: 2px; transition: 0.3s; }

        /* HERO */
        #hero { min-height: 100vh; position: relative; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 10rem 2rem 6rem; overflow: hidden; }
        .hero-bg-canvas { position: absolute; inset: 0; z-index: 0; width: 100%; height: 100%; pointer-events: none; }
        .hero-bg-overlay { position: absolute; inset: 0; background: radial-gradient(circle at 50% 50%, rgba(139,92,246,0.1), transparent 70%); pointer-events: none; z-index: 0; }
        .hero-content-wrapper { position: relative; z-index: 1; display: flex; flex-direction: column; align-items: center; }

        .hero-grid { position: absolute; inset: 0; z-index: 0; background-image: linear-gradient(var(--border) 1px, transparent 1px), linear-gradient(90deg, var(--border) 1px, transparent 1px); background-size: 60px 60px; mask-image: radial-gradient(ellipse 80% 80% at 50% 50%, black 30%, transparent 80%); -webkit-mask-image: radial-gradient(ellipse 80% 80% at 50% 50%, black 30%, transparent 80%); }

        .hero-eyebrow { display: inline-flex; align-items: center; gap: 8px; background: rgba(139, 92, 246, 0.12); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 100px; padding: 0.35rem 1rem; font-size: 0.8rem; font-weight: 500; color: var(--purple-light); letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 1.75rem; position: relative; }
        .hero-eyebrow::before { content: ''; width: 6px; height: 6px; border-radius: 50%; background: var(--purple-light); animation: pulse 2s ease-in-out infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.5; transform: scale(0.8); } }

        .hero-title { font-family: var(--font-display); font-size: clamp(2.8rem, 7vw, 6rem); font-weight: 700; line-height: 1.05; letter-spacing: -0.03em; color: var(--text); margin-bottom: 1.5rem; }
        .hero-title .accent { background: linear-gradient(135deg, var(--purple-light), #c084fc, #e879f9); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
        .hero-sub { font-size: 1.1rem; color: var(--muted); max-width: 560px; margin: 0 auto 2.5rem; font-weight: 400; line-height: 1.7; }
        .hero-actions { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-bottom: 4rem; }

        .btn-primary { background: linear-gradient(135deg, var(--purple), var(--purple-dark)); color: #fff; padding: 0.85rem 2rem; border-radius: 100px; font-weight: 600; font-size: 0.95rem; text-decoration: none; border: none; cursor: pointer; transition: box-shadow 0.3s, transform 0.2s; box-shadow: 0 4px 24px rgba(139, 92, 246, 0.3); font-family: var(--font-body); }
        .btn-primary:hover { box-shadow: 0 8px 40px rgba(139, 92, 246, 0.5); transform: translateY(-2px); }
        .btn-ghost { background: transparent; color: var(--text); padding: 0.85rem 2rem; border-radius: 100px; font-weight: 500; font-size: 0.95rem; text-decoration: none; border: 1px solid var(--border); cursor: pointer; transition: border-color 0.3s, background 0.3s; font-family: var(--font-body); display: flex; align-items: center; gap: 0.5rem; }
        .btn-ghost:hover { border-color: rgba(139, 92, 246, 0.5); background: var(--surface-hover); }
        .play-icon { width: 18px; height: 18px; background: var(--purple-light); border-radius: 50%; display: flex; align-items: center; justify-content: center; }
        .play-icon::after { content: ''; border-style: solid; border-width: 4px 0 4px 7px; border-color: transparent transparent transparent #fff; margin-left: 1px; }

        .video-card { position: relative; width: 100%; max-width: 820px; border-radius: 20px; overflow: hidden; border: 1px solid var(--border-accent); box-shadow: 0 0 60px rgba(139, 92, 246, 0.2); background: var(--surface); backdrop-filter: blur(20px); z-index: 1; }
        .video-bar { display: flex; align-items: center; gap: 8px; padding: 0.75rem 1rem; border-bottom: 1px solid var(--border); background: rgba(255, 255, 255, 0.03); }
        html.light .video-bar { background: rgba(0,0,0,0.03); }
        .video-dot { width: 10px; height: 10px; border-radius: 50%; }
        video, .video-placeholder { width: 100%; display: block; aspect-ratio: 16/9; }
        .video-placeholder { background: linear-gradient(135deg, #0f0a1e 0%, #1a0d35 50%, #0d0d0d 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 1rem; cursor: pointer; }
        .play-btn-large { width: 70px; height: 70px; border-radius: 50%; background: linear-gradient(135deg, var(--purple), var(--purple-dark)); display: flex; align-items: center; justify-content: center; box-shadow: 0 0 40px rgba(139, 92, 246, 0.5); transition: transform 0.2s, box-shadow 0.3s; cursor: pointer; border: none; }
        .play-btn-large:hover { transform: scale(1.1); box-shadow: 0 0 60px rgba(139, 92, 246, 0.7); }
        .play-btn-large::after { content: ''; border-style: solid; border-width: 12px 0 12px 22px; border-color: transparent transparent transparent #fff; margin-left: 4px; }
        .video-placeholder p { color: rgba(255,255,255,0.7); font-size: 0.875rem; }

        /* STATS */
        .stats-strip { display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap; padding: 3.5rem 2rem; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); background: var(--bg2); }
        .stat { text-align: center; }
        .stat-num { font-family: var(--font-display); font-size: 2.25rem; font-weight: 700; color: var(--text); letter-spacing: -0.03em; background: linear-gradient(135deg, var(--text), var(--purple-light)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
        .stat-label { font-size: 0.8rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; margin-top: 2px; }

        section { padding: 6rem 2rem; }
        .section-inner { max-width: 1200px; margin: 0 auto; }
        .section-eyebrow { font-size: 0.75rem; font-weight: 600; color: var(--purple-light); letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 0.75rem; }
        .section-title { font-family: var(--font-display); font-size: clamp(2rem, 4vw, 3rem); font-weight: 700; letter-spacing: -0.03em; color: var(--text); margin-bottom: 1rem; line-height: 1.1; }
        .section-sub { color: var(--muted); font-size: 1rem; max-width: 500px; margin-bottom: 3.5rem; line-height: 1.7; }

        /* PRODUCTS */
        #products { background: var(--bg); }
        .products-header { display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 1rem; margin-bottom: 3rem; }
        .filter-tabs { display: flex; gap: 0.5rem; flex-wrap: wrap; }
        .filter-tab { background: transparent; color: var(--muted); border: 1px solid var(--border); padding: 0.4rem 1rem; border-radius: 100px; font-size: 0.8rem; font-weight: 500; cursor: pointer; transition: all 0.2s; font-family: var(--font-body); }
        .filter-tab.active, .filter-tab:hover { background: rgba(139, 92, 246, 0.15); border-color: var(--border-accent); color: var(--purple-light); }

        .product-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem; }
        .product-card { background: var(--surface); backdrop-filter: blur(20px); border: 1px solid var(--border); border-radius: 16px; overflow: hidden; transition: transform 0.3s, border-color 0.3s, box-shadow 0.3s, opacity 0.2s; cursor: pointer; position: relative; }
        .product-card:hover { transform: translateY(-6px) scale(1.01); border-color: var(--border-accent); box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), 0 0 40px rgba(139, 92, 246, 0.15); }
        html.light .product-card:hover { box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1), 0 0 40px rgba(139, 92, 246, 0.15); }

        .product-thumb-placeholder { width: 100%; aspect-ratio: 16/10; display: flex; align-items: center; justify-content: center; font-size: 3rem; position: relative; overflow: hidden; background: #1a1a2e; transition: background 0.3s; }
        .product-body { padding: 1.25rem; }
        .product-tag { display: inline-block; background: rgba(139, 92, 246, 0.15); border: 1px solid rgba(139, 92, 246, 0.3); color: var(--purple-light); font-size: 0.7rem; font-weight: 600; padding: 2px 10px; border-radius: 100px; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 0.6rem; }
        .product-name { font-family: var(--font-display); font-size: 1rem; font-weight: 600; color: var(--text); margin-bottom: 0.4rem; line-height: 1.3; }
        .product-desc { font-size: 0.82rem; color: var(--muted); line-height: 1.5; margin-bottom: 1rem; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
        .product-footer { display: flex; align-items: center; justify-content: space-between; margin-top: 0.75rem; }
        .stars { color: #f59e0b; font-size: 0.8rem; letter-spacing: 1px; }
        .rating-count { font-size: 0.72rem; color: var(--subtle); margin-left: 4px; }
        .product-price { font-family: var(--font-display); font-size: 1.25rem; font-weight: 700; color: var(--text); }
        
        .add-cart { margin-top: 1rem; width: 100%; background: linear-gradient(135deg, var(--purple), var(--purple-dark)); color: #fff; border: none; padding: 0.65rem; border-radius: 10px; font-weight: 600; font-size: 0.875rem; cursor: pointer; font-family: var(--font-body); transition: box-shadow 0.3s, transform 0.2s; }
        .add-cart:hover { box-shadow: 0 8px 30px rgba(139, 92, 246, 0.4); transform: translateY(-1px); }
        .badge-new { position: absolute; top: 12px; right: 12px; background: rgba(139, 92, 246, 0.9); color: #fff; font-size: 0.65rem; font-weight: 700; padding: 3px 9px; border-radius: 100px; letter-spacing: 0.08em; text-transform: uppercase; z-index: 2; }

        .compare-checkbox-container { position: absolute; top: 12px; left: 12px; z-index: 10; }
        .compare-checkbox { accent-color: var(--purple); width: 18px; height: 18px; cursor: pointer; }

        .quick-view-btn { position: absolute; bottom: 0; left: 0; right: 0; background: rgba(0,0,0,0.8); color: #fff; padding: 0.5rem; text-align: center; font-size: 0.85rem; font-weight: bold; transform: translateY(100%); transition: transform 0.3s ease; cursor: pointer; border: none; }
        .product-card:hover .quick-view-btn { transform: translateY(0); }

        /* BENTO GRID ABOUT */
        #about { background: var(--bg2); }
        .bento-grid { display: grid; grid-template-columns: repeat(3, 1fr); grid-auto-rows: minmax(180px, auto); gap: 1.5rem; grid-template-areas: "c1 c1 c2" "c3 c4 c4" "c3 c5 c5"; }
        @media (max-width: 900px) { .bento-grid { grid-template-columns: 1fr; grid-template-areas: "c1" "c2" "c3" "c4" "c5"; } }
        .bento-cell { background: var(--surface); backdrop-filter: blur(20px); border: 1px solid var(--border); border-radius: 24px; padding: 2rem; position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: center; }
        .bento-c1 { grid-area: c1; border-color: var(--border-accent); }
        .bento-c2 { grid-area: c2; text-align: center; }
        .bento-c3 { grid-area: c3; align-items: center; justify-content: center; padding: 1rem; }
        .bento-c4 { grid-area: c4; justify-content: center; padding: 0; }
        .bento-c5 { grid-area: c5; align-items: flex-start; }
        .bento-c1 h3 { font-family: var(--font-display); font-size: 2rem; color: var(--text); margin-bottom: 1rem; }
        .bento-c1 p { color: var(--muted); }
        .bento-c2 .counter { font-family: var(--font-display); font-size: 3.5rem; font-weight: 700; color: var(--purple-light); line-height:1; }
        .bento-c2 .label { color: var(--muted); font-size: 0.9rem; text-transform: uppercase; margin-top: 0.5rem; }
        .bento-c3 svg { width: 100%; height: auto; opacity: 0.8; stroke: var(--muted); }
        .map-dot { fill: var(--purple); animation: pulse 2s infinite; }
        .ticker-wrap { width: 100%; overflow: hidden; display: flex; white-space: nowrap; padding: 1.5rem 0; background: rgba(0,0,0,0.1); }
        html.light .ticker-wrap { background: rgba(0,0,0,0.03); }
        .ticker { display: inline-block; animation: ticker 20s linear infinite; padding-left: 100%; }
        .ticker-item { display: inline-block; padding: 0 2rem; font-family: var(--font-display); font-size: 1.2rem; color: var(--text); font-weight: 500; }
        @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }

        /* FEATURES */
        #features { background: var(--bg); }
        .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; }
        .feature-card { background: var(--surface); backdrop-filter: blur(20px); border: 1px solid var(--border); border-radius: 16px; padding: 2rem; transition: border-color 0.3s, box-shadow 0.3s; position: relative; overflow: hidden; }
        .feature-card::before { content: ''; position: absolute; top: -40px; right: -40px; width: 100px; height: 100px; border-radius: 50%; background: var(--glow); filter: blur(40px); opacity: 0; transition: opacity 0.3s; }
        .feature-card:hover { border-color: var(--border-accent); box-shadow: 0 8px 40px rgba(0, 0, 0, 0.3); }
        html.light .feature-card:hover { box-shadow: 0 8px 40px rgba(0, 0, 0, 0.05); }
        .feature-card:hover::before { opacity: 1; }
        .feature-icon { width: 52px; height: 52px; border-radius: 14px; background: rgba(139, 92, 246, 0.12); border: 1px solid rgba(139, 92, 246, 0.25); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; margin-bottom: 1.25rem; }
        .feature-title { font-family: var(--font-display); font-size: 1.1rem; font-weight: 600; color: var(--text); margin-bottom: 0.5rem; }
        .feature-desc { font-size: 0.875rem; color: var(--muted); line-height: 1.65; }

        /* TESTIMONIALS */
        #testimonials { background: var(--bg2); }
        .testimonials-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; }
        .testimonial-card { background: var(--surface); backdrop-filter: blur(20px); border: 1px solid var(--border); border-radius: 16px; padding: 2rem; transition: border-color 0.3s; position: relative; }
        .testimonial-card:hover { border-color: var(--border-accent); }
        .testimonial-quote { font-size: 0.95rem; color: var(--text); line-height: 1.75; margin-bottom: 1.5rem; position: relative; }
        .testimonial-quote::before { content: '"'; font-family: var(--font-display); font-size: 4rem; color: var(--purple); line-height: 0; position: absolute; top: 1rem; left: -0.25rem; opacity: 0.3; }
        .testimonial-author { display: flex; align-items: center; gap: 0.875rem; }
        .avatar { width: 42px; height: 42px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.875rem; color: #fff; flex-shrink: 0; font-family: var(--font-display); }
        .author-name { font-weight: 600; font-size: 0.9rem; color: var(--text); }
        .author-role { font-size: 0.78rem; color: var(--muted); }
        .t-stars { color: #f59e0b; font-size: 0.8rem; margin-bottom: 1rem; }

        /* CTA BAND */
        .cta-band { padding: 5rem 2rem; background: var(--bg); text-align: center; position: relative; overflow: hidden; border-top: 1px solid var(--border); }
        .cta-band::before { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse 60% 80% at 50% 50%, rgba(139, 92, 246, 0.12), transparent 70%); }
        .cta-band .section-title { margin-bottom: 1rem; }
        .cta-band .section-sub { margin: 0 auto 2.5rem; }
        .cta-band-actions { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; position: relative; }

        /* FOOTER */
        footer { background: var(--bg2); border-top: 1px solid var(--border); position: relative; overflow: hidden; padding: 4rem 2rem 2rem; }
        .footer-watermark { position: absolute; bottom: -0.15em; left: 50%; transform: translateX(-50%); font-family: var(--font-display); font-size: clamp(5rem, 18vw, 14rem); font-weight: 700; letter-spacing: -0.04em; color: var(--text); opacity: 0.04; white-space: nowrap; pointer-events: none; user-select: none; line-height: 1; z-index: 0; }
        .footer-inner { max-width: 1200px; margin: 0 auto; position: relative; z-index: 1; }
        .footer-top { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 3rem; margin-bottom: 3rem; }
        .footer-brand .brand-logo { font-family: var(--font-display); font-size: 1.5rem; font-weight: 700; color: var(--text); letter-spacing: -0.02em; text-shadow: 0 0 20px rgba(139, 92, 246, 0.5); margin-bottom: 0.75rem; }
        .footer-brand p { font-size: 0.875rem; color: var(--muted); line-height: 1.7; max-width: 280px; }
        .social-links { display: flex; gap: 0.75rem; margin-top: 1.25rem; }
        .social-link { width: 38px; height: 38px; background: var(--surface); border: 1px solid var(--border); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: var(--muted); text-decoration: none; font-size: 0.85rem; transition: border-color 0.2s, color 0.2s, background 0.2s; }
        .social-link:hover { border-color: var(--border-accent); color: var(--purple-light); background: rgba(139, 92, 246, 0.1); }
        .footer-col h4 { font-family: var(--font-display); font-size: 0.85rem; font-weight: 600; color: var(--text); letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 1.25rem; }
        .footer-col ul { list-style: none; display: flex; flex-direction: column; gap: 0.6rem; }
        .footer-col ul a { color: var(--muted); text-decoration: none; font-size: 0.875rem; transition: color 0.2s; }
        .footer-col ul a:hover { color: var(--text); }
        .footer-bottom { border-top: 1px solid var(--border); padding-top: 2rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; }
        .footer-copy { font-size: 0.8rem; color: var(--subtle); }
        .footer-bottom-links { display: flex; gap: 1.5rem; }
        .footer-bottom-links a { font-size: 0.8rem; color: var(--subtle); text-decoration: none; transition: color 0.2s; }
        .footer-bottom-links a:hover { color: var(--muted); }

        /* ANIMATIONS & STATES */
        .fade-in { opacity: 0; transform: translateY(30px); transition: opacity 0.7s ease, transform 0.7s ease; }
        .fade-in.visible { opacity: 1; transform: none; }
        
        .stagger-child { opacity: 0; transform: translateY(20px); transition: opacity 0.5s ease, transform 0.5s ease; }
        .stagger-child.visible { opacity: 1; transform: translateY(0); }

        /* CART DRAWER */
        .cart-drawer { position: fixed; top: 0; right: 0; bottom: 0; width: 380px; background: rgba(10, 10, 10, 0.92); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border-left: 1px solid rgba(139, 92, 246, 0.25); z-index: 250; transform: translateX(100%); transition: transform 0.35s ease; display: flex; flex-direction: column; color: #fff; }
        html.light .cart-drawer { background: rgba(255, 255, 255, 0.92); color: #000; border-left: 1px solid rgba(0,0,0,0.1); }
        @media (max-width: 400px) { .cart-drawer { width: 100%; } }
        .cart-drawer.open { transform: translateX(0); }
        .cart-header { padding: 1.5rem; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; }
        .cart-header h3 { font-family: var(--font-display); }
        .close-drawer { background: none; border: none; color: inherit; font-size: 1.5rem; cursor: pointer; }
        .cart-items { flex: 1; overflow-y: auto; padding: 1.5rem; }
        .cart-footer { padding: 1.5rem; border-top: 1px solid var(--border); }
        .cart-item { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; padding-bottom: 1rem; border-bottom: 1px solid var(--border); }
        .cart-item-info h4 { font-size: 0.95rem; margin-bottom: 0.25rem; font-family: var(--font-body); }
        .cart-item-info p { font-size: 0.85rem; color: var(--muted); }
        .cart-item-controls { display: flex; align-items: center; gap: 0.5rem; }
        .cart-btn { background: var(--surface); border: 1px solid var(--border); color: inherit; width: 24px; height: 24px; border-radius: 4px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
        .cart-subtotal { display: flex; justify-content: space-between; font-size: 1.2rem; font-weight: bold; margin-bottom: 1rem; }
        .checkout-btn { width: 100%; background: linear-gradient(135deg, var(--purple), var(--purple-dark)); color: #fff; border: none; padding: 1rem; border-radius: 12px; font-weight: bold; cursor: pointer; font-family: var(--font-body); font-size: 1rem; }

        /* COMPARE BAR & MODAL */
        .compare-bar { position: fixed; bottom: 0; left: 0; right: 0; height: 72px; background: rgba(10, 10, 10, 0.9); backdrop-filter: blur(24px); border-top: 2px solid var(--purple); box-shadow: 0 -4px 20px rgba(139, 92, 246, 0.2); display: flex; align-items: center; justify-content: space-between; padding: 0 2rem; z-index: 150; transform: translateY(100%); transition: transform 0.3s ease; }
        html.light .compare-bar { background: rgba(255,255,255,0.9); }
        .compare-bar.visible { transform: translateY(0); }
        .compare-items { display: flex; gap: 1rem; }
        .compare-pill { background: var(--surface); border: 1px solid var(--border); padding: 0.4rem 1rem; border-radius: 100px; font-size: 0.85rem; color: var(--text); }
        .modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.8); backdrop-filter: blur(8px); z-index: 200; display: flex; align-items: center; justify-content: center; opacity: 0; pointer-events: none; transition: opacity 0.3s ease; }
        .modal-overlay.active { opacity: 1; pointer-events: auto; }
        .compare-modal { background: var(--bg2); border: 1px solid var(--purple); box-shadow: 0 0 40px rgba(139, 92, 246, 0.2); border-radius: 20px; width: 90%; max-width: 900px; max-height: 90vh; overflow-y: auto; padding: 2rem; position: relative; }
        .close-modal { position: absolute; top: 1rem; right: 1rem; background: none; border: none; color: var(--text); font-size: 1.5rem; cursor: pointer; }
        .compare-table { width: 100%; border-collapse: collapse; margin-top: 1rem; color: var(--text); }
        .compare-table th, .compare-table td { padding: 1rem; border: 1px solid var(--border); text-align: left; }
        .compare-table th { background: var(--surface); color: var(--purple-light); }

        /* QUICK VIEW MODAL */
        .qv-modal { background: var(--surface); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border: 1px solid rgba(139, 92, 246, 0.4); box-shadow: 0 0 40px rgba(139, 92, 246, 0.2); border-radius: 20px; width: 90%; max-width: 680px; padding: 2rem; position: relative; display: flex; gap: 2rem; transform: scale(0.95); opacity: 0; transition: all 0.25s ease; color: var(--text); }
        .modal-overlay.active .qv-modal { transform: scale(1); opacity: 1; }
        .qv-left { flex: 1; border-radius: 12px; overflow: hidden; display: flex; align-items: center; justify-content: center; font-size: 4rem; min-height: 200px; }
        .qv-right { flex: 1; display: flex; flex-direction: column; }
        .qv-title { font-family: var(--font-display); font-size: 1.75rem; color: var(--text); margin-bottom: 0.5rem; }
        .qv-cat { display: inline-block; background: rgba(139,92,246,0.15); color: var(--purple-light); padding: 2px 10px; border-radius: 100px; font-size: 0.75rem; margin-bottom: 1rem; align-self: flex-start; }
        .qv-desc { color: var(--muted); font-size: 0.9rem; margin-bottom: 1rem; line-height: 1.5; }
        .qv-features { list-style: none; margin-bottom: 1.5rem; font-size: 0.85rem; color: var(--text); }
        .qv-features li { margin-bottom: 0.3rem; }
        .qv-features li::before { content: '✓'; color: var(--purple); margin-right: 0.5rem; font-weight: bold; }
        .qv-price { font-family: var(--font-display); font-size: 1.5rem; font-weight: bold; color: var(--text); margin-bottom: 1rem; }
        .qv-actions { display: flex; gap: 1rem; margin-top: auto; }
        .qv-actions .btn-primary { flex: 1; text-align: center; padding: 0.8rem; }
        .qv-actions .btn-ghost { flex: 1; text-align: center; padding: 0.8rem; justify-content: center;}
        @media (max-width: 600px) { .qv-modal { flex-direction: column; } .compare-bar { flex-direction: column; height: auto; padding: 1rem; gap: 1rem;} .compare-items { flex-wrap: wrap; justify-content: center;} }

        @keyframes flyToCart { 0% { transform: scale(1); opacity: 1; } 100% { transform: scale(0.3) translate(var(--tx), var(--ty)); opacity: 0; } }
        .flying-emoji { position: fixed; z-index: 1000; font-size: 2rem; pointer-events: none; }

        @media (max-width: 900px) {
            .footer-top { grid-template-columns: 1fr 1fr; }
            .nav-links { display: none; }
            .nav-links.open { display: flex; flex-direction: column; position: absolute; top: 68px; left: 0; right: 0; background: rgba(10, 10, 10, 0.97); padding: 1.5rem 2rem 2rem; border-bottom: 1px solid var(--border); gap: 1.25rem; }
            html.light .nav-links.open { background: rgba(255,255,255,0.97); }
            .hamburger { display: flex; }
        }
        @media (max-width: 600px) {
            .footer-top { grid-template-columns: 1fr; gap: 2rem; }
            .stats-strip { gap: 2rem; }
            .footer-bottom { flex-direction: column; align-items: flex-start; }
            section { padding: 4rem 1.25rem; }
            .hero-title { font-size: 2.5rem; }
        }
        @media (prefers-reduced-motion: reduce) {
            *, .fade-in, .stagger-child { animation: none !important; transition: none !important; }
            .fade-in, .stagger-child { opacity: 1; transform: none; }
        }
    </style>
</head>
<body>

    <!-- NAVBAR -->
    <nav id="navbar">
        <a class="nav-logo" href="#" tabindex="0">Salething</a>
        <ul class="nav-links" id="navLinks">
            <li><a href="#hero" tabindex="0">Home</a></li>
            <li><a href="#products" tabindex="0">Products</a></li>
            <li><a href="#about" tabindex="0">About</a></li>
            <li><a href="#features" tabindex="0">Features</a></li>
            <li><a href="#testimonials" tabindex="0">Reviews</a></li>
        </ul>
        <div class="nav-actions">
            <div class="search-container">
                <input type="text" id="searchInput" class="search-input" placeholder="Search products..." aria-label="Search">
                <button class="search-toggle icon-btn" id="searchToggle" aria-label="Toggle Search">🔍</button>
                <button class="search-clear" id="searchClear" aria-label="Clear Search">×</button>
            </div>
            <button class="icon-btn theme-toggle" id="themeToggle" aria-label="Toggle Theme">☀️</button>
            <button class="icon-btn cart-toggle" id="cartToggle" aria-label="Open Cart">
                🛒
                <span class="cart-badge" id="cartBadge">0</span>
            </button>
            <a href="#products" class="nav-cta" tabindex="0">Get Started</a>
            <button class="hamburger" id="hamburger" aria-label="Toggle menu">
                <span></span><span></span><span></span>
            </button>
        </div>
    </nav>

    <!-- CART DRAWER -->
    <div class="cart-drawer" id="cartDrawer">
        <div class="cart-header">
            <h3>Your Cart</h3>
            <button class="close-drawer" id="closeCartBtn" aria-label="Close Cart">×</button>
        </div>
        <div class="cart-items" id="cartItemsList">
            <!-- Cart items go here -->
        </div>
        <div class="cart-footer">
            <div class="cart-subtotal">
                <span>Subtotal</span>
                <span id="cartSubtotal">$0.00</span>
            </div>
            <button class="checkout-btn" tabindex="0">Checkout Now</button>
        </div>
    </div>

    <!-- HERO -->
    <section id="hero">
        <canvas id="heroCanvas" class="hero-bg-canvas"></canvas>
        <div class="hero-bg-overlay"></div>
        <div class="hero-grid"></div>
        <div class="hero-content-wrapper">
            <div class="hero-eyebrow">The #1 Digital Marketplace</div>
            <h1 class="hero-title">
                Sell Digital Products<br><span class="accent">Smarter & Faster</span>
            </h1>
            <p class="hero-sub">Discover, buy, and sell premium digital goods — templates, software, courses, and more. Built for creators who mean business.</p>
            <div class="hero-actions">
                <a href="#products" class="btn-primary" tabindex="0">Browse Products</a>
                <button class="btn-ghost" id="watchDemo" tabindex="0">
                    <span class="play-icon"></span> Watch Demo
                </button>
            </div>
            <!-- VIDEO CARD -->
            <div class="video-card fade-in" id="videoCard">
                <div class="video-bar">
                    <div class="video-dot" style="background:#ff5f57"></div>
                    <div class="video-dot" style="background:#ffbd2e"></div>
                    <div class="video-dot" style="background:#28c840"></div>
                    <span style="font-size:0.75rem;color:var(--muted);margin-left:8px;font-family:var(--font-body)">salething.io — Intro</span>
                </div>
                <div class="video-placeholder" id="videoPlaceholder">
                    <button class="play-btn-large" id="playBtn" aria-label="Play intro video" tabindex="0"></button>
                    <p>Watch the 2-minute product tour</p>
                </div>
                <video id="heroVideo" style="display:none;width:100%" controls>
                    <source src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" type="video/mp4" />
                </video>
            </div>
        </div>
    </section>

    <!-- STATS STRIP -->
    <div class="stats-strip">
        <div class="stat">
            <div class="stat-num" data-target="40" data-suffix="K+">0</div>
            <div class="stat-label">Digital Products</div>
        </div>
        <div class="stat">
            <div class="stat-num" data-target="120" data-suffix="K">0</div>
            <div class="stat-label">Happy Buyers</div>
        </div>
        <div class="stat">
            <div class="stat-num" data-prefix="$" data-target="8" data-suffix="M+">0</div>
            <div class="stat-label">Creator Earnings</div>
        </div>
        <div class="stat">
            <div class="stat-num" data-target="4.9" data-suffix="★">0</div>
            <div class="stat-label">Avg. Rating</div>
        </div>
    </div>

    <!-- PRODUCTS -->
    <section id="products">
        <div class="section-inner">
            <div class="products-header">
                <div>
                    <p class="section-eyebrow">Marketplace</p>
                    <h2 class="section-title">Featured Products</h2>
                    <p class="section-sub">Handpicked premium digital products from our top creators.</p>
                </div>
                <div class="filter-tabs">
                    <button class="filter-tab active" tabindex="0">All</button>
                    <button class="filter-tab" tabindex="0">Templates</button>
                    <button class="filter-tab" tabindex="0">Software</button>
                    <button class="filter-tab" tabindex="0">Courses</button>
                    <button class="filter-tab" tabindex="0">Assets</button>
                </div>
            </div>
            <div class="product-grid stagger-grid" id="productGrid"></div>
        </div>
    </section>

    <!-- COMPARE BAR & MODAL -->
    <div class="compare-bar" id="compareBar">
        <div class="compare-items" id="compareItems"></div>
        <button class="btn-primary" id="compareNowBtn" tabindex="0">Compare Now</button>
    </div>
    
    <div class="modal-overlay" id="compareModalOverlay">
        <div class="compare-modal">
            <button class="close-modal" id="closeCompareModal" aria-label="Close Comparison">×</button>
            <h2 class="section-title" style="font-size:1.5rem;margin-bottom:0">Product Comparison</h2>
            <div id="compareTableContainer" style="overflow-x:auto;"></div>
        </div>
    </div>

    <!-- QUICK VIEW MODAL -->
    <div class="modal-overlay" id="quickViewModalOverlay">
        <div class="qv-modal">
            <button class="close-modal" id="closeQvModal" aria-label="Close Quick View">×</button>
            <div class="qv-left" id="qvEmojiContainer">
                <span id="qvEmoji">✨</span>
            </div>
            <div class="qv-right">
                <span class="qv-cat" id="qvCat">Category</span>
                <h2 class="qv-title" id="qvName">Product Name</h2>
                <div style="margin-bottom:1rem;" id="qvStars"></div>
                <p class="qv-desc" id="qvDesc">Description...</p>
                <ul class="qv-features">
                    <li>High quality assets</li>
                    <li>Instant digital access</li>
                    <li>Premium creator support</li>
                </ul>
                <div class="qv-price" id="qvPrice">$0.00</div>
                <div class="qv-actions">
                    <button class="btn-primary" id="qvAddToCart" tabindex="0">Add to Cart</button>
                    <button class="btn-ghost" tabindex="0">Full Details</button>
                </div>
            </div>
        </div>
    </div>

    <!-- BENTO GRID ABOUT -->
    <section id="about">
        <div class="section-inner">
            <p class="section-eyebrow">About Salething</p>
            <h2 class="section-title">We empower creators</h2>
            <div class="bento-grid stagger-grid">
                <div class="bento-cell bento-c1 stagger-child">
                    <h3>We built the marketplace creators deserve.</h3>
                    <p>Salething was designed from the ground up to eliminate the friction between creating and earning. No more complex setups or hidden fees.</p>
                </div>
                <div class="bento-cell bento-c2 stagger-child">
                    <div class="counter stat-num" data-target="3" data-suffix="">0</div>
                    <div class="label">yrs in the market</div>
                </div>
                <div class="bento-cell bento-c3 stagger-child">
                    <svg viewBox="0 0 1000 500" preserveAspectRatio="xMidYMid meet">
                        <path d="M150,150 Q200,100 250,150 T350,200 Q400,250 450,200 T550,150 Q600,100 650,150 T750,200 Q800,250 850,200 T950,150" fill="none" stroke-width="4" stroke-linecap="round"/>
                        <circle cx="200" cy="150" r="10" class="map-dot"/>
                        <circle cx="450" cy="200" r="10" class="map-dot" style="animation-delay: 0.5s"/>
                        <circle cx="800" cy="250" r="10" class="map-dot" style="animation-delay: 1s"/>
                    </svg>
                </div>
                <div class="bento-cell bento-c4 stagger-child">
                    <div class="ticker-wrap">
                        <div class="ticker">
                            <span class="ticker-item">Alex J. · $12,400 · Notion Templates</span>
                            <span class="ticker-item">Sarah M. · $8,200 · UI Kits</span>
                            <span class="ticker-item">David K. · $15,100 · Video Courses</span>
                            <span class="ticker-item">Elena R. · $5,300 · Brushes</span>
                            <span class="ticker-item">Alex J. · $12,400 · Notion Templates</span>
                        </div>
                    </div>
                </div>
                <div class="bento-cell bento-c5 stagger-child">
                    <h3>Join Us</h3>
                    <p style="color:var(--muted); font-size:0.85rem; margin-bottom:1rem;">Start your journey today.</p>
                    <a href="#" class="btn-primary" style="width:100%; text-align:center;" tabindex="0">Apply Now</a>
                </div>
            </div>
        </div>
    </section>

    <!-- FEATURES -->
    <section id="features">
        <div class="section-inner">
            <p class="section-eyebrow">Why Salething</p>
            <h2 class="section-title">Built for Creators</h2>
            <p class="section-sub">Everything you need to launch, sell, and scale your digital product business.</p>
            <div class="features-grid stagger-grid">
                <div class="feature-card stagger-child">
                    <div class="feature-icon">⚡</div>
                    <h3 class="feature-title">Instant Delivery</h3>
                    <p class="feature-desc">Buyers receive their files the second payment clears. No manual sending, no delays — fully automated digital fulfillment.</p>
                </div>
                <div class="feature-card stagger-child">
                    <div class="feature-icon">🔒</div>
                    <h3 class="feature-title">Secure Payments</h3>
                    <p class="feature-desc">Bank-grade encryption and fraud detection protect every transaction. Stripe-powered checkout with global currency support.</p>
                </div>
                <div class="feature-card stagger-child">
                    <div class="feature-icon">📊</div>
                    <h3 class="feature-title">Creator Analytics</h3>
                    <p class="feature-desc">Real-time dashboards showing your sales, traffic sources, conversion rates, and revenue breakdown at a glance.</p>
                </div>
                <div class="feature-card stagger-child">
                    <div class="feature-icon">🌍</div>
                    <h3 class="feature-title">Global Reach</h3>
                    <p class="feature-desc">Sell to customers in 180+ countries with automatic tax handling, multi-currency support, and localized checkout pages.</p>
                </div>
                <div class="feature-card stagger-child">
                    <div class="feature-icon">🎯</div>
                    <h3 class="feature-title">Smart Discovery</h3>
                    <p class="feature-desc">Our algorithm surfaces your products to the right buyers at the right time based on browsing behavior and purchase history.</p>
                </div>
                <div class="feature-card stagger-child">
                    <div class="feature-icon">💬</div>
                    <h3 class="feature-title">24/7 Support</h3>
                    <p class="feature-desc">Our human support team and AI assistant are available around the clock for both creators and buyers on any issue.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- TESTIMONIALS -->
    <section id="testimonials">
        <div class="section-inner">
            <p class="section-eyebrow">Community</p>
            <h2 class="section-title">Creators Love It</h2>
            <p class="section-sub">Thousands of independent creators have grown their business with Salething.</p>
            <div class="testimonials-grid stagger-grid">
                <div class="testimonial-card stagger-child">
                    <div class="t-stars">★★★★★</div>
                    <p class="testimonial-quote">Salething completely replaced my old setup. The instant delivery and clean checkout converted way better than anything I'd tried before. First $10k month within six weeks.</p>
                    <div class="testimonial-author">
                        <div class="avatar" style="background: linear-gradient(135deg,#8b5cf6,#6d28d9)">AJ</div>
                        <div>
                            <div class="author-name">Alex Johnson</div>
                            <div class="author-role">UI Designer & Template Creator</div>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card stagger-child">
                    <div class="t-stars">★★★★★</div>
                    <p class="testimonial-quote">The analytics alone are worth it. I finally understand where my sales actually come from. Switched from Gumroad and never looked back — fees are lower too.</p>
                    <div class="testimonial-author">
                        <div class="avatar" style="background: linear-gradient(135deg,#0ea5e9,#0369a1)">SM</div>
                        <div>
                            <div class="author-name">Shreya Mehta</div>
                            <div class="author-role">Indie SaaS Developer</div>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card stagger-child">
                    <div class="t-stars">★★★★★</div>
                    <p class="testimonial-quote">I launched my Notion template pack on a Tuesday, hit the featured section by Friday, and made $4,200 in the first two weeks. The discovery is genuinely powerful.</p>
                    <div class="testimonial-author">
                        <div class="avatar" style="background: linear-gradient(135deg,#10b981,#065f46)">MO</div>
                        <div>
                            <div class="author-name">Marcus Okafor</div>
                            <div class="author-role">Productivity Coach & Creator</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA BAND -->
    <div class="cta-band">
        <div class="section-inner">
            <p class="section-eyebrow">Ready?</p>
            <h2 class="section-title fade-in">Start Selling Today</h2>
            <p class="section-sub fade-in">Join 120,000+ creators who chose Salething to build their digital revenue stream.</p>
            <div class="cta-band-actions fade-in">
                <a href="#" class="btn-primary" tabindex="0">Create Free Account</a>
                <a href="#products" class="btn-ghost" tabindex="0">Explore Products</a>
            </div>
        </div>
    </div>

    <!-- FOOTER -->
    <footer>
        <div class="footer-watermark" aria-hidden="true">Salething</div>
        <div class="footer-inner">
            <div class="footer-top">
                <div class="footer-brand">
                    <div class="brand-logo">Salething</div>
                    <p>The digital marketplace built for creators. Sell smarter, earn more, grow faster.</p>
                    <div class="social-links">
                        <a class="social-link" href="#" aria-label="Twitter">𝕏</a>
                        <a class="social-link" href="#" aria-label="Instagram">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <rect x="2" y="2" width="20" height="20" rx="5" ry="5" />
                                <circle cx="12" cy="12" r="3" />
                                <circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none" />
                            </svg>
                        </a>
                        <a class="social-link" href="#" aria-label="LinkedIn">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2z" />
                                <circle cx="4" cy="4" r="2" />
                            </svg>
                        </a>
                        <a class="social-link" href="#" aria-label="YouTube">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M22.54 6.42a2.78 2.78 0 0 0-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46A2.78 2.78 0 0 0 1.46 6.42 29 29 0 0 0 1 12a29 29 0 0 0 .46 5.58 2.78 2.78 0 0 0 1.95 1.96C5.12 20 12 20 12 20s6.88 0 8.59-.46a2.78 2.78 0 0 0 1.96-1.96A29 29 0 0 0 23 12a29 29 0 0 0-.46-5.58z" />
                                <polygon points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02" fill="currentColor" />
                            </svg>
                        </a>
                    </div>
                </div>
                <div class="footer-col">
                    <h4>Marketplace</h4>
                    <ul>
                        <li><a href="#" tabindex="0">Browse All</a></li>
                        <li><a href="#" tabindex="0">Templates</a></li>
                        <li><a href="#" tabindex="0">Software & Apps</a></li>
                        <li><a href="#" tabindex="0">Online Courses</a></li>
                        <li><a href="#" tabindex="0">Design Assets</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Creators</h4>
                    <ul>
                        <li><a href="#" tabindex="0">Start Selling</a></li>
                        <li><a href="#" tabindex="0">Creator Dashboard</a></li>
                        <li><a href="#" tabindex="0">Pricing & Fees</a></li>
                        <li><a href="#" tabindex="0">Affiliate Program</a></li>
                        <li><a href="#" tabindex="0">Creator Blog</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Company</h4>
                    <ul>
                        <li><a href="#" tabindex="0">About Us</a></li>
                        <li><a href="#" tabindex="0">Careers</a></li>
                        <li><a href="#" tabindex="0">Press Kit</a></li>
                        <li><a href="#" tabindex="0">Contact</a></li>
                        <li><a href="#" tabindex="0">Status</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p class="footer-copy">© 2025 Salething. All rights reserved.</p>
                <div class="footer-bottom-links">
                    <a href="#" tabindex="0">Privacy Policy</a>
                    <a href="#" tabindex="0">Terms of Service</a>
                    <a href="#" tabindex="0">Cookies</a>
                </div>
            </div>
        </div>
    </footer>

    <script>
    document.addEventListener('DOMContentLoaded', () => {
        
        // ─── THEME TOGGLE ───
        const themeToggle = document.getElementById('themeToggle');
        themeToggle.addEventListener('click', () => {
            document.documentElement.classList.toggle('light');
            const isLight = document.documentElement.classList.contains('light');
            localStorage.setItem('theme', isLight ? 'light' : 'dark');
            themeToggle.innerHTML = isLight ? '🌙' : '☀️';
        });
        themeToggle.innerHTML = document.documentElement.classList.contains('light') ? '🌙' : '☀️';

        // ─── HERO CANVAS ANIMATION ───
        const canvas = document.getElementById('heroCanvas');
        const ctx = canvas.getContext('2d');
        let particles = [];
        let reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

        function initCanvas() {
            canvas.width = canvas.parentElement.offsetWidth;
            canvas.height = canvas.parentElement.offsetHeight;
            particles = [];
            const count = window.innerWidth > 768 ? 90 : 40;
            for (let i = 0; i < count; i++) {
                particles.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    vx: (Math.random() - 0.5) * 0.5,
                    vy: (Math.random() - 0.5) * 0.5,
                    radius: Math.random() * 0.5 + 1.5,
                    opacity: Math.random() * 0.3 + 0.3
                });
            }
        }

        function animateParticles() {
            if (reducedMotion) return;
            requestAnimationFrame(animateParticles);
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            for (let i = 0; i < particles.length; i++) {
                let p = particles[i];
                p.x += p.vx;
                p.y += p.vy;
                if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
                if (p.y < 0 || p.y > canvas.height) p.vy *= -1;
                
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(255, 255, 255, ${p.opacity})`;
                ctx.fill();
                
                for (let j = i + 1; j < particles.length; j++) {
                    let p2 = particles[j];
                    let dx = p.x - p2.x;
                    let dy = p.y - p2.y;
                    let dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 120) {
                        ctx.beginPath();
                        ctx.moveTo(p.x, p.y);
                        ctx.lineTo(p2.x, p2.y);
                        ctx.strokeStyle = `rgba(139, 92, 246, ${0.15 * (1 - dist / 120)})`;
                        ctx.lineWidth = 1;
                        ctx.stroke();
                    }
                }
            }
        }
        window.addEventListener('resize', initCanvas);
        window.matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change', e => {
            reducedMotion = e.matches;
            if (!reducedMotion) animateParticles();
        });
        initCanvas();
        if (!reducedMotion) animateParticles();

        // ─── PRODUCT DATA ───
        const products = [
            { id: 0, name: "Nova UI Kit", cat: "Templates", desc: "300+ components for Figma & Framer. Dark and light variants included.", price: "$49.00", stars: 5, reviews: 312, emoji: "🎨", bg: "linear-gradient(135deg,#1a0a2e,#2d1052)", isNew: true },
            { id: 1, name: "LaunchFlow SaaS Template", cat: "Templates", desc: "Complete Next.js SaaS boilerplate with auth, billing & dashboard.", price: "$89.00", stars: 5, reviews: 178, emoji: "🚀", bg: "linear-gradient(135deg,#0a1628,#1a3050)" },
            { id: 2, name: "PromptVault Pro", cat: "Software", desc: "AI prompt library manager with tagging, search, and export tools.", price: "$29.00", stars: 4, reviews: 554, emoji: "🤖", bg: "linear-gradient(135deg,#0d1a0a,#163020)", isNew: true },
            { id: 3, name: "Mastering Dark UI", cat: "Courses", desc: "6-hour video course on designing beautiful dark-mode interfaces.", price: "$129.00", stars: 5, reviews: 91, emoji: "🎓", bg: "linear-gradient(135deg,#1a1400,#302400)" },
            { id: 4, name: "IconForge Bundle", cat: "Assets", desc: "2,400 premium outline icons in SVG, PNG, and Figma format.", price: "$19.00", stars: 5, reviews: 820, emoji: "✨", bg: "linear-gradient(135deg,#1a001a,#2d0045)" },
            { id: 5, name: "ResumeAI Template Pack", cat: "Templates", desc: "10 ATS-optimized resume templates in Word, PDF and Notion.", price: "$24.00", stars: 4, reviews: 1243, emoji: "📄", bg: "linear-gradient(135deg,#001a1a,#003333)" },
            { id: 6, name: "MicroSaaS Masterclass", cat: "Courses", desc: "Build and launch a profitable solo software product in 30 days.", price: "$199.00", stars: 5, reviews: 67, emoji: "💡", bg: "linear-gradient(135deg,#1a0a00,#301a00)", isNew: true },
            { id: 7, name: "MotionKit After Effects", cat: "Assets", desc: "80 high-quality motion presets and transitions for video editors.", price: "$59.00", stars: 4, reviews: 289, emoji: "🎬", bg: "linear-gradient(135deg,#0a001a,#1a0030)" },
        ];

        function renderStars(n) { return '★'.repeat(n) + '☆'.repeat(5 - n); }

        const grid = document.getElementById('productGrid');
        
        function renderProducts(items) {
            grid.innerHTML = '';
            let emptyState = document.getElementById('emptyState');
            if (emptyState) emptyState.remove();

            if (items.length === 0) {
                emptyState = document.createElement('div');
                emptyState.id = 'emptyState';
                emptyState.style.gridColumn = '1/-1';
                emptyState.style.textAlign = 'center';
                emptyState.style.padding = '4rem 0';
                emptyState.innerHTML = `<div style="font-size: 3rem; color: var(--muted); margin-bottom: 1rem;">👻</div><p>No products match your search.</p>`;
                grid.appendChild(emptyState);
                return;
            }

            items.forEach((p) => {
                const card = document.createElement('div');
                card.className = 'product-card stagger-child';
                card.dataset.id = p.id;
                card.tabIndex = 0;
                card.innerHTML = `
                    <div class="compare-checkbox-container">
                        <input type="checkbox" class="compare-checkbox" aria-label="Compare ${p.name}" data-id="${p.id}" tabindex="0">
                    </div>
                    ${p.isNew ? '<span class="badge-new">New</span>' : ''}
                    <div class="product-thumb-placeholder lazy-bg" data-bg="${p.bg}">
                        <span>${p.emoji}</span>
                        <button class="quick-view-btn" data-id="${p.id}" tabindex="0">Quick View</button>
                    </div>
                    <div class="product-body">
                        <span class="product-tag">${p.cat}</span>
                        <h3 class="product-name">${p.name}</h3>
                        <p class="product-desc">${p.desc}</p>
                        <div class="product-footer">
                            <div>
                                <span class="stars">${renderStars(p.stars)}</span>
                                <span class="rating-count">(${p.reviews})</span>
                            </div>
                            <span class="product-price">${p.price}</span>
                        </div>
                        <button class="add-cart" data-id="${p.id}" tabindex="0">Add to Cart</button>
                    </div>
                `;
                grid.appendChild(card);
            });

            document.querySelectorAll('.lazy-bg').forEach(el => observer.observe(el));
            const staggerGrid = document.getElementById('productGrid');
            observer.observe(staggerGrid);
        }

        // ─── INTERSECTION OBSERVER ───
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(e => {
                if (e.isIntersecting) {
                    if (e.target.classList.contains('lazy-bg')) {
                        e.target.style.background = e.target.dataset.bg;
                        e.target.classList.remove('lazy-bg');
                        observer.unobserve(e.target);
                    } else if (e.target.classList.contains('stagger-grid')) {
                        const children = e.target.querySelectorAll('.stagger-child:not(.visible)');
                        children.forEach((child, i) => {
                            child.style.transitionDelay = `${i * 80}ms`;
                            child.classList.add('visible');
                        });
                        observer.unobserve(e.target);
                    } else if (e.target.classList.contains('stat-num')) {
                        startCountUp(e.target);
                        observer.unobserve(e.target);
                    } else {
                        e.target.classList.add('visible');
                        observer.unobserve(e.target);
                    }
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

        document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
        document.querySelectorAll('.stagger-grid').forEach(el => observer.observe(el));
        document.querySelectorAll('.stat-num').forEach(el => observer.observe(el));

        renderProducts(products);

        // ─── COUNT UP ───
        function startCountUp(el) {
            const targetStr = el.dataset.target || el.innerText.replace(/[^0-9.]/g, '');
            const target = parseFloat(targetStr);
            const duration = 1500;
            const start = performance.now();
            const suffix = el.dataset.suffix || '';
            const prefix = el.dataset.prefix || '';
            
            function easeOutExpo(x) { return x === 1 ? 1 : 1 - Math.pow(2, -10 * x); }
            
            function update(time) {
                let progress = (time - start) / duration;
                if (progress > 1) progress = 1;
                const val = target * easeOutExpo(progress);
                let displayVal = Math.floor(val);
                if (targetStr.includes('.')) displayVal = val.toFixed(1);
                
                el.innerText = prefix + displayVal + suffix;
                if (progress < 1) requestAnimationFrame(update);
                else el.innerText = prefix + target + suffix;
            }
            requestAnimationFrame(update);
        }

        // ─── CART DRAWER & ADD TO CART ───
        let cart = [];
        const cartDrawer = document.getElementById('cartDrawer');
        const cartBadge = document.getElementById('cartBadge');
        
        document.getElementById('cartToggle').addEventListener('click', () => {
            cartDrawer.classList.add('open');
            document.body.style.overflow = 'hidden';
        });
        document.getElementById('closeCartBtn').addEventListener('click', () => {
            cartDrawer.classList.remove('open');
            document.body.style.overflow = '';
        });

        function updateCartUI() {
            const count = cart.reduce((acc, item) => acc + item.qty, 0);
            cartBadge.innerText = count;
            
            const list = document.getElementById('cartItemsList');
            list.innerHTML = '';
            let subtotal = 0;
            
            cart.forEach((item, index) => {
                const price = parseFloat(item.price.replace('$', ''));
                subtotal += price * item.qty;
                list.innerHTML += `
                    <div class="cart-item">
                        <div class="cart-item-info">
                            <h4>${item.name}</h4>
                            <p>${item.price}</p>
                        </div>
                        <div class="cart-item-controls">
                            <button class="cart-btn" onclick="window.updateQty(${index}, -1)" aria-label="Decrease quantity" tabindex="0">−</button>
                            <span>${item.qty}</span>
                            <button class="cart-btn" onclick="window.updateQty(${index}, 1)" aria-label="Increase quantity" tabindex="0">+</button>
                            <button class="cart-btn" onclick="window.removeCartItem(${index})" aria-label="Remove item" tabindex="0" style="background:transparent;border-color:transparent">🗑</button>
                        </div>
                    </div>
                `;
            });
            document.getElementById('cartSubtotal').innerText = `$${subtotal.toFixed(2)}`;
        }

        window.updateQty = (index, delta) => {
            cart[index].qty += delta;
            if (cart[index].qty <= 0) cart.splice(index, 1);
            updateCartUI();
        };
        window.removeCartItem = (index) => {
            cart.splice(index, 1);
            updateCartUI();
        };

        // ─── LIVE SEARCH ───
        const searchInput = document.getElementById('searchInput');
        const searchToggle = document.getElementById('searchToggle');
        const searchClear = document.getElementById('searchClear');

        searchToggle.addEventListener('click', () => {
            searchInput.classList.toggle('active');
            if (searchInput.classList.contains('active')) searchInput.focus();
        });

        let searchTimeout;
        searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                const q = e.target.value.toLowerCase();
                searchClear.style.display = q ? 'block' : 'none';
                
                const filtered = products.filter(p => 
                    p.name.toLowerCase().includes(q) || p.desc.toLowerCase().includes(q)
                );
                
                let emptyState = document.getElementById('emptyState');
                if (filtered.length === 0) {
                    if (!emptyState) {
                        emptyState = document.createElement('div');
                        emptyState.id = 'emptyState';
                        emptyState.style.gridColumn = '1/-1';
                        emptyState.style.textAlign = 'center';
                        emptyState.style.padding = '4rem 0';
                        emptyState.innerHTML = `<div style="font-size: 3rem; color: var(--muted); margin-bottom: 1rem;">👻</div><p>No products match your search.</p>`;
                        grid.appendChild(emptyState);
                    }
                    emptyState.style.display = 'block';
                } else {
                    if (emptyState) emptyState.style.display = 'none';
                }

                document.querySelectorAll('.product-card').forEach(card => {
                    const id = parseInt(card.dataset.id);
                    const p = products.find(prod => prod.id === id);
                    const match = p.name.toLowerCase().includes(q) || p.desc.toLowerCase().includes(q);
                    if (match) {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                        card.style.display = '';
                    } else {
                        card.style.opacity = '0';
                        card.style.transform = 'scale(0.95)';
                        setTimeout(() => { if(card.style.opacity === '0') card.style.display = 'none'; }, 200);
                    }
                });
            }, 150);
        });

        searchClear.addEventListener('click', () => {
            searchInput.value = '';
            searchInput.dispatchEvent(new Event('input'));
            searchInput.classList.remove('active');
            searchClear.style.display = 'none';
        });

        // ─── COMPARE BAR ───
        let compareItems = [];
        const compareBar = document.getElementById('compareBar');
        
        function updateCompareBar() {
            const itemsContainer = document.getElementById('compareItems');
            if (compareItems.length >= 2) {
                compareBar.classList.add('visible');
                itemsContainer.innerHTML = compareItems.map(id => {
                    const p = products.find(prod => prod.id === parseInt(id));
                    return `<div class="compare-pill">${p.name}</div>`;
                }).join('');
            } else {
                compareBar.classList.remove('visible');
            }
        }

        document.getElementById('compareNowBtn').addEventListener('click', () => {
            const modalOverlay = document.getElementById('compareModalOverlay');
            const tableContainer = document.getElementById('compareTableContainer');
            
            let html = `<table class="compare-table">
                <tr>
                    <th>Product</th>
                    ${compareItems.map(id => `<td><strong>${products.find(prod => prod.id == id).name}</strong></td>`).join('')}
                </tr>
                <tr>
                    <th>Category</th>
                    ${compareItems.map(id => `<td>${products.find(prod => prod.id == id).cat}</td>`).join('')}
                </tr>
                <tr>
                    <th>Price</th>
                    ${compareItems.map(id => `<td>${products.find(prod => prod.id == id).price}</td>`).join('')}
                </tr>
                <tr>
                    <th>Rating</th>
                    ${compareItems.map(id => `<td>${products.find(prod => prod.id == id).stars} ★ (${products.find(prod => prod.id == id).reviews})</td>`).join('')}
                </tr>
                <tr>
                    <th>Features</th>
                    ${compareItems.map(id => `<td><ul style="padding-left:1rem;margin:0;font-size:0.85rem">
                        <li>High Quality</li><li>Instant Access</li><li>Support Included</li>
                    </ul></td>`).join('')}
                </tr>
            </table>`;
            
            tableContainer.innerHTML = html;
            modalOverlay.classList.add('active');
        });

        document.getElementById('closeCompareModal').addEventListener('click', () => {
            document.getElementById('compareModalOverlay').classList.remove('active');
        });

        // ─── EVENT DELEGATION ───
        document.addEventListener('change', e => {
            if (e.target.classList.contains('compare-checkbox')) {
                const id = parseInt(e.target.dataset.id);
                if (e.target.checked) {
                    if (compareItems.length >= 3) {
                        const oldest = compareItems.shift();
                        const cb = document.querySelector(`.compare-checkbox[data-id="${oldest}"]`);
                        if(cb) cb.checked = false;
                    }
                    compareItems.push(id);
                } else {
                    compareItems = compareItems.filter(item => item !== id);
                }
                updateCompareBar();
            }
        });

        document.addEventListener('click', e => {
            // Add to Cart Logic
            if (e.target.classList.contains('add-cart') || e.target.id === 'qvAddToCart') {
                const id = parseInt(e.target.dataset.id);
                const p = products.find(prod => prod.id === id);
                
                const existing = cart.find(item => item.id === p.id);
                if (existing) existing.qty++;
                else cart.push({ ...p, qty: 1 });
                updateCartUI();
                
                // Flying emoji
                if (!reducedMotion && e.target.classList.contains('add-cart')) {
                    const btn = e.target;
                    const card = btn.closest('.product-card');
                    const emojiEl = card.querySelector('.product-thumb-placeholder span');
                    const rect = emojiEl.getBoundingClientRect();
                    
                    const cartIcon = document.querySelector('.cart-toggle');
                    const cartRect = cartIcon.getBoundingClientRect();
                    
                    const clone = document.createElement('div');
                    clone.innerText = p.emoji;
                    clone.className = 'flying-emoji';
                    clone.style.left = rect.left + 'px';
                    clone.style.top = rect.top + 'px';
                    
                    const tx = cartRect.left - rect.left;
                    const ty = cartRect.top - rect.top;
                    
                    clone.style.setProperty('--tx', `${tx}px`);
                    clone.style.setProperty('--ty', `${ty}px`);
                    clone.style.animation = 'flyToCart 0.6s cubic-bezier(0.25, 1, 0.5, 1) forwards';
                    
                    document.body.appendChild(clone);
                    setTimeout(() => clone.remove(), 600);
                }
            }

            // Quick View Logic
            if (e.target.classList.contains('quick-view-btn')) {
                const id = parseInt(e.target.dataset.id);
                const p = products.find(prod => prod.id === id);
                
                document.getElementById('qvEmoji').innerText = p.emoji;
                document.getElementById('qvEmojiContainer').style.background = p.bg;
                document.getElementById('qvName').innerText = p.name;
                document.getElementById('qvCat').innerText = p.cat;
                document.getElementById('qvDesc').innerText = p.desc + " This product includes top-tier assets tailored for professionals. Instantly downloadable and fully customizable. Upgrade your workflow today.";
                document.getElementById('qvPrice').innerText = p.price;
                document.getElementById('qvStars').innerHTML = renderStars(p.stars) + ` <span style="font-size:0.8rem;color:var(--muted)">(${p.reviews} reviews)</span>`;
                document.getElementById('qvAddToCart').dataset.id = p.id;
                
                document.getElementById('quickViewModalOverlay').classList.add('active');
            }
        });

        document.getElementById('closeQvModal').addEventListener('click', () => {
            document.getElementById('quickViewModalOverlay').classList.remove('active');
        });

        // ─── ESCAPE TO CLOSE ───
        document.addEventListener('keydown', e => {
            if (e.key === 'Escape') {
                document.getElementById('compareModalOverlay').classList.remove('active');
                document.getElementById('quickViewModalOverlay').classList.remove('active');
                cartDrawer.classList.remove('open');
                document.body.style.overflow = '';
            }
        });

        // ─── FILTER TABS ───
        document.querySelectorAll('.filter-tab').forEach(tab => {
            tab.addEventListener('click', function () {
                document.querySelectorAll('.filter-tab').forEach(t => t.classList.remove('active'));
                this.classList.add('active');
                const cat = this.textContent.trim();
                
                document.querySelectorAll('.product-card').forEach(card => {
                    const id = parseInt(card.dataset.id);
                    const p = products.find(prod => prod.id === id);
                    const show = cat === 'All' || p.cat === cat;
                    if(show) {
                        card.style.display = '';
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    } else {
                        card.style.display = 'none';
                        card.style.opacity = '0';
                        card.style.transform = 'scale(0.95)';
                    }
                });
            });
        });

        // ─── NAVBAR SCROLL ───
        const navbar = document.getElementById('navbar');
        window.addEventListener('scroll', () => {
            navbar.classList.toggle('scrolled', window.scrollY > 50);
        });

        // ─── HAMBURGER ───
        const hamburger = document.getElementById('hamburger');
        const navLinks = document.getElementById('navLinks');
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('open');
        });
        navLinks.querySelectorAll('a').forEach(a => {
            a.addEventListener('click', () => navLinks.classList.remove('open'));
        });

        // ─── VIDEO PLAY ───
        const playBtn = document.getElementById('playBtn');
        const placeholder = document.getElementById('videoPlaceholder');
        const video = document.getElementById('heroVideo');
        function startVideo() {
            placeholder.style.display = 'none';
            video.style.display = 'block';
            video.play().catch(() => {});
        }
        playBtn.addEventListener('click', startVideo);
        document.getElementById('watchDemo').addEventListener('click', () => {
            document.getElementById('videoCard').scrollIntoView({ behavior: 'smooth', block: 'center' });
            setTimeout(startVideo, 600);
        });
    });
    </script>
</body>
</html>
"""

with open("/home/aayush/Downloads/Salething/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html successfully.")
