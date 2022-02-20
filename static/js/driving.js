const video = document.body.querySelector(".drive-stream .drive-stream-video");
const toolbar = document.body.querySelector(
  ".drive-stream .drive-stream--toolbar"
);

var tl = gsap.timeline();

tl.to(video, {
  opacity: 1,
  ease: "power2.out",
  duration: 1,
}).to(toolbar, { opacity: 1, ease: "power2.out", duration: 0.5 });
