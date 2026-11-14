 function updateTime() {
    const now = new Date()
    const dateOptions = {day: 'numeric', month: 'short', year: 'numeric'};
    document.getElementById('current-date').textContent = now.toLocaleDateString('ru-RU', dateOptions);
    const timeOptions = {hour: '2-digit', minute: '2-digit'};
    document.getElementById('current-time').textContent = now.toLocaleTimeString('ru-RU', timeOptions);
}
updateTime();
setInterval(updateTime, 60000)
