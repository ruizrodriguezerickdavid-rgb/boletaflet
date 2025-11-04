import flet as ft

def main(page: ft.Page):
    page.title = "Boleta de calificaciones"
    page.bgcolor = "red"
    page.window_width = 1600
    page.window_height = 600

    lista_alumnos = ft.Dropdown(
        width=150,
        label="Alumnos",
        options=[
            ft.dropdown.Option("vito007"),
            ft.dropdown.Option("el señor fiesta"),
            ft.dropdown.Option("elmaau"),
            ft.dropdown.Option("nicokadoavocado"),
            ft.dropdown.Option("bob toronja"),
        ],
    )

    esp = ft.Dropdown(
        width=150,
        label="Español",
        options=[ft.dropdown.Option(str(i)) for i in range(10, 101, 10)]
    )

    mat = ft.Dropdown(
        width=160,
        label="Matemáticas",
        options=[ft.dropdown.Option(str(i)) for i in range(10, 101, 10)]
    )

    ing = ft.Dropdown(
        width=130,
        label="Inglés",
        options=[ft.dropdown.Option(str(i)) for i in range(10, 101, 10)]
    )

    info = ft.Dropdown(
        width=140,
        label="Informática",
        options=[ft.dropdown.Option(str(i)) for i in range(10, 101, 10)]
    )

    hist = ft.Dropdown(
        width=135,
        label="Historia",
        options=[ft.dropdown.Option(str(i)) for i in range(10, 101, 10)]
    )
    
    monta = ft.Dropdown(
        width=180,
        label="como defender montapuercos",
        options=[ft.dropdown.Option(str(i)) for i in range(10, 101, 10)]
    )
    art = ft.Dropdown(
        width=180,
        label="artes",
        options=[ft.dropdown.Option(str(i)) for i in range(10, 101, 10)]
    )
    tabla_calificaciones = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Alumno")),
            ft.DataColumn(label=ft.Text("Español")),
            ft.DataColumn(label=ft.Text("Matemáticas")),
            ft.DataColumn(label=ft.Text("Inglés")),
            ft.DataColumn(label=ft.Text("Informática")),
            ft.DataColumn(label=ft.Text("Historia")),
            ft.DataColumn(label=ft.Text("como defender montapuercos")),
            ft.DataColumn(label=ft.Text("Promedio")),
        ],
        rows=[]
    )

    def calcular_promedio(e):
        notas = [
            int(esp.value or 0),
            int(mat.value or 0),
            int(ing.value or 0),
            int(info.value or 0),
            int(hist.value or 0),
        ]

        promedio = sum(notas) / len(notas)
        label_promedio= ft.Text(value="", size=20, width=100, color="white")

        label_promedio.value = f"{promedio:.2f}"

        nueva_fila = ft.DataRow(cells=[
            ft.DataCell(ft.Text(lista_alumnos.value or "")),
            ft.DataCell(ft.Text(esp.value or "")),
            ft.DataCell(ft.Text(mat.value or "")),
            ft.DataCell(ft.Text(ing.value or "")),
            ft.DataCell(ft.Text(info.value or "")),
            ft.DataCell(ft.Text(hist.value or "")),
            ft.DataCell(ft.Text(monta.value or "")),
            ft.DataCell(ft.Text(art.value or "")),
            ft.DataCell(ft.Text(f"{promedio:.2f}")),
        ])

        tabla_calificaciones.rows.append(nueva_fila)
        page.update()

    boton_calcular = ft.ElevatedButton(text="Calcular Promedio", on_click=calcular_promedio)

    fila_dropdowns = ft.Row(
        [
            lista_alumnos,
            esp,
            mat,
            ing,
            info,
            hist,
            monta,
            art,
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

    fila_boton = ft.Row(
        [boton_calcular],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        ft.Column(
            [
                fila_dropdowns,
                fila_boton,
                tabla_calificaciones
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )
ft.app(target=main, view=ft.WEB_BROWSER)
