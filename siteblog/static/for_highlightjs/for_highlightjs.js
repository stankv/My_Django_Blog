document.addEventListener('DOMContentLoaded', (event) => {
    // Инициализация подсветки кода
    hljs.highlightAll();
    hljs.initLineNumbersOnLoad();

    // Добавляем обработчики для кнопок копирования
    document.querySelectorAll('.copy-code').forEach(button => {
        const pre = button.parentElement;
        const code = pre.querySelector('code');
        const originalIcon = button.innerHTML;

        button.addEventListener('click', () => {
            // Копируем текст кода
            navigator.clipboard.writeText(code.textContent)
                .then(() => {
                    // Показываем подтверждение копирования
                    button.innerHTML = `
                        <svg viewBox="0 0 24 24">
                            <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z"/>
                        </svg>
                    `;
                    button.classList.add('copied');

                    // Возвращаем исходную иконку через 2 секунды
                    setTimeout(() => {
                        button.innerHTML = originalIcon;
                        button.classList.remove('copied');
                    }, 2000);
                })
                .catch(err => {
                    console.error('Ошибка копирования: ', err);
                    button.innerHTML = `
                        <svg viewBox="0 0 24 24">
                            <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"/>
                        </svg>
                    `;
                    setTimeout(() => {
                        button.innerHTML = originalIcon;
                    }, 2000);
                });
        });
    });
});