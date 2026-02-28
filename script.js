// ===== Helpers =====
const $ = (id) => document.getElementById(id);

const state = {
  gayaVisual: "",
  layout: "", // Susun Atur (Infografik) ATAU Orientasi (Slaid)
  nada: "",
  audiens: [],
  fokusIndustri: "",
  tema: [],
  skemaWarna: [],
  latar: [],
  tekstur: [],
  font: "",
  _warnaTyped: "",
  _latarTyped: "",
};

function uniq(arr){ return Array.from(new Set(arr.filter(Boolean))); }

// ===== Chips =====
function chipSingle(containerId, onPick){
  const wrap = $(containerId);
  if(!wrap) return;

  wrap.addEventListener("click", (e) => {
    const btn = e.target.closest(".chip");
    if(!btn) return;

    wrap.querySelectorAll(".chip").forEach(b => b.classList.remove("is-active"));
    btn.classList.add("is-active");

    onPick(btn.dataset.value || btn.textContent.trim());
    validate();
  });
}

function chipMulti(containerId, arrRef){
  const wrap = $(containerId);
  if(!wrap) return;

  wrap.addEventListener("click", (e) => {
    const btn = e.target.closest(".chip");
    if(!btn) return;

    const v = btn.dataset.value || btn.textContent.trim();
    const isActive = btn.classList.toggle("is-active");

    if(isActive) arrRef.push(v);
    else{
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
$("gayaVisual")?.addEventListener("change", (e) => { state.gayaVisual = e.target.value.trim(); validate(); });
$("nada")?.addEventListener("change", (e) => { state.nada = e.target.value.trim(); validate(); });
$("fokusIndustri")?.addEventListener("change", (e) => { state.fokusIndustri = e.target.value.trim(); validate(); });
$("fontSelect")?.addEventListener("change", (e) => { state.font = e.target.value.trim(); validate(); });

$("audiensInput")?.addEventListener("input", (e) => {
  const v = e.target.value.trim();
  state.audiens = v ? uniq(v.split(",").map(s => s.trim())) : [];
  validate();
});

// ✅ Tema dropdown (multiple)
const temaSelectEl = $("temaSelect");
temaSelectEl?.addEventListener("change", () => {
  const selected = Array.from(temaSelectEl.selectedOptions)
    .map(o => o.textContent.trim().replace(/^[^\w(]+/u, "").trim()); // buang emoji depan

  state.tema = selected;
  validate();
});

$("skemaWarnaInput")?.addEventListener("input", (e) => {
  state._warnaTyped = e.target.value.trim();
  validate();
});

$("latarInput")?.addEventListener("input", (e) => {
  state._latarTyped = e.target.value.trim();
  validate();
});

// ===== Chips wiring =====
chipSingle("layoutChips", (v) => state.layout = v);       // Infografik
chipSingle("orientasiChips", (v) => state.layout = v);    // Slaid

chipMulti("audiensChips", state.audiens);
chipMulti("warnaChips", state.skemaWarna);
chipMulti("latarWarnaChips", state.latar);
chipMulti("latarTeksturChips", state.tekstur);

// ===== Validate =====
const requiredFields = [
  { key: "gayaVisual", label: "Gaya Visual" },
  { key: "layout", label: "Susun Atur / Orientasi" },
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
    `Susun atur / orientasi: ${state.layout}. ` +
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

// ===== Buttons =====
$("btnJana")?.addEventListener("click", () => {
  if(!validate()) return;
  $("output").value = buildPrompt();
  toast("Dah siap! Prompt comel masuk kat bawah 💗");
});

$("btnTukar")?.addEventListener("click", () => {
  $("output").value = buildPrompt();
  toast("Dah tukar ayat sikit ✨");
});

$("btnSalin")?.addEventListener("click", async () => {
  const text = $("output").value.trim();
  if(!text){
    toast("Belum ada prompt lagi 🥺 Tekan JANA dulu ya.");
    return;
  }
  try{
    await navigator.clipboard.writeText(text);
    toast("Dah salin! 🦄💗");
  }catch{
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

// ===== Toggle Mode =====
let mode = "infografik";

function clearChipActive(id){
  const w = $(id);
  if(!w) return;
  w.querySelectorAll(".chip").forEach(c => c.classList.remove("is-active"));
}

function setMode(next){
  mode = next;

  const btnInfo = $("btnModeInfografik");
  const btnSlaid = $("btnModeSlaid");
  const layoutSection = $("layoutSection");
  const orientasiSection = $("orientasiSection");

  btnInfo?.classList.toggle("is-active", mode === "infografik");
  btnSlaid?.classList.toggle("is-active", mode === "slaid");
  btnInfo?.setAttribute("aria-selected", mode === "infografik" ? "true" : "false");
  btnSlaid?.setAttribute("aria-selected", mode === "slaid" ? "true" : "false");

  if(layoutSection && orientasiSection){
    layoutSection.style.display = (mode === "infografik") ? "" : "none";
    orientasiSection.style.display = (mode === "slaid") ? "" : "none";
  }

  // reset layout supaya user pilih ikut mode
  state.layout = "";
  clearChipActive("layoutChips");
  clearChipActive("orientasiChips");

  validate();
}

$("btnModeInfografik")?.addEventListener("click", () => setMode("infografik"));
$("btnModeSlaid")?.addEventListener("click", () => setMode("slaid"));

// init
setMode("infografik");
validate();
