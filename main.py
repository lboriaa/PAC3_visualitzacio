import pandas as pd
import plotly.express as px

df = pd.read_csv("hotel_bookings.csv")

df = df[[
    "lead_time",
    "adr",
    "is_canceled"
]]

df = df[df["adr"] > 0]          # elimina ADRs 0 o negatius
df = df[df["lead_time"] >= 0]


df["lead_bin"] = pd.cut(df["lead_time"], bins=30)

lead_cancel = (
    df.groupby("lead_bin")
      .agg(
          lead_mean=("lead_time", "mean"),
          cancel_rate=("is_canceled", "mean"),
          n=("is_canceled", "size")
      )
      .reset_index()
)

fig1 = px.scatter(
    lead_cancel,
    x="lead_mean",
    y="cancel_rate",
    size="n",
    labels={
        "lead_mean": "Temps d’antelació (dies)",
        "cancel_rate": "Probabilitat de cancel·lació"
    }
)

fig1.update_layout(
    title="La cancel·lació augmenta amb el temps d’antelació",
    plot_bgcolor="white"
)

fig1.show()
# FIG 2
df["adr_bin"] = pd.cut(df["adr"], bins=30)

adr_cancel = (
    df.groupby("adr_bin")
      .agg(
          adr_mean=("adr", "mean"),
          cancel_rate=("is_canceled", "mean"),
          n=("is_canceled", "size")
      )
      .reset_index()
)

fig2 = px.scatter(
    adr_cancel,
    x="adr_mean",
    y="cancel_rate",
    size="n",
    labels={
        "adr_mean": "ADR mitjà (€)",
        "cancel_rate": "Probabilitat de cancel·lació"
    }
)

fig2.update_layout(
    title="El preu per si sol no determina clarament la cancel·lació",
    plot_bgcolor="white"
)

fig2.show()

# FIG 3
agg = (
    df.groupby(["lead_bin", "adr_bin"])
      .agg(
          lead_mean=("lead_time", "mean"),
          adr_mean=("adr", "mean"),
          cancel_rate=("is_canceled", "mean"),
          n=("is_canceled", "size")
      )
      .reset_index()
)

agg = agg[agg["n"] >= 30]

fig3 = px.scatter(
    agg,
    x="lead_mean",
    y="adr_mean",
    size="n",
    color="cancel_rate",
    color_continuous_scale="Reds",
    labels={
        "lead_mean": "Temps d’antelació (dies)",
        "adr_mean": "ADR mitjà (€)",
        "cancel_rate": "Probabilitat de cancel·lació"
    }
)

fig3.update_layout(
    title="El risc de cancel·lació emergeix de la combinació de temps i preu",
    plot_bgcolor="white"
)

fig3.show()

fig1.write_html("fig1_lead_time.html", include_plotlyjs="cdn")
fig2.write_html("fig2_adr.html", include_plotlyjs="cdn")
fig3.write_html("fig3_combined.html", include_plotlyjs="cdn")


