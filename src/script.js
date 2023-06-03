function toggleDarkMode() {
  const body = document.body;
  body.classList.toggle("body-dark-mode");
  document.querySelectorAll("*").forEach((El) => {
    const elements = ["P", "H3", "H1", "INPUT", "LABEL"];
    if (elements.includes(El.nodeName)) {
      El.classList.toggle("dark");
    }
  });
  const btnEl = document.querySelector("button");
  btnEl.classList.toggle("dark-btn");
  document.querySelector(".dark-btn")
    ? (btnEl.textContent = "SWITCH TO LIGHT MODE")
    : (btnEl.textContent = "SWITCH TO DARK MODE");
}
