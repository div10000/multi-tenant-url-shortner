const apiBase = "http://127.0.0.1:8000/api";  // Backend URL

// Elements
const logo = document.getElementById("logo");
const appName = document.getElementById("app-name");
const inputUrl = document.getElementById("original-url");
const shortenBtn = document.getElementById("shorten-btn");
const resultDiv = document.getElementById("result");
const shortUrlLink = document.getElementById("short-url");
const copyBtn = document.getElementById("copy-btn");

// 1️⃣ Fetch tenant info
async function fetchTenant() {
    try {
        const res = await fetch(`${apiBase}/tenant/info/`);
        const data = await res.json();
        logo.src = data.logo_url;
        appName.innerText = data.app_name;
        document.body.style.backgroundColor = data.primary_color || "#f4f4f4";
    } catch (err) {
        console.error("Tenant info fetch failed", err);
        appName.innerText = "URL Shortener";
    }
}

// 2️⃣ Shorten URL
async function shortenURL() {
    const url = inputUrl.value.trim();
    if (!url) return alert("Please enter a URL");

    try {
        const res = await fetch(`${apiBase}/shorten/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ original_url: url })
        });

        const data = await res.json();

        if (res.ok) {
            shortUrlLink.href = data.short_url;
            shortUrlLink.innerText = data.short_url;
            resultDiv.style.display = "block";
        } else {
            alert(data.error || JSON.stringify(data));
        }
    } catch (err) {
        console.error(err);
        alert("Something went wrong");
    }
}

// 3️⃣ Copy short URL
copyBtn.addEventListener("click", () => {
    navigator.clipboard.writeText(shortUrlLink.href);
    alert("Copied to clipboard!");
});

// Button click
shortenBtn.addEventListener("click", shortenURL);

// Load tenant info on page load
fetchTenant();
