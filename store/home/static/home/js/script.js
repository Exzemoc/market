// Ожидаем, что DOM-дерево полностью загружено
document.addEventListener('DOMContentLoaded', function () {
  // Находим кнопку "Добавить в корзину"
  const addToCartButton = document.querySelector('#form_add_to_cart button');

  // Добавляем обработчик события на нажатие кнопки
  addToCartButton.addEventListener('click', function (event) {
    event.preventDefault(); // Отменяем стандартное действие (отправку формы)

    // Показываем сообщение о добавлении товара в корзину
    showCartMessage();
  });
});

// Функция для показа сообщения
function showCartMessage() {
  const cartMessage = document.getElementById('cart-message');
  cartMessage.style.display = 'block';

  // Через 3 секунды скрываем сообщение
  setTimeout(function () {
    cartMessage.style.display = 'none';
  }, 3000);
}