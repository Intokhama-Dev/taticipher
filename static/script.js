function copyAndChangeIcon() {
    const btn = document.getElementById("copyBtn");
    const textArea = btn.previousElementSibling;
    const textToCopy = textArea.value;

    if (textToCopy) {
        navigator.clipboard.writeText(textToCopy).then(() => {
            btn.innerHTML = "✅";
            btn.style.color = "#92fe9d";
            setTimeout(() => {
                btn.innerHTML = "📋";
                btn.style.color = "";
            }, 3000);
        });
    }
}
