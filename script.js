const graphic = document.getElementById("graphic");

function showFig(src) {
  graphic.innerHTML = `<iframe src="${src}"></iframe>`;
}

// Gràfic inicial
showFig("fig1_lead_time.html");

const scroller = scrollama();

scroller
  .setup({
    step: ".step",
    offset: 0.5
  })

  .onStepEnter(response => {
    if (response.index === 0) {
      showFig("fig1_lead_time.html");
    }
    if (response.index === 1) {
      showFig("fig2_adr.html");
    }
    if (response.index === 2) {
      showFig("fig3_combined.html");
    }
  })

  .onStepExit(response => {
    // Si pugem, mostrem el gràfic anterior
    if (response.direction === "up") {
      if (response.index === 2) {
        showFig("fig2_adr.html");
      }
      if (response.index === 1) {
        showFig("fig1_lead_time.html");
      }
    }
  });
