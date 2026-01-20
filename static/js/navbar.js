document.addEventListener("DOMContentLoaded", () => {
  const btn = document.querySelector(".nav-toggle");
  const menu = document.querySelector("#navMenu");
  if (!btn || !menu) return;

  btn.addEventListener("click", () => {
    const isOpen = menu.classList.toggle("open");
    btn.setAttribute("aria-expanded", isOpen ? "true" : "false");
  });

  // close menu when clicking a link (mobile)
  menu.querySelectorAll("a").forEach((a) => {
    a.addEventListener("click", () => {
      if (menu.classList.contains("open")) {
        menu.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
      }
    });
  });
});
