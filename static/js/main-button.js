const mainContainer = document.body.querySelector(".hero");
const contentContainers = document.body.querySelectorAll(".container.content");
const button = document.body.querySelector(".next--button");
const accident = mainContainer.querySelector(".accident");
const nametitle = document.body.querySelector(".next--title");
const titleContainer = document.body.querySelector(".title-container");
const title = document.body.querySelector(".title-container .title");
const tagline = document.body.querySelector(".title-container .tagline");

var t = true;

var tl = gsap.timeline();

tl.to(accident, {
  opacity: 1,
  duration: 0.75,
  ease: "power2.in",
})
  .to(nametitle, {
    opacity: 1,
    scrollTrigger: nametitle,
    duration: 0.25,
    ease: "power2.in",
  })
  .to(button, {
    opacity: 1,
    scrollTrigger: button,
    duration: 0.25,
    ease: "power2.in",
  });

contentContainers.forEach((content) =>
  gsap.to(content, {
    opacity: 1,
    scrollTrigger: content,
    duration: 0.25,
    ease: "power2.in",
  })
);

button.addEventListener("mousedown", () => {
  if (t) {
    tl.to(".accident", {
      opacity: 0,
      duration: 0.3,
      yPercent: 10,
      ease: "power2.out",
    }).to(".next--title", {
      opacity: 0,
      duration: 0.2,
      yPercent: 10,
      ease: "power2.out",
    });
    contentContainers.forEach((content) =>
      gsap.to(content, {
        opacity: 0,
        duration: 0.2,
        yPercent: 10,
        ease: "power2.out",
      })
    );
    setTimeout(() => {
      mainContainer.removeChild(accident);
      contentContainers.forEach((c) => document.body.removeChild(c));
      nametitle.classList.add("noDisplay");
      titleContainer.classList.remove("noDisplay");
      tl.to(".title-container .title", {
        opacity: 1,
        duration: 0.3,
        yPercent: -5,
        ease: "power2.in",
      }).to(".title-container .tagline", {
        opacity: 1,
        duration: 0.3,
        yPercent: -5,
        ease: "power2.in",
      });
      includeHTML();
    }, 600);
    t = false;
  } else {
    tl.to(".title-container", {
      opacity: 0,
      duration: 0.3,
      yPercent: 10,
      ease: "power2.out",
    }).to(button, { opacity: 0, duration: 0.3, ease: "power2.out" });
    setTimeout(() => {
      window.location.replace("/loginPage");
    }, 600);
  }
});