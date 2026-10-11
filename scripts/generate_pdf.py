from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Informe_Automatizacion_API_Todoly.pdf"
REPOSITORY_URL = "https://github.com/Joseph-Colbert/api-testing-todoly"

NAVY = colors.HexColor("#14213D")
BLUE = colors.HexColor("#2563EB")
PALE_BLUE = colors.HexColor("#EAF1FF")
INK = colors.HexColor("#1F2937")
MUTED = colors.HexColor("#64748B")
LINE = colors.HexColor("#CBD5E1")
GREEN = colors.HexColor("#15803D")


def register_fonts():
    candidates = [
        ("C:/Windows/Fonts/arial.ttf", "Arial"),
        ("C:/Windows/Fonts/arialbd.ttf", "Arial-Bold"),
    ]
    for path, name in candidates:
        if Path(path).exists():
            pdfmetrics.registerFont(TTFont(name, path))


def footer(canvas, document):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.line(18 * mm, 14 * mm, 192 * mm, 14 * mm)
    canvas.setFont("Arial", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(18 * mm, 9 * mm, "Automatizacion REST API Todo.ly")
    canvas.drawRightString(192 * mm, 9 * mm, f"Pagina {document.page}")
    canvas.restoreState()


def build():
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=20 * mm,
        title="Informe de automatizacion REST API Todo.ly",
        author="Joseph Colbert",
        subject="Seccion 2 - Pregunta Rest API",
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="TitleCustom", parent=styles["Title"], fontName="Arial-Bold",
        fontSize=26, leading=30, textColor=NAVY, alignment=TA_LEFT, spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="Subtitle", parent=styles["Normal"], fontName="Arial",
        fontSize=12, leading=17, textColor=MUTED, spaceAfter=18,
    ))
    styles.add(ParagraphStyle(
        name="H1Custom", parent=styles["Heading1"], fontName="Arial-Bold",
        fontSize=16, leading=20, textColor=NAVY, spaceBefore=12, spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="H2Custom", parent=styles["Heading2"], fontName="Arial-Bold",
        fontSize=11, leading=14, textColor=BLUE, spaceBefore=8, spaceAfter=5,
    ))
    styles.add(ParagraphStyle(
        name="BodyCustom", parent=styles["BodyText"], fontName="Arial",
        fontSize=9.5, leading=14, textColor=INK, spaceAfter=7,
    ))
    styles.add(ParagraphStyle(
        name="Small", parent=styles["BodyText"], fontName="Arial",
        fontSize=8, leading=11, textColor=INK,
    ))
    styles.add(ParagraphStyle(
        name="TableHeader", parent=styles["BodyText"], fontName="Arial-Bold",
        fontSize=8, leading=11, textColor=colors.white,
    ))
    styles.add(ParagraphStyle(
        name="CodeCustom", parent=styles["Code"], fontName="Courier",
        fontSize=8.5, leading=12, textColor=NAVY, backColor=PALE_BLUE,
        borderPadding=8, spaceBefore=4, spaceAfter=10,
    ))
    styles.add(ParagraphStyle(
        name="Badge", parent=styles["BodyText"], fontName="Arial-Bold",
        fontSize=9, leading=12, textColor=colors.white, backColor=GREEN,
        borderPadding=7, alignment=TA_CENTER, spaceAfter=10,
    ))

    story = []
    story.append(Spacer(1, 12 * mm))
    story.append(Paragraph("AUTOMATIZACION REST API", styles["TitleCustom"]))
    story.append(Paragraph("Todo.ly - Seccion 2", styles["Subtitle"]))
    story.append(Spacer(1, 4 * mm))

    metadata = Table([
        ["Autor", "Joseph Colbert"],
        ["Fecha", "11 de octubre de 2026"],
        ["Stack", "Java 17 / Gradle / Cucumber / Rest Assured"],
        ["Flujo", "Usuario nuevo + token + CRUD de proyecto"],
    ], colWidths=[35 * mm, 125 * mm])
    metadata.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "Arial"),
        ("FONTNAME", (0, 0), (0, -1), "Arial-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("TEXTCOLOR", (0, 0), (0, -1), NAVY),
        ("TEXTCOLOR", (1, 0), (1, -1), INK),
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story.append(metadata)
    story.append(Spacer(1, 10 * mm))
    story.append(Paragraph("RESULTADO VERIFICADO: 1 escenario y 7 pasos aprobados", styles["Badge"]))
    story.append(Paragraph(
        f'<b>Repositorio publico:</b><br/><link href="{REPOSITORY_URL}" color="#2563EB">{REPOSITORY_URL}</link>',
        styles["BodyCustom"],
    ))
    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph(
        "Este documento presenta el caso de prueba, el diseno clean, la evidencia de ejecucion y las instrucciones para reproducir la automatizacion.",
        styles["BodyCustom"],
    ))
    story.append(PageBreak())

    story.append(Paragraph("1. Objetivo", styles["H1Custom"]))
    story.append(Paragraph(
        "Automatizar un caso de prueba E2E para la API de Todo.ly, utilizando el stack solicitado y manteniendo separadas la configuracion, las peticiones HTTP, el estado del escenario y las validaciones de negocio.",
        styles["BodyCustom"],
    ))

    story.append(Paragraph("2. Flujo seleccionado", styles["H1Custom"]))
    story.append(Paragraph(
        "Se eligio el primer flujo: crear un usuario, obtener su token y ejecutar Create / Read / Update / Delete de un proyecto con autenticacion por token. Aunque la consigna resume Create / Update / Delete, se agrega la consulta GET para comprobar la persistencia antes y despues de la actualizacion.",
        styles["BodyCustom"],
    ))

    story.append(Paragraph("3. Caso de prueba", styles["H1Custom"]))
    case_data = [
        ["ID", "TC-API-001"],
        ["Nombre", "CRUD de proyecto con usuario nuevo y autenticacion por token"],
        ["Prioridad", "Alta"],
        ["Tipo", "Funcional - integracion E2E - positivo"],
        ["Precondicion", "Todo.ly disponible y acceso a Internet"],
        ["Datos", "Correo unico, contrasena configurable y nombres controlados"],
    ]
    case_table = Table(case_data, colWidths=[31 * mm, 129 * mm])
    case_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "Arial"),
        ("FONTNAME", (0, 0), (0, -1), "Arial-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("TEXTCOLOR", (0, 0), (0, -1), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("BACKGROUND", (0, 0), (0, -1), PALE_BLUE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(case_table)
    story.append(Spacer(1, 5 * mm))

    headers = [
        Paragraph("Paso", styles["TableHeader"]),
        Paragraph("Peticion", styles["TableHeader"]),
        Paragraph("Resultado esperado", styles["TableHeader"]),
    ]
    rows = [
        ["1", "POST /api/user.json", "HTTP 200 y correo creado"],
        ["2", "GET /api/authentication/token.json", "HTTP 200 y TokenString no vacio"],
        ["3", "POST /api/projects.json", "HTTP 200, nombre correcto, Deleted=false"],
        ["4", "GET /api/projects/{id}.json", "HTTP 200, mismo id y nombre original"],
        ["5", "PUT /api/projects/{id}.json", "HTTP 200 y nombre actualizado"],
        ["6", "GET /api/projects/{id}.json", "HTTP 200 y cambio persistido"],
        ["7", "DELETE /api/projects/{id}.json", "HTTP 200 y Deleted=true"],
    ]
    steps = Table([headers] + rows, colWidths=[13 * mm, 65 * mm, 82 * mm], repeatRows=1)
    steps.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Arial-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Arial"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("TEXTCOLOR", (0, 1), (-1, -1), INK),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(steps)
    story.append(PageBreak())

    story.append(Paragraph("4. Diseno clean", styles["H1Custom"]))
    architecture = [
        ("config", "Centraliza URL base y variables de entorno."),
        ("client", "Construye peticiones Rest Assured y aplica Basic Auth o Token segun el endpoint."),
        ("context", "Mantiene correo, token, id de proyecto y ultima respuesta dentro del escenario."),
        ("steps", "Traduce Gherkin a acciones y aserciones observables."),
        ("features", "Describe el comportamiento esperado en lenguaje de negocio."),
        ("postman", "Permite repetir manualmente el mismo encadenamiento."),
    ]
    for name, description in architecture:
        story.append(KeepTogether([
            Paragraph(name, styles["H2Custom"]),
            Paragraph(description, styles["BodyCustom"]),
        ]))

    story.append(Paragraph("5. Seguridad de la prueba", styles["H1Custom"]))
    story.append(Paragraph(
        "No se copiaron las credenciales visibles del proyecto de referencia. Cada ejecucion genera un correo unico. La contrasena puede configurarse por entorno y el token se conserva solamente en memoria durante el escenario. Las solicitudes de proyecto usan el encabezado Token y no combinan Basic Auth con token.",
        styles["BodyCustom"],
    ))

    story.append(Paragraph("6. Especificacion Cucumber", styles["H1Custom"]))
    story.append(Paragraph(
        "Dado un usuario nuevo registrado en Todo.ly<br/>"
        "Y obtengo el token de autenticacion del usuario<br/>"
        "Cuando creo un proyecto usando el token<br/>"
        "Entonces puedo consultarlo, actualizarlo y eliminarlo usando el token",
        styles["CodeCustom"],
    ))

    story.append(Paragraph("7. Evidencia de ejecucion", styles["H1Custom"]))
    story.append(Paragraph("Comando ejecutado:", styles["BodyCustom"]))
    story.append(Paragraph(".\\gradlew.bat clean cucumber", styles["CodeCustom"]))
    story.append(Paragraph("Resultado obtenido el 11 de octubre de 2026:", styles["BodyCustom"]))
    story.append(Paragraph(
        "1 scenario (1 passed)<br/>7 steps (7 passed)<br/>BUILD SUCCESSFUL",
        styles["CodeCustom"],
    ))
    story.append(Paragraph(
        "La validacion real creo el proyecto, comprobo su contenido, actualizo el nombre, verifico la persistencia y elimino el proyecto. Cucumber genero el reporte HTML en build/reports/cucumber/cucumber.html.",
        styles["BodyCustom"],
    ))
    story.append(PageBreak())

    story.append(Paragraph("8. Como ejecutar", styles["H1Custom"]))
    story.append(Paragraph("Windows", styles["H2Custom"]))
    story.append(Paragraph(".\\gradlew.bat clean cucumber", styles["CodeCustom"]))
    story.append(Paragraph("Linux o macOS", styles["H2Custom"]))
    story.append(Paragraph("./gradlew clean cucumber", styles["CodeCustom"]))
    story.append(Paragraph(
        "Variables opcionales: TODO_LY_BASE_URL cambia la URL base y TODO_LY_TEST_PASSWORD cambia la contrasena temporal. Ninguna variable sensible se versiona.",
        styles["BodyCustom"],
    ))

    story.append(Paragraph("9. Postman", styles["H1Custom"]))
    story.append(Paragraph(
        "Importar primero Todo.ly-Project-CRUD.postman_collection.json y despues Todo.ly.postman_environment.json. Seleccionar el environment Todo.ly Local y ejecutar la coleccion completa. Sus scripts generan el correo y guardan automaticamente TokenString y projectId.",
        styles["BodyCustom"],
    ))

    story.append(Paragraph("10. Repositorio publico", styles["H1Custom"]))
    story.append(Paragraph(
        f'<link href="{REPOSITORY_URL}" color="#2563EB">{REPOSITORY_URL}</link>',
        styles["BodyCustom"],
    ))

    story.append(Paragraph("11. Conclusion", styles["H1Custom"]))
    story.append(Paragraph(
        "El caso cubre el flujo requerido con datos independientes, autenticacion por token y aserciones sobre cada respuesta. La estructura permite mantener el cliente HTTP separado del comportamiento BDD y ofrece evidencia reproducible en Gradle, Cucumber y Postman.",
        styles["BodyCustom"],
    ))

    story.append(Paragraph("12. Referencias", styles["H1Custom"]))
    references = [
        ("Todo.ly API Wiki", "https://todo.ly/ApiWiki/"),
        ("Rest Assured", "https://rest-assured.io/"),
        ("Cucumber", "https://cucumber.io/docs/cucumber/"),
        ("Gradle", "https://docs.gradle.org/"),
    ]
    for label, url in references:
        story.append(Paragraph(f'- <link href="{url}" color="#2563EB">{label}: {url}</link>', styles["BodyCustom"]))

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == "__main__":
    build()

