const graphic = document.getElementById("graphic");

function showFig(src) {
  graphic.innerHTML = `<iframe src="${src}"></iframe>`;
}

// Inicial
showFig("figs/fig1_lead_time.html");

const scroller = scrollama();

scroller
  .setup({
    step: ".step",
    offset: 0.5
  })
  .onStepEnter(response => {
    if (response.index === 0) {
      showFig("figs/fig1_lead_time.html");
    }
    if (response.index === 1) {
      showFig("figs/fig2_adr.html");
    }
    if (response.index === 2) {
      showFig("figs/fig3_combined.html");
    }
  });
