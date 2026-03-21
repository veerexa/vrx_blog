document.addEventListener('DOMContentLoaded', () => {
    // 1. Intersection Observer for Scroll Animations
    const revealElements = document.querySelectorAll('.fade-up, .step, .feature-card, .apply-card');
    
    // Convert existing fade-up elements to use scroll reveal instead of on-load animation
    revealElements.forEach(el => {
      // If it has fade-up, remove it and add reveal so it triggers on scroll
      if (el.classList.contains('fade-up')) {
        el.classList.remove('fade-up');
        el.classList.add('reveal');
      }
      if (!el.classList.contains('reveal')) {
        el.classList.add('reveal');
      }
    });
  
    const revealOptions = {
      threshold: 0.15,
      rootMargin: "0px 0px -50px 0px"
    };
  
    const revealObserver = new IntersectionObserver(function(entries, observer) {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('active');
        observer.unobserve(entry.target);
      });
    }, revealOptions);
  
    document.querySelectorAll('.reveal').forEach(el => {
      revealObserver.observe(el);
    });
  
    // 2. Hero Glow Follow Mouse Effect
    const hero = document.querySelector('.hero');
    const heroGlow = document.querySelector('.hero-bg-glow');
    
    if(hero && heroGlow) {
      hero.addEventListener('mousemove', (e) => {
        const { clientX, clientY } = e;
        const x = Math.round((clientX / window.innerWidth) * 60 - 30);
        const y = Math.round((clientY / window.innerHeight) * 60 - 30);
        // Translate from center
        heroGlow.style.transform = `translate(calc(-50% + ${x}px), calc(-50% + ${y}px))`;
      });
    }
  
    // 3. Card Mouse Hover Gradient Effect
    const cards = document.querySelectorAll('.glass-card, .apply-card');
    cards.forEach(card => {
      card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);
      });
    });
  
    // 4. FAQ Accordion Logic
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
      item.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        
        // Close all other FAQs
        faqItems.forEach(otherItem => {
          otherItem.classList.remove('active');
        });
        
        // Toggle current FAQ
        if (!isActive) {
          item.classList.add('active');
        }
      });
    });
  });
