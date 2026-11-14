 function updateTime() {
    const now = new Date()
    const dateOptions = {day: 'numeric', month: 'short', year: 'numeric'};
    document.getElementById('current-date').textContent = now.toLocaleDateString('ru-RU', dateOptions);
    const timeOptions = {hour: '2-digit', minute: '2-digit'};
    document.getElementById('current-time').textContent = now.toLocaleTimeString('ru-RU', timeOptions);
}
updateTime();
setInterval(updateTime, 60000)
        // Находим элементы
const modal = document.getElementById('projectModal');
const openBtn = document.querySelector('.btn-add'); // Ваша кнопка добавить
const closeBtn = document.getElementById('closeModal');

        // Открыть окно при клике на кнопку
openBtn.addEventListener('click', function(e) {
    e.preventDefault(); // Отменяем переход по ссылке href="#"
    modal.classList.add('active');
});

        // Закрыть окно при клике на крестик
        closeBtn.addEventListener('click', function() {
            modal.classList.remove('active');
        });

        // Закрыть кно при клике на темный фон (вне окна)
        window.addEventListener('click', function(e) {
            if (e.target === modal) {
                modal.classList.remove('active');
            }
        });

        // Если форма была отправлена с ошибками (например, не заполнено поле)
        // и страница перезагрузилась, автоматически открываем окно снова
        {% if form.errors %}
            modal.classList.add('active');
        {% endif %}