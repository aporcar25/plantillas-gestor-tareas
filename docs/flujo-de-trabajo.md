# Flujo de trabajo (GitFlow)

Este documento explica cómo trabaja el equipo en el repositorio.

## Ramas

| Rama | Función |
|---|---|
| `main` | Versión estable. Solo recibe cambios desde `develop`. |
| `develop` | Rama de integración donde se juntan las tareas terminadas. |
| `feature/*` | Una rama por cada nueva funcionalidad o mejora. |
| `hotfix/*` | Una rama por cada corrección de error. |

## Ciclo de trabajo

1. Se registra la tarea como Issue y se asigna a un integrante.
2. El responsable crea su rama desde `develop`.
3. Realiza los cambios, los prueba y hace commits con mensajes claros.
4. Sube la rama y abre un Pull Request hacia `develop` con la plantilla completa.
5. Otro integrante revisa el PR y lo aprueba o pide cambios.
6. Tras la aprobación, se hace el merge a `develop`.
7. Al terminar todas las tareas, se abre un PR de `develop` a `main`, que también se revisa.

## Normas de trabajo colaborativo

- Cada integrante utiliza su propia cuenta de GitHub.
- Todas las modificaciones se hacen en ramas independientes.
- Nadie hace commits directamente en `main` ni en `develop`.
- Cada tarea está documentada mediante una Issue.
- Los Pull Requests incluyen toda la información de la plantilla.
- Nadie revisa ni aprueba sus propios cambios.
- Todos los integrantes desarrollan cambios y revisan el trabajo de sus compañeros.
- Las observaciones y decisiones sobre los cambios se registran en GitHub.
- Los cambios se revisan antes de incorporarse a la rama principal.

## Mensajes de commit

Formato: `tipo: descripción breve (#número de issue)`

| Tipo | Uso |
|---|---|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de un error |
| `docs` | Cambios en la documentación |
| `chore` | Tareas de mantenimiento |