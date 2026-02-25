// ====== Chips helper ======
function setupChips(containerId, { single = false } = {}) {
  const el = document.getElementById(containerId);
  if (!el) return;

  el.addEventListener("click", (e) => {
    const btn = e.target.closest(".chip");
    if (!btn) return;

    if (single) {
      el.querySelectorAll(".chip").forEach(b => b.classList.remove("is-active"));
      btn.classList.add("is-active");
    } else {
      btn.classList.toggle("is-active");
    }
    syncButtonState();
  });
}

function getSingle(containerId) {
  const el = document.getElementById(containerId);
  const b = el?.querySelector(".chip.is-active");
  return b?.dataset?.value || "";
}

function getMany(containerId) {
  const el = document.getElementById(containerId);
  return el ? [...el.querySelectorAll(".chip.is-active")].map(b => b.dataset.value) : [];
}

function val(id) {
  return (document.getElementById(id)?.value || "").trim();
}

function setToast(msg) {
  const t = document.getElementById("toast");
  if (!t) return;
  t.textContent = msg;
  if (msg) setTimeout(() => (t.textContent = ""), 2200);
}

// ====== 9 medan wajib ======
function validate9() {
  const missing = [];

  // 1 Gaya Visual
  if (!val("gayaVisual")) missing.push("Gaya Visual");

  // 2 Lajur/Grid (single chip)
  if (!getSingle("layoutChips")) missing.push("Lajur atau Grid");

  // 3 Nada
  if (!val("nada")) missing.push("Nada");

  // 4 Sasaran Audiens (input ATAU chip)
  const audiensOk = !!val("audiensInput") || getMany("audiensChips").length > 0;
  if (!audiensOk) missing.push("Sasaran Audiens");

  // 5 Tema (Pilihan) (input ATAU chip)
  const temaOk = !!val("temaInput") || getMany("temaChips").length > 0;
  if (!temaOk) missing.push("Tema (Pilihan)");

  // 6 Skema Warna (input ATAU chip)
  const warnaOk = !!val("skemaWarnaInput") || getMany("warnaChips").length > 0;
  if (!warnaOk) missing.push("Skema Warna");

  // 7 Gaya Latar Belakang (input ATAU chips)
  const latarOk =
    !!val("latarInput") ||
    !!getSingle("latarWarnaChips") ||
    getMany("latarTeksturChips").length > 0;
  if (!latarOk) missing.push("Gaya Latar Belakang");

  // 8 Fokus Industri
  if (!val("fokusIndustri")) missing.push("Fokus Industri");

  // 9 Font
  if (!val("fontSelect")) missing.push("Font");

  return missing;
}

function syncButtonState() {
  const missing = validate9();
  const btn = document.getElementById("btnJana");
  const hint = document.getElementById("hintText");

  btn.disabled = missing.length > 0;

  if (missing.length) {
    hint.textContent = "Alamak 😅 belum cukup lagi. Lengkapkan dulu ya: " + missing.join(", ") + " ✨";
    btn.title = "Sila lengkapkan: " + missing.join(", ");
  } else {
    hint.textContent = "Siap! Jom Cikgu Moon jana prompt cantik untuk Cikgu ✨";
    btn.title = "Sedia jana prompt";
  }
}

// ====== Build Prompt (Cikgu Moon tone) ======
function buildPrompt() {
  const gayaVisual = val("gayaVisual");
  const layout = getSingle("layoutChips");
  const nada = val("nada");

  const audiens = val("audiensInput") || getMany("audiensChips").join(", ");
  const tema = val("temaInput") || getMany("temaChips").join(", ");

  const skemaWarna = val("skemaWarnaInput") || getMany("warnaChips").join(", ");

  const latarInput = val("latarInput");
  const latarWarna = getSingle("latarWarnaChips");
  const latarTekstur = getMany("latarTeksturChips").join(", ");
  const latarGabung = [latarInput, latarWarna, latarTekstur].filter(Boolean).join(" | ");

  const fokusIndustri = val("fokusIndustri");
  const font = val("fontSelect");

  // Prompt “natural” macam contoh NotebookLM yang Cikgu tunjuk
  return [
    `Hasilkan infografik yang padat dan kemas.`,
    `Guna gaya visual "${gayaVisual}".`,
    `Susun atur "${layout}".`,
    `Guna skema warna "${skemaWarna}" dan fon "${font}".`,
    `Latar belakang: ${latarGabung || "ikut yang sesuai"}.`,
    `Sasaran audiens: ${audiens}.`,
    `Tema: ${tema}.`,
    `Nada penulisan: ${nada}.`,
    `Fokus industri: ${fokusIndustri}.`,
    `Infografik perlu seimbang, jelas, menarik, dan mudah difahami.`,
    `Sila gunakan tajuk, subjudul dan poin ringkas supaya nampak profesional.`
  ].join(" ");
}

// Variasi kecil untuk butang “Tukar”
function buildPromptVariant() {
  const base = buildPrompt();
  const extras = [
    "Sertakan ikon kecil yang sesuai di setiap seksyen.",
    "Pastikan spacing lega dan ada hierarchy tajuk yang jelas.",
    "Tambahkan ringkasan 1 ayat di bahagian bawah.",
    "Gunakan gaya bahasa yang mesra tetapi kemas.",
    "Letakkan highlight pada 3 poin utama (maksimum)."
  ];
  const pick = extras[Math.floor(Math.random() * extras.length)];
  return base + " " + pick;
}

// ====== Main ======
window.addEventListener("DOMContentLoaded", () => {
  // Setup chips
  setupChips("layoutChips", { single: true });
  setupChips("audiensChips", { single: false });
  setupChips("temaChips", { single: false });
  setupChips("warnaChips", { single: false });
  setupChips("latarWarnaChips", { single: true });
  setupChips("latarTeksturChips", { single: false });

  // Monitor inputs/selects
  document.querySelectorAll("input, select").forEach(el => {
    el.addEventListener("input", syncButtonState);
    el.addEventListener("change", syncButtonState);
  });

  // Initial
  syncButtonState();

  // Jana
  document.getElementById("btnJana").addEventListener("click", () => {
    const missing = validate9();
    if (missing.length) {
      alert("Cikgu sayang 😅 lengkapkan dulu ya:\n- " + missing.join("\n- "));
      return;
    }
    document.getElementById("output").value = buildPrompt();
    setToast("Siap! Prompt dah dijana 💗");
    document.getElementById("output").scrollIntoView({ behavior: "smooth", block: "center" });
  });

  // Tukar (variant)
  document.getElementById("btnTukar").addEventListener("click", () => {
    const missing = validate9();
    if (missing.length) {
      alert("Cikgu isi semua pilihan dulu ya 😄\n- " + missing.join("\n- "));
      return;
    }
    document.getElementById("output").value = buildPromptVariant();
    setToast("Okay! Cikgu Moon bagi versi lain ✨");
  });

  // Salin
  document.getElementById("btnSalin").addEventListener("click", async () => {
    const out = document.getElementById("output").value.trim();
    if (!out) {
      setToast("Belum ada prompt lagi 😅 Tekan Jana dulu ya!");
      return;
    }
    try {
      await navigator.clipboard.writeText(out);
      setToast("Prompt dah disalin 🦄💗");
    } catch {
      // fallback
      const ta = document.getElementById("output");
      ta.focus();
      ta.select();
      document.execCommand("copy");
      setToast("Prompt dah disalin 💗");
    }
  });
});
