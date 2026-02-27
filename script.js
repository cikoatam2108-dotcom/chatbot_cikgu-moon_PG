// ===== Helpers =====
const $ = (id) => document.getElementById(id);

const state = {
  gayaVisual: "",
  layout: "",
  nada: "",
  audiens: [],
  fokusIndustri: "",
  tema: [],
  skemaWarna: [],
  latar: [],
  tekstur: [],
  font: "",
};

function uniq(arr){ return Array.from(new Set(arr.filter(Boolean))); }

function chipSingle(containerId, onPick){
  const wrap = $(containerId);
  wrap.addEventListener("click", (e) => {
    const btn = e.target.closest(".chip");
    if(!btn) return;
    wrap.querySelectorAll(".chip").forEach(b => b.classList.remove("is-active"));
    btn.classList.add("is-active");
    onPick(btn.dataset.value);
    validate();
  });
}

function chipMulti(containerId, arrRef){
  const wrap = $(containerId);
  wrap.addEventListener("click", (e) => {
    const btn = e.target.closest(".chip");
    if(!btn) return;

    const v = btn.dataset.value;
    const isActive = btn.classList.toggle("is-active");
    if(isActive) arrRef.push(v);
    else {
      const idx = arrRef.indexOf(v);
      if(idx >= 0) arrRef.splice(idx,1);
    }
    // keep unique
    const u = uniq(arrRef);
    arrRef.length = 0;
    arrRef.push(...u);

    validate();
  });
}

// ===== Bind inputs =====
$("gayaVisual").addEventListener("change", (e) => { state.gayaVisual = e.target.value.trim(); validate(); });
$("nada").addEventListener("change", (e) => { state.nada = e.target.value.trim(); validate(); });
$("fokusIndustri").addEventListener("change", (e) => { state.fokusIndustri = e.target.value.trim(); validate(); });
$("fontSelect").addEventListener("change", (e) => { state.font = e.target.value.trim(); validate(); });

$("audiensInput").addEventListener("input", (e) => {
  const v = e.target.value.trim();
  state.audiens = v ? uniq(v.split(",").map(s => s.trim())) : [];
  validate();
});

$("temaInput").addEventListener("input", (e) => {
  const v = e.target.value.trim();
  state.tema = v ? uniq(v.split(",").map(s => s.trim())) : [];
  validate();
});

$("skemaWarnaInput").addEventListener("input", (e) => {
  // let user type extra, but still require at least 1 chip/type
  const v = e.target.value.trim();
  // store typed as 1 item if not empty
  // (chips will add more)
  state._warnaTyped = v;
  validate();
});

$("latarInput").addEventListener("input", (e) => {
  const v = e.target.value.trim();
  state._latarTyped = v;
  validate();
});

// ===== Chips wiring =====
chipSingle("layoutChips", (v) => state.layout = v);

chipMulti("audiensChips", state.audiens);
chipMulti("temaChips", state.tema);
chipMulti("warnaChips", state.skemaWarna);

// latar: chips 2 kumpulan (warna + tekstur) — gabungkan dalam output
chipMulti("latarWarnaChips", state.latar);
chipMulti("latarTeksturChips", state.tekstur);

// ===== Validate (9 medan wajib) =====
const requiredFields = [
  { key: "gayaVisual", label: "Gaya Visual" },
  { key: "layout", label: "Lajur atau Grid" },
  { key: "nada", label: "Nada" },
  { key: "audiens", label: "Sasaran Audiens" },
  { key: "fokusIndustri", label: "Fokus Industri" },
  { key: "tema", label: "Tema (Pilihan)" },
  { key: "skemaWarna", label: "Skema Warna" },
  { key: "latar", label: "Gaya Latar Belakang" },
  { key: "font", label: "Font" },
];

function isFilled(field){
  if(Array.isArray(state[field])) return state[field].length > 0;
  return String(state[field] || "").trim().length > 0;
}

function validate(){
  // allow typed skema warna/latar count as filled if user type
  const warnaFilled = state.skemaWarna.length > 0 || (state._warnaTyped && state._warnaTyped.length > 0);
  const latarFilled = state.latar.length > 0 || state.tekstur.length > 0 || (state._latarTyped && state._latarTyped.length > 0);

  const missing = [];
  for(const f of requiredFields){
    if(f.key === "skemaWarna"){
      if(!warnaFilled) missing.push(f.label);
      continue;
    }
    if(f.key === "latar"){
      if(!latarFilled) missing.push(f.label);
      continue;
    }
    if(!isFilled(f.key)) missing.push(f.label);
  }

  const ok = missing.length === 0;
  $("btnJana").disabled = !ok;

  $("hintText").textContent = ok
    ? "Dah cukup! Tekan JANA ya ✨"
    : `Alamak 😅 belum cukup lagi. Lengkapkan dulu ya: ${missing.join(", ")} ✨`;

  return ok;
}

// ===== Prompt generator =====
function buildPrompt(){
  const audiens = uniq(state.audiens).join(", ");
  const tema = uniq(state.tema).join(", ");
  const warna = uniq([...(state.skemaWarna || []), state._warnaTyped].filter(Boolean)).join(", ");
  const latar = uniq([...(state.latar || []), ...(state.tekstur || []), state._latarTyped].filter(Boolean)).join(", ");

  const temaLine = tema ? `Masukkan elemen tema: ${tema}. ` : "";

  return (
`Hasilkan infografik yang padat dan mudah difahami. ` +
`Gaya visual: ${state.gayaVisual}. ` +
`Susun atur: ${state.layout}. ` +
`Skema warna: ${warna}. ` +
`Keutamaan fon: ${state.font}. ` +
`Gaya latar belakang: ${latar}. ` +
`Nada penulisan: ${state.nada}. ` +
`Sasaran audiens: ${audiens}. ` +
`Fokus industri: ${state.fokusIndustri}. ` +
temaLine +
`Pastikan susun atur seimbang, tajuk jelas, poin ringkas, ikon/ilustrasi comel, dan hasil nampak kemas serta profesional dengan vibe Cikgu Moon tone.`
  );
}

$("btnJana").addEventListener("click", () => {
  if(!validate()) return;
  $("output").value = buildPrompt();
  toast("Dah siap! Prompt comel masuk kat bawah 💗");
});

$("btnTukar").addEventListener("click", () => {
  $("output").value = buildPrompt();
  toast("Dah tukar ayat sikit ✨");
});

$("btnSalin").addEventListener("click", async () => {
  const text = $("output").value.trim();
  if(!text){
    toast("Belum ada prompt lagi 🥺 Tekan JANA dulu ya.");
    return;
  }
  try{
    await navigator.clipboard.writeText(text);
    toast("Dah salin! 🦄💗");
  }catch{
    // fallback
    $("output").select();
    document.execCommand("copy");
    toast("Dah salin (cara lama) 💗");
  }
});

let tmr;
function toast(msg){
  clearTimeout(tmr);
  $("toast").textContent = msg;
  tmr = setTimeout(() => $("toast").textContent = "", 2200);
}

// initial
validate();

// ===== MODE TOGGLE: Infografik / Slaid =====
(() => {
  const btnInfografik = document.getElementById("btnModeInfografik");
  const btnSlaid = document.getElementById("btnModeSlaid");

  const layoutSection = document.getElementById("layoutSection");
  const orientasiSection = document.getElementById("orientasiSection");

  if(!btnInfografik || !btnSlaid || !layoutSection || !orientasiSection) return;

  let mode = "infografik"; // default

  function setMode(next){
    mode = next;

    // Toggle button active UI
    btnInfografik.classList.toggle("is-active", mode === "infografik");
    btnSlaid.classList.toggle("is-active", mode === "slaid");
    btnInfografik.setAttribute("aria-selected", mode === "infografik" ? "true" : "false");
    btnSlaid.setAttribute("aria-selected", mode === "slaid" ? "true" : "false");

    // Toggle medan
    layoutSection.style.display = (mode === "infografik") ? "" : "none";
    orientasiSection.style.display = (mode === "slaid") ? "" : "none";

    // OPTIONAL: kalau Cikgu ada function semak siap/enable button,
    // panggil balik kat sini supaya button "JANA" update ikut mode.
    if (typeof window.checkReady === "function") window.checkReady();
  }

  btnInfografik.addEventListener("click", () => setMode("infografik"));
  btnSlaid.addEventListener("click", () => setMode("slaid"));

  // start
  setMode("infografik");
})();
