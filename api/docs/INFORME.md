# Automatizacion REST API Todo.ly

## Seccion 2 - Pregunta Rest API

**Autor:** Joseph Colbert  
**Fecha:** 11 de octubre de 2026  
**Repositorio publico previsto:** https://github.com/Joseph-Colbert/api-testing-todoly

## 1. Objetivo

Automatizar un caso de prueba E2E para Todo.ly utilizando Gradle, Java 17, Cucumber y Rest Assured, con una estructura limpia y responsabilidades separadas.

## 2. Flujo seleccionado

Crear un usuario y, con ese usuario, obtener un token para crear, consultar, actualizar y eliminar un proyecto usando el encabezado HTTP `Token`.

## 3. Caso de prueba

**Identificador:** TC-API-001  
**Nombre:** CRUD de proyecto con usuario nuevo y autenticacion por token  
**Prioridad:** Alta  
**Tipo:** Funcional, integracion E2E, positivo  
**Precondiciones:** Todo.ly disponible y acceso a Internet.  
**Datos:** correo unico generado en cada ejecucion, nombre de usuario de prueba, contrasena configurable y nombres de proyecto controlados.

| Paso | Accion | Resultado esperado |
|---|---|---|
| 1 | POST `/api/user.json` | HTTP 200 y correo creado en la respuesta. |
| 2 | GET `/api/authentication/token.json` con Basic Auth | HTTP 200 y `TokenString` no vacio. |
| 3 | POST `/api/projects.json` con encabezado `Token` | HTTP 200, nombre correcto y `Deleted=false`. |
| 4 | GET `/api/projects/{id}.json` con token | HTTP 200, mismo id y nombre original. |
| 5 | PUT `/api/projects/{id}.json` con token | HTTP 200 y nombre actualizado. |
| 6 | GET `/api/projects/{id}.json` con token | HTTP 200 y nombre actualizado persistido. |
| 7 | DELETE `/api/projects/{id}.json` con token | HTTP 200 y `Deleted=true`. |

## 4. Arquitectura clean aplicada

- `config`: configuracion por variables de entorno.
- `client`: construccion y envio de peticiones Rest Assured.
- `context`: estado aislado del escenario.
- `steps`: lenguaje de negocio y validaciones Cucumber.
- `features`: especificacion ejecutable en Gherkin.
- `postman`: comprobacion manual equivalente.

Las credenciales del proyecto de referencia no se copiaron. El usuario se genera dinamicamente y el token solo vive en memoria durante la ejecucion.

## 5. Evidencia de ejecucion

Comando ejecutado:

```text
.\gradlew.bat clean cucumber
```

Resultado obtenido el 11 de octubre de 2026:

```text
1 scenario (1 passed)
7 steps (7 passed)
BUILD SUCCESSFUL
```

El proyecto temporal creado durante la validacion fue eliminado correctamente.

## 6. Ejecucion y reporte

Ejecutar `./gradlew clean cucumber` o `.\gradlew.bat clean cucumber`. El reporte HTML queda en `build/reports/cucumber/cucumber.html`.

## 7. Postman

Se incluyen una coleccion y un environment. Al ejecutar la coleccion completa, sus scripts generan el correo, guardan el token y encadenan el id del proyecto sin copiar valores manualmente.

## 8. Repositorio

El codigo y este documento se publican en:

https://github.com/Joseph-Colbert/api-testing-todoly

## 9. Conclusion

El caso demuestra el ciclo completo solicitado, separa autenticacion y operaciones de negocio, evita secretos versionados y deja evidencia reproducible tanto automatizada como manual.

## 10. Referencias

- Todo.ly API Wiki: https://todo.ly/ApiWiki/
- Rest Assured: https://rest-assured.io/
- Cucumber: https://cucumber.io/docs/cucumber/
- Gradle: https://docs.gradle.org/

