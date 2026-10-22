import flet as ft

# ==========================================
# БАЗА ДАННЫХ (МЕНЮ КАФЕ)
# ==========================================
MENU = [
    {"id": 1, "name": "Эспрессо", "price": 150, "desc": "Крепкий бодрящий кофе"},
    {"id": 2, "name": "Капучино", "price": 220, "desc": "Кофе с нежной молочной пенкой"},
    {"id": 3, "name": "Круассан с шоколадом", "price": 180, "desc": "Свежая французская выпечка"},
    {"id": 4, "name": "Чизкейк Нью-Йорк", "price": 250, "desc": "Классический творожный десерт"},
    {"id": 5, "name": "Сэндвич с курицей", "price": 310, "desc": "Сытный перекус с зеленью"}
]


# ==========================================
# БИЗНЕС-ЛОГИКА (ФУНКЦИИ РАСЧЕТА)
# ==========================================
def calculate_total(cart_items):
    """
    Принимает список элементов в корзине.
    Каждый элемент — это словарь вида: {"id": 1, "quantity": 2}
    """
    total = 0.0
    for cart_item in cart_items:
        # Ищем блюдо в меню по id
        product = next((item for item in MENU if item["id"] == cart_item["id"]), None)
        if product:
            total += product["price"] * cart_item["quantity"]
    return total


# ==========================================
# КОНСОЛЬНЫЕ ТЕСТЫ (Запускаются отдельно)
# ==========================================
def run_tests():
    print("--- ЗАПУСК ТЕСТОВ ---")
    # Тест 1: 2 Эспрессо (id: 1, цена: 150) -> должно быть 300
    test_cart = [{"id": 1, "quantity": 2}]
    print(f"Тест для 2 шт. ID 1 (Ожидается 300): {calculate_total(test_cart)} руб.")

    # Тест 2: Пустой заказ -> должно быть 0
    empty_cart = []
    print(f"Тест для пустого заказа (Ожидается 0): {calculate_total(empty_cart)} руб.")
    print("---------------------\n")


# ==========================================
# ИНТЕРФЕЙС ПРИЛОЖЕНИЯ (FLET APPLICATION)
# ==========================================
def main(page: ft.Page):
    # Настройки окна приложения
    page.title = "Касса Кафе (Cafe POS)"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 800
    page.window_height = 600
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    # Заголовок на экране
    welcome_text = ft.Text(
        "Система Кассы Кафе\nМеню из 5 позиций",
        size=28,
        weight="BOLD",
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.ORANGE_ACCENT
    )
    page.add(welcome_text, ft.Divider(height=20, color=ft.Colors.GREEN_ACCENT))

    # Создаем контейнер для списка блюд
    menu_list = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, expand=True)

    # Заполняем список блюдами из базы данных
    for item in MENU:
        menu_list.controls.append(
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.RESTAURANT, color=ft.Colors.ORANGE_ACCENT, size=30),
                        ft.Column(
                            controls=[
                                ft.Text(item["name"], size=18, weight="BOLD"),
                                ft.Text(item["desc"], size=14, color=ft.Colors.GREY_400),
                            ],
                            expand=True
                        ),
                        ft.Text(f"{item['price']} руб.", size=18, weight="BOLD", color=ft.Colors.GREEN_ACCENT)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                padding=15,
                border_radius=10,
                bgcolor=ft.Colors.SURFACE
            )
        )

    # Добавляем готовое меню на страницу
    page.add(menu_list)


# ==========================================
# ТОЧКА ВХОДА В ПРОГРАММУ
# ==========================================
if __name__ == "__main__":
    # Сначала прогоняем тесты в консоли
    run_tests()
    # Затем запускаем графический интерфейс
    ft.run(main)
