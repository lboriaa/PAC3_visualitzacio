const graphic = document.getElementById("graphic");

function showFig(src) {
  graphic.innerHTML = `<iframe src="${src}"></iframe>`;
}

// Gràfic inicial
showFig("figs/fig1_lead_time.html");

const scroller = scrollama();

scroller
  .setup({
    step: ".step",
    offset: 0.5
  })
  .onStepEnter(response => {

    // STEP 0
    if (response.index === 0) {
      showFig("figs/fig1_lead_time.html");
    }

    // STEP 1
    if (response.index === 1) {
      if (response.direction === "down") {
        showFig("figs/fig2_adr.html");
      }
      if (response.direction === "up") {
        showFig("figs/fig1_lead_time.html");
      }
    }

    // STEP 2
    if (response.index === 2) {
      if (response.direction === "down") {
        showFig("figs/fig3_combined.html");
      }
      if (response.direction === "up") {
        showFig("figs/fig2_adr.html");
      }
    }
  });
