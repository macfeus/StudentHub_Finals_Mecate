document.addEventListener("DOMContentLoaded", () => {
  const btn = document.querySelector(".nav-toggle");
  const menu = document.querySelector("#navMenu");
  if (!btn || !menu) return;

  btn.addEventListener("click", () => {
    menu.classList.toggle("open");
    btn.setAttribute("aria-expanded", menu.classList.contains("open") ? "true" : "false");
  });
});
