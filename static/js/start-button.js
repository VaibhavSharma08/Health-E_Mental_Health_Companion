const container = document.body.querySelector(".dizzy-container");
const button = document.body.querySelector(
  ".dizzy-container .details button.button"
);
const toRemoveContainer = document.body.querySelector(".details");
const videoContainer = document.body.querySelector(
  ".dizzy-container .video-container"
);

const cursorOutline = document.body.querySelector(".cursor-dot-outline");
const cursorDot = document.body.querySelector(".cursor-dot");

var tl = gsap.timeline();

tl.to(container, {
  opacity: 1,
  duration: 0.75,
  ease: "power2.in",
});

button.addEventListener("mousedown", () => {
  tl.to(toRemoveContainer, {
    duration: 0.3,
    opacity: 0,
    css: {
      display: "none",
    },
  }).to(videoContainer, {
    duration: 0.6,
    scale: 1.5,
  });

  // force show result
  setTimeout(() => {
    window.location.replace("/dizzy-result");
  }, 15000);
});
