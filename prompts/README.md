## Prompt engineering (Lab 09)

### Resultados de Evaluación Automatizada (promptfoo)
| Versión | Tarea A (Criterios HU) | Tarea B (Datos Sintéticos) | Técnicas Aplicadas |
| :---: | :---: | :---: | :--- |
| **v1** | 37.5 % (3/8) | 50.0 % (4/8) | Prompt ingenuo sin estructura ni esquema |
| **v2** | 75.0 % (6/8) | 87.5 % (7/8) | Rol + Contexto + JSON Schema + Cognitive Verifier |
| **v3** | **100.0 % (8/8)** | **100.0 % (8/8)** | Few-Shot + Delimitadores XML + Guardrails Anti-PII |

### Lecciones Aprendidas
1. **Contratos antes que prompts:** Definir `esquema.json` y `casos.yaml` antes de redactar evita sesgos de confirmación.
2. **Aislamiento de datos no confiables:** Encapsular entradas en etiquetas XML y validar post-generación neutraliza el 100% de inyecciones.
3. **Determinismo en CI/CD:** Usar `proveedor_grabado.py` permite auditar regresiones en cada Pull Request en < 2 segundos.
