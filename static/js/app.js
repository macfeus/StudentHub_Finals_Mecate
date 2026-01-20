document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".nav-toggle");
  const menu = document.getElementById("navMenu");

  if (!toggle || !menu) return;

  const closeMenu = () => {
    menu.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
  };

  const openMenu = () => {
    menu.classList.add("is-open");
    toggle.setAttribute("aria-expanded", "true");
  };

  toggle.addEventListener("click", (e) => {
    e.stopPropagation();
    const isOpen = menu.classList.contains("is-open");
    isOpen ? closeMenu() : openMenu();
  });

  // Close when clicking outside
  document.addEventListener("click", (e) => {
    if (!menu.contains(e.target) && !toggle.contains(e.target)) {
      closeMenu();
    }
  });

  // Close after clicking a link (mobile-friendly)
  menu.addEventListener("click", (e) => {
    const link = e.target.closest("a");
    if (link) closeMenu();
  });

  // Reset on resize (avoid stuck menu)
  window.addEventListener("resize", () => {
    if (window.innerWidth > 768) closeMenu();
  });
});
