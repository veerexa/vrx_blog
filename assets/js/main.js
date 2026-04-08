/* Veerexa School Blog - Main JS (minimal, fast) */
(function () {
  'use strict';

  /* --- Mobile Nav Toggle --- */
  const toggle = document.getElementById('nav-toggle');
  const navLinks = document.getElementById('nav-links');
  if (toggle && navLinks) {
    toggle.addEventListener('click', () => {
      navLinks.classList.toggle('open');
      const expanded = navLinks.classList.contains('open');
      toggle.setAttribute('aria-expanded', expanded);
    });
    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!toggle.contains(e.target) && !navLinks.contains(e.target)) {
        navLinks.classList.remove('open');
      }
    });
  }

  /* --- Active nav link highlight --- */
  const path = window.location.pathname;
  document.querySelectorAll('.nav-links a').forEach((a) => {
    if (a.getAttribute('href') === path || (path.startsWith('/blog') && a.getAttribute('href') === '/blog/')) {
      a.classList.add('active');
    }
  });

  /* --- Lazy-load images --- */
  if ('IntersectionObserver' in window) {
    const images = document.querySelectorAll('img[data-src]');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          observer.unobserve(img);
        }
      });
    }, { rootMargin: '200px 0px' });
    images.forEach((img) => observer.observe(img));
  }

  /* --- Smooth scroll for anchor links --- */
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* --- Reading progress bar (articles) --- */
  const progressBar = document.getElementById('reading-progress');
  if (progressBar) {
    window.addEventListener('scroll', () => {
      const doc = document.documentElement;
      const scrollTop = doc.scrollTop || document.body.scrollTop;
      const scrollHeight = doc.scrollHeight - doc.clientHeight;
      const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
      progressBar.style.width = progress + '%';
    }, { passive: true });
  }

  /* --- Animate elements on scroll --- */
  if ('IntersectionObserver' in window) {
    const animEls = document.querySelectorAll('.blog-card, .feature-card, .stat-item');
    const animObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          animObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    animEls.forEach((el) => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      animObserver.observe(el);
    });
  }

  /* --- Theme Toggle --- */
  const themeToggle = document.getElementById('theme-toggle');
  const currentTheme = localStorage.getItem('theme') || 'dark';
  
  if (currentTheme === 'light') {
    document.documentElement.setAttribute('data-theme', 'light');
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      let theme = document.documentElement.getAttribute('data-theme');
      if (theme === 'light') {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'dark');
      } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
      }
    });
  }
  /* --- MOSDAC RSS Feed Fetcher --- */
  const alertsContainer = document.getElementById('mosdac-alerts-container');
  if (alertsContainer) {
    // We use allorigins as a CORS proxy since MOSDAC feed might not allow direct cross-origin access
    const rssUrl = 'https://www.mosdac.gov.in/rss.xml';
    const proxyUrl = `https://api.allorigins.win/get?url=${encodeURIComponent(rssUrl)}`;

    fetch(proxyUrl)
      .then(response => {
        if (response.ok) return response.json();
        throw new Error('Network response was not ok.');
      })
      .then(data => {
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(data.contents, "text/xml");
        const items = xmlDoc.querySelectorAll("item");
        
        // Clear skeleton loading
        alertsContainer.innerHTML = '';

        if (items.length === 0) {
          alertsContainer.innerHTML = '<p class="text-sm text-slate-500">No active alerts right now.</p>';
          return;
        }

        // Render up to 5 alerts
        const alertsToRender = Array.from(items).slice(0, 5);
        
        alertsToRender.forEach(item => {
          const title = item.querySelector("title")?.textContent || "Alert";
          const link = item.querySelector("link")?.textContent || "#";
          const description = item.querySelector("description")?.textContent || "";
          
          let alertDate = "";
          const pubDateNode = item.querySelector("pubDate");
          if (pubDateNode) {
            const d = new Date(pubDateNode.textContent);
            alertDate = isNaN(d) ? pubDateNode.textContent : d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' });
          }

          const alertCard = document.createElement('a');
          alertCard.href = link;
          alertCard.target = "_blank";
          alertCard.rel = "noopener noreferrer";
          alertCard.className = "block bg-white hover:bg-indigo-50/50 p-4 rounded-xl border border-indigo-100 shadow-sm transition-colors group";
          
          alertCard.innerHTML = `
            <div class="flex flex-col gap-1">
              <span class="text-sm font-bold text-slate-800 group-hover:text-indigo-600 transition-colors">${title}</span>
              ${description ? `<p class="text-xs text-slate-500 line-clamp-2">${description}</p>` : ''}
              ${alertDate ? `<span class="text-[10px] text-slate-400 mt-1 font-medium">${alertDate}</span>` : ''}
            </div>
          `;
          
          alertsContainer.appendChild(alertCard);
        });
      })
      .catch(error => {
        console.error('Error fetching MOSDAC feed:', error);
        alertsContainer.innerHTML = '<p class="text-sm text-red-400">Unable to load alerts at this time.</p>';
      });
  }

  /* --- Search Modal Logic --- */
  window.openSearchModal = function() {
    const modal = document.getElementById('search-modal');
    if (modal) {
      modal.classList.remove('hidden');
      // small delay to allow display block to apply before animating opacity
      setTimeout(() => {
        modal.classList.remove('opacity-0');
        document.getElementById('search-input')?.focus();
      }, 10);
      document.body.style.overflow = 'hidden';
    }
  };

  window.closeSearchModal = function() {
    const modal = document.getElementById('search-modal');
    if (modal) {
      modal.classList.add('opacity-0');
      setTimeout(() => {
        modal.classList.add('hidden');
      }, 300);
      document.body.style.overflow = '';
      document.getElementById('search-input').value = '';
      document.getElementById('search-results').innerHTML = '';
    }
  };

  // Predefined search index since it's a static site
  const searchIndex = [
    { title: "The Rise of Indian Private Space Tech", url: "/space/indian-private-space-companies.html", desc: "Skyroot, Agnikul, Pixxel, Bellatrix" },
    { title: "India's Lunar Missions", url: "/space/moon-missions.html", desc: "Chandrayaan missions overview" },
    { title: "Mangalyaan & Mars", url: "/space/mars-missions.html", desc: "India's Mars Orbiter Mission deep dive" },
    { title: "LLM Models Guide", url: "/tech/llm-models-guide.html", desc: "Comprehensive guide to modern AI LLMs" },
    { title: "School ERP Software", url: "/education/how-school-erp-software-helps-schools.html", desc: "How school ERPs boost productivity" },
    { title: "Medical Careers Guide", url: "/education/career-lab/medical-careers-guide-india.html", desc: "NEET Prep and medical career roadmap" },
    { title: "Join ISRO After 12th", url: "/education/career-lab/science-research-isro-careers.html", desc: "Roadmap to joining ISRO" },
    { title: "Tech Career Roadmap", url: "/education/career-lab/engineering-tech-career-roadmap.html", desc: "Engineering and software development guide" },
    { title: "ROI on Inventory Management", url: "/inventory/roi-inventory-management-software-sme.html", desc: "Supply chain optimization" },
    { title: "Defense Core Index", url: "/defense/index.html", desc: "Defense weaponry and jets" },
    { title: "Launchpad Workspace", url: "/launchpad/index.html", desc: "Free personal website builder" },
    { title: "Skyroot Aerospace", url: "/space/skyroot-aerospace.html", desc: "India's first private launch vehicle" },
    { title: "Agnikul Cosmos", url: "/space/agnikul-cosmos.html", desc: "Agnibaan and 3D printed engines" },
    { title: "Pixxel Space", url: "/space/pixxel-space.html", desc: "Hyperspectral earth imaging" },
    { title: "Bellatrix Aerospace", url: "/space/bellatrix-aerospace.html", desc: "Water-powered in-space thrusters" }
  ];

  window.performSearch = function() {
    const query = document.getElementById('search-input').value.toLowerCase();
    const resultsContainer = document.getElementById('search-results');
    
    if (query.trim() === '') {
      resultsContainer.innerHTML = '';
      return;
    }

    const filtered = searchIndex.filter(item => 
      item.title.toLowerCase().includes(query) || 
      item.desc.toLowerCase().includes(query)
    );

    if (filtered.length === 0) {
      resultsContainer.innerHTML = '<p class="text-white/60 text-center py-8">No results found for "'+ query +'"</p>';
      return;
    }

    resultsContainer.innerHTML = filtered.map(item => `
      <a href="${item.url}" class="block bg-white/5 hover:bg-white/10 p-4 rounded-xl border border-white/10 transition-all group">
        <h4 class="text-lg font-bold text-white group-hover:text-brand-sky transition-colors">${item.title}</h4>
        <p class="text-white/60 text-sm mt-1">${item.desc}</p>
      </a>
    `).join('');
  };

})();
