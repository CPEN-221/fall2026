(() => {
  const progress = document.querySelector(".reading-progress span");
  const railLinks = [...document.querySelectorAll(".section-rail a")];
  const sections = railLinks
    .map((link) => document.querySelector(link.hash))
    .filter(Boolean);

  const update = () => {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const ratio = scrollable > 0 ? window.scrollY / scrollable : 0;
    if (progress) {
      progress.style.width = String(Math.min(100, Math.max(0, ratio * 100))) + "%";
    }

    let current = sections[0];
    for (const section of sections) {
      if (section.getBoundingClientRect().top <= 130) current = section;
    }

    for (const link of railLinks) {
      if (current && link.hash === "#" + current.id) {
        link.setAttribute("aria-current", "location");
      } else {
        link.removeAttribute("aria-current");
      }
    }
  };

  update();
  window.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
})();

