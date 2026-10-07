# Reporte de Comparación Round-Trip (Lab 05)

| Diferencia Observada | Causa | Acción Tomada |
| :--- | :--- | :--- |
| Las asociaciones de agregado/composición no se grafican en pyreverse. | Pyreverse procesa atributos simples pero no deduce relaciones agregadas explícitas de referencias indirectas de UUIDs. | Aceptable por limitaciones conocidas del analizador estático en Python. Se conserva la estructura en `clases.puml`. |
| Nombres traducidos a `snake_case` (`fecha_hora`) respecto a `camelCase` (`fechaHora`) de UML. | Convención estándar PEP 8 aplicada en el código de Python. | Documentar la equivalencia (Cumple regla C5). |
| `NotificadorSMS` y `RepositorioCitas` aparecen como clases abstractas (`ABC`) en lugar de estereotipo `<<puerto>>`. | Python no posee la palabra clave `interface`; usa clases abstractas con el módulo `abc`. | Aceptable en la implementación orientada a objetos en Python. |
