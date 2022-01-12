const currentLocation = window.location;
const width = window.screen.width;
let item;
let link;
let icon;
let arrow;

if (currentLocation.toString().includes("familias")) {
  item = document.querySelector("#familias-item");
  link = document.querySelector("#familias-link");
  icon = document.querySelector("#familias-icon");
  arrow = document.querySelector("#familias-arrow-icon");

  if (width > 1000) {
    arrow.classList.remove("icon-inactive");
    arrow.classList.add("icon-active");
  }

  item.classList.add("nav-item-active");
  link.classList.add("nav-link-active");
  icon.classList.add("icon-active");
} else if (currentLocation.toString().includes("doacoes")) {
  item = document.querySelector("#doacoes-item");
  link = document.querySelector("#doacoes-link");
  icon = document.querySelector("#doacoes-icon");
  arrow = document.querySelector("#doacoes-arrow-icon");

  if (width > 1000) {
    arrow.classList.remove("icon-inactive");
    arrow.classList.add("icon-active");
  }

  item.classList.add("nav-item-active");
  link.classList.add("nav-link-active");
  icon.classList.add("icon-active");
} else if (currentLocation.toString().includes("entidades")) {
  item = document.querySelector("#entidades-item");
  link = document.querySelector("#entidades-link");
  icon = document.querySelector("#entidades-icon");
  arrow = document.querySelector("#entidades-arrow-icon");

  if (width > 1000) {
    arrow.classList.remove("icon-inactive");
    arrow.classList.add("icon-active");
  }

  item.classList.add("nav-item-active");
  link.classList.add("nav-link-active");
  icon.classList.add("icon-active");
} else if (currentLocation.toString().includes("usuario")) {
  item = document.querySelector("#usuario-item");
  link = document.querySelector("#usuario-link");
  icon = document.querySelector("#usuario-icon");
  arrow = document.querySelector("#usuario-arrow-icon");

  if (width > 1000) {
    arrow.classList.remove("icon-inactive");
    arrow.classList.add("icon-active");
  }

  item.classList.add("nav-item-active");
  link.classList.add("nav-link-active");
  icon.classList.add("icon-active");
} else {
  item = document.querySelector("#dashboard-item");
  link = document.querySelector("#dashboard-link");
  icon = document.querySelector("#dashboard-icon");
  arrow = document.querySelector("#dashboard-arrow-icon");

  if (width > 1000) {
    arrow.classList.remove("icon-inactive");
    arrow.classList.add("icon-active");
  }

  item.classList.add("nav-item-active");
  link.classList.add("nav-link-active");
  icon.classList.add("icon-active");
}
