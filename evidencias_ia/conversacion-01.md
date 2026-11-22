# Conversación 01 con la IA

- **Integrante:** Leandro García
- **Herramienta:** Claude (Anthropic), aplicación claude.ai
- **Período general de evidencias indicado por el equipo:** del jueves 19 al domingo 22 de noviembre de 2026
- **Interacciones que respalda:** IA-01 a IA-10 del informe del uso de la IA

## Evidencia

**Enlace compartido de la conversación:** https://claude.ai/share/609c378e-b01d-45ef-92ae-15b0b98c15c2

**Texto completo exportado:** No incluido en este archivo. La evidencia se aporta mediante el enlace compartido; consultar allí la conversación completa.

> El equipo confirmó que este enlace puede abrirse sin iniciar sesión y muestra la conversación. Fecha declarada por el equipo: jueves 19 de noviembre de 2026.

## Registro resumido (ayuda para ubicarse; no reemplaza la exportación)

Los mensajes del integrante están tomados de la conversación. Las respuestas de la IA están resumidas.

### IA-01 · Inicio
- **Integrante:** «Necesito ayuda con un proyecto de programación».
- **IA:** preguntó de qué trataba, en qué lenguaje y qué necesitaba (código desde cero, corregir, revisar o plantear).

### IA-02 · Lectura del código de ejemplo
- **Integrante:** subió `proyecto_lanchas_incrementos_1_a_6.zip` y dijo «Tengo este código de ejemplo».
- **IA:** leyó `business_logic.py`, `user_interface.py` y los casos del ejemplo, y resumió la estructura y los patrones que se repiten.

### IA-03 · Propuesta de código para la Alternativa E
- **Integrante:** subió los términos de referencia y el documento de la Alternativa E, y pidió un código parecido al ejemplo pero no igual, que funcione y cumpla los términos.
- **IA:** entregó `red-museos-caribe.zip` con `business_logic.py`, `user_interface.py`, los CSV de prueba y un documento de casos. Lo probó con los ejemplos del enunciado.

### IA-04 · Revisión de lo que faltaba
- **Integrante:** subió los archivos del proyecto y preguntó qué le faltaba.
- **IA:** ejecutó el programa, confirmó los ejemplos del enunciado y reportó cuatro hallazgos: cierre en el año 9999, enteros con guion bajo, type hints y constantes que tenía el ejemplo, y archivos `.pyc` en el paquete. Listó los casos que faltaban y los productos pendientes de la entrega.

### IA-05 · Corrección y verificador ejecutable
- **Integrante:** pidió ayuda para arreglar lo encontrado y completar los casos.
- **IA:** corrigió `convertir_a_entero`, agregó `hay_fechas_para`, creó `verificar_casos.py` con 95 casos, y entregó `red-museos-caribe-v2.zip`. Contra el código anterior fallaban 9 casos; contra el corregido pasan los 95.

### IA-06 · Documento de análisis
- **Integrante:** pidió los documentos que exigen los términos.
- **IA:** redactó el documento de análisis con los 14 requisitos y, más tarde, actualizó su sección 6 con las decisiones tomadas.

### IA-07 · Informe integral e informe del uso de la IA
- **Integrante:** pidió el informe integral y el informe del uso de la IA.
- **IA:** redactó los dos borradores, con el diagrama de clases y los algoritmos, y marcó entre corchetes lo que el equipo debía completar.

### IA-08 · Incrementos y casos por incremento
- **Integrante:** pidió los incrementos.
- **IA:** preparó el plan de incrementos y entregó `red-museos-caribe-v3.zip`, con un documento de casos por incremento y `verificar_casos.py --incremento N`. Los 95 casos pasan por incremento y en conjunto.

### IA-09 · Ajuste de los documentos
- **Integrante:** pidió pasar los informes a cinco incrementos, dio los nombres del equipo y la fecha de entrega (23 de noviembre de 2026).
- **IA:** actualizó el informe integral, el informe del uso de la IA, el plan de incrementos y el documento de análisis.

### IA-10 · Presentación del código
- **Integrante:** pidió una presentación con varias diapositivas que expliquen las partes más importantes del código.
- **IA:** creó una presentación de 7 diapositivas con notas del orador.
