# language: es
@e2e @regression @projects
Característica: Gestionar proyectos de Todo.ly con autenticacion por token
  Como responsable de calidad
  Quiero automatizar el ciclo de vida de un proyecto
  Para comprobar que el API protege y procesa correctamente sus recursos

  Escenario: Crear, consultar, actualizar y eliminar un proyecto con un usuario nuevo
    Dado un usuario nuevo registrado en Todo.ly
    Y obtengo el token de autenticacion del usuario
    Cuando creo un proyecto llamado "Proyecto API Clean" usando el token
    Entonces puedo consultar el proyecto "Proyecto API Clean" usando el token
    Cuando actualizo el proyecto a "Proyecto API Clean Actualizado" usando el token
    Entonces puedo consultar el proyecto "Proyecto API Clean Actualizado" usando el token
    Y elimino el proyecto usando el token

