const title = [
   "You need to take rest",
   "You can do better",
   "You have done well!",
];

const res = [
  "Result: Not fit to exercise currently",
  "Result: Average Mobility",
  "Result: Good Mobility",
];

const color = ["danger", "warning", ""];

const buttons = [
  '<button class="button" data-level="danger" startDrive>Proceed</button>',
  '<button class="button" data-level="warning">Proceed</button><button class="button" data-level="muted" startDrive>Go Back</button>',
  '<button class="button" data-level="" startDrive>Proceed</button>',
];

const maxNormal = 0;
const maxWarning = 1;

const currentValue = parseInt(
  document.body.querySelector(".score-container .score").innerHTML
);

const index = currentValue < maxNormal ? 0 : currentValue < maxWarning ? 1 : 2;

const result = document.querySelector(".result-container");
const scoreContainer = result.querySelector(".score-container");
const resultText = result.querySelector(".result-text");
const resultTitle = resultText.querySelector(".result");
const resText = resultText.querySelector("h4");
const resultActions = resultText.querySelector(".result-actions");

// var tl = gsap.timeline();

// gsap.to(".result-container", { ease: "power2.out", opacity: 1, duration: 1.5 });

scoreContainer.setAttribute("data-level", color[index]);
resText.innerText = res[index];
resultTitle.innerText = title[index];
resultActions.innerHTML = buttons[index];

const tl = gsap.timeline();

tl.to(scoreContainer, {
  ease: "power2.out",
  opacity: 1,
  duration: 0.5,
})
  .to(resText, {
    ease: "power2.out",
    opacity: 0.5,
    duration: 0.5,
  })
  .to(resultTitle, {
    ease: "power2.out",
    opacity: 1,
    duration: 0.5,
  })
  .to(resultActions, {
    ease: "power2.out",
    opacity: 1,
    duration: 0.5,
  });

const start = document.querySelector(".button[startDrive]");
start.addEventListener("mousedown", () => {
  gsap.to(result, { ease: "power2.in", opacity: 0, duration: 0.75 });
  setTimeout(() => {
    window.location.replace("/driving");
  }, 500);
});