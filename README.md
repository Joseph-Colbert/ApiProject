# Automatizacion API Todo.ly

Proyecto de evaluacion para automatizar con **Java 17, Gradle, Cucumber y Rest Assured** el flujo:

1. Crear un usuario temporal.
2. Obtener su token mediante autenticacion Basic.
3. Crear un proyecto usando el encabezado `Token`.
4. Consultar el proyecto.
5. Actualizar el proyecto.
6. Eliminar el proyecto.

La implementacion separa configuracion, cliente HTTP, estado del escenario y pasos BDD. No contiene usuarios, contrasenas ni tokens reales del proyecto de referencia.

## Requisitos

- JDK 17 o superior.
- Acceso a `https://todo.ly`.
- PowerShell, CMD o una terminal compatible.

## Ejecutar

En Windows:

```powershell
.\gradlew.bat clean cucumber
```

En Linux o macOS:

```bash
./gradlew clean cucumber
```

El reporte se genera en `build/reports/cucumber/cucumber.html`.

Variables opcionales:

- `TODO_LY_BASE_URL`: URL base; por defecto `https://todo.ly`.
- `TODO_LY_TEST_PASSWORD`: contrasena de los usuarios temporales; tiene un valor de prueba seguro por defecto.

## Postman

Importar en Postman, en este orden:

1. `postman/Todo.ly-Project-CRUD.postman_collection.json`
2. `postman/Todo.ly.postman_environment.json`

Seleccionar el environment **Todo.ly Local** y ejecutar la coleccion completa. Los scripts guardan automaticamente `email`, `token` y `projectId`.

## Estructura

```text
src/test/java/com/josephcolbert/apitesting/
  client/      Cliente Rest Assured y autenticacion
  config/      Configuracion por entorno
  context/     Estado aislado del escenario
  steps/       Definiciones Cucumber
src/test/resources/features/
  project_crud_token.feature
postman/
docs/
output/pdf/
```

## Documentacion de referencia

- Todo.ly API Wiki: https://todo.ly/ApiWiki/

