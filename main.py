import flet as ft

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

    # База данных меню (5 позиций с блюдами)
    MENU = [
        {"name": "Эспрессо", "price": 150, "desc": "Крепкий бодрящий кофе"},
        {"name": "Капучино", "price": 220, "desc": "Кофе с нежной молочной пенкой"},
        {"name": "Круассан с шоколадом", "price": 180, "desc": "Свежая французская выпечка"},
        {"name": "Чизкейк Нью-Йорк", "price": 250, "desc": "Классический творожный десерт"},
        {"name": "Сэндвич с курицей", "price": 310, "desc": "Сытный перекус с зеленью"}
    ]

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

# Запуск приложения
if __name__ == "__main__":
    ft.run(main)
