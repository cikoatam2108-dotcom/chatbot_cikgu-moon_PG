// ========= Helpers =========
const $ = (id) => document.getElementById(id);

function setSingleSelect(containerEl, stateKey, state) {
  containerEl.addEventListener("click", (e) => {
    const btn = e.target.closest(".chip");
    if (!btn) return;

    // single select: clear all
    containerEl.querySelectorAll(".chip").forEach(c => c.classList.remove("is-active"));
    btn.classList.add("is-active");

    state[stateKey] = btn.dataset.value || btn.textContent.trim();
    updateGate(state);
  });
}

function setMultiSelect(containerEl, stateKey, state) {
  containerEl.addEventListener("click", (e) => {
    const btn = e.target.closest(".chip");
    if (!btn) return;

    btn.classList.toggle("is-active");
    const selected = [...containerEl.querySelectorAll(".chip.is-active")]
      .map(b => b.dataset.value || b.textContent.trim());

    state[stateKey] = selected;
    updateGate(state);
  });
}

function normalizeList(arr) {
  if (!arr) return [];
  return arr.map(x => String(x).replace(/\s+/g, " ").trim()).filter(Boolean);
}

function updateGate(state){
  const required = [
    ["Gaya Visual", state.gayaVisual],
    ["Lajur atau Grid", state.layout],
    ["Nada", state.nada],
    ["Sasaran Audiens", (state.audiensText || normalizeList(state.audiens).join(", "))],
    ["Tema (Pilihan)", (state.temaText || normalizeList(state.tema).join(", "))],
    ["Skema Warna", (state.warnaText || normalizeList(state.warna).join(", "))],
    ["Gaya Latar Belakang", (state.latarText || normalizeList(state.latarWarna).join(", ") || normalizeList(state.latarTekstur).join(", "))],
    ["Fokus Industri", state.fokusIndustri],
    ["Font", state.font]
  ];

  const missing = required.filter(([,v]) => !String(v || "").trim()).map(([k]) => k);

  const btn = $("btnJana");
  const hint = $("hintText");

  if (missing.length === 0){
    btn.disabled = false;
    hint.textContent = "Okayyy ✨ tekan butang jana, Cikgu Moon buatkan prompt cantik!";
  } else {
    btn.disabled = true;
    hint.textContent = `Alamak 😅 belum cukup lagi. Lengkapkan dulu ya: ${missing.join(", ")} ✨`;
  }
}

function buildPrompt(state){
  const gaya = state.gayaVisual;
  const layout = state.layout;
  const nada = state.nada;
  const audiens = (state.audiensText || normalizeList(state.audiens).join(", "));
  const tema = (state.temaText || normalizeList(state.tema).join(", "));
  const warna = (state.warnaText || normalizeList(state.warna).join(", "));
  const latar = [
    state.latarText,
    ...normalizeList(state.latarWarna),
    ...normalizeList(state.latarTekstur)
  ].filter(Boolean).join(", ");
  const fokus = state.fokusIndustri;
  const font = state.font;

  return [
    `Hasilkan infografik yang padat dan mudah faham.`,
    `Gaya visual: ${gaya}.`,
    `Susun atur: ${layout}.`,
    `Skema warna: ${warna}.`,
    `Fon: ${font}.`,
    `Latar belakang: ${latar}.`,
    `Nada penulisan: ${nada}.`,
    `Sasaran audiens: ${audiens}.`,
    tema ? `Tema pilihan: ${tema}.` : ``,
    `Fokus industri: ${fokus}.`,
    `Infografik perlu seimbang, jelas, kemas, dan menarik (Cikgu Moon tone: comel + profesional).`
  ].filter(Boolean).join(" ");
}

// ========= App =========
const state = {
  gayaVisual: "",
  layout: "",
  nada: "",
  audiens: [],
  audiensText: "",
  fokusIndustri: "",
  tema: [],
  temaText: "",
  warna: [],
  warnaText: "",
  latarText: "",
  latarWarna: [],
  latarTekstur: [],
  font: ""
};

// Dropdowns
$("gayaVisual").addEventListener("change", (e) => { state.gayaVisual = e.target.value; updateGate(state); });
$("nada").addEventListener("change", (e) => { state.nada = e.target.value; updateGate(state); });
$("fokusIndustri").addEventListener("change", (e) => { state.fokusIndustri = e.target.value; updateGate(state); });
$("fontSelect").addEventListener("change", (e) => { state.font = e.target.value; updateGate(state); });

// Inputs
$("audiensInput").addEventListener("input", (e) => { state.audiensText = e.target.value.trim(); updateGate(state); });
$("temaInput").addEventListener("input", (e) => { state.temaText = e.target.value.trim(); updateGate(state); });
$("skemaWarnaInput").addEventListener("input", (e) => { state.warnaText = e.target.value.trim(); updateGate(state); });
$("latarInput").addEventListener("input", (e) => { state.latarText = e.target.value.trim(); updateGate(state); });

// Chips
setSingleSelect($("layoutChips"), "layout", state);
setMultiSelect($("audiensChips"), "audiens", state);
setMultiSelect($("temaChips"), "tema", state);
setMultiSelect($("warnaChips"), "warna", state);
setSingleSelect($("latarWarnaChips"), "latarWarna", state);     // single select latar warna
setMultiSelect($("latarTeksturChips"), "latarTekstur", state);  // multi select tekstur

// Override single select handler for latarWarnaChips to store as array with 1 item
$("latarWarnaChips").addEventListener("click", () => {
  const active = $("latarWarnaChips").querySelector(".chip.is-active");
  state.latarWarna = active ? [active.dataset.value || active.textContent.trim()] : [];
  updateGate(state);
});

// Buttons
$("btnJana").addEventListener("click", () => {
  $("output").value = buildPrompt(state);
  $("toast").textContent = "Siap! Prompt dah dijana 🌸";
});

$("btnSalin").addEventListener("click", async () => {
  const text = $("output").value.trim();
  if (!text){ $("toast").textContent = "Belum ada prompt lagi 😅"; return; }

  try{
    await navigator.clipboard.writeText(text);
    $("toast").textContent = "Berjaya salin! 🦄✨";
  } catch {
    $("toast").textContent = "Tak boleh auto-salin 😭 (Cikgu copy manual je ya)";
  }
});

$("btnTukar").addEventListener("click", () => {
  $("output").value = "";
  $("toast").textContent = "Okay, kita tukar semula 🌷";
});

// init
updateGate(state);
