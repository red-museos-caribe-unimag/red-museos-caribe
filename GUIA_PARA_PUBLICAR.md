# Guía de publicación y comprobación final

Proyecto: Red de Museos del Caribe — Alternativa E.  
Organización: `red-museos-caribe-unimag`.  
Repositorio: `red-museos-caribe`.

## 1. Subir los archivos

1. Descomprimir `Red_Museos_ENTREGA_COMPLETA_GITHUB.zip`.
2. Abrir la carpeta interior `red-museos-caribe`.
3. Seleccionar **su contenido** y arrastrarlo en GitHub a **Add file > Upload files**.
4. Comprobar que `business_logic.py` y `user_interface.py` aparecen directamente en la raíz del repositorio, no dentro de otra carpeta de igual nombre.
5. Guardar el cambio con un commit que describa lo subido. La carga en GitHub aún debe realizarla un integrante con acceso.

## 2. Documentos y resultados incluidos

- `documentacion/Documento_de_Analisis.pdf`: análisis detallado de los 14 requisitos.
- `documentacion/Informe_Integral.pdf`: cinco incrementos y actividades de análisis, diseño, codificación y verificación.
- `documentacion/Informe_del_Uso_de_IA.pdf`: seis fichas de interacción y los enlaces reales de evidencia.
- `resultados_verificacion.md`: ejecución automatizada completa guardada del 22/11/2026, 95 OK de 95 para la versión de código y datos incluida. No se atribuye a un estudiante.
- `evidencias_ia/`: tres archivos de conversación con enlaces compartidos; `video/ENLACE_VIDEO.md`: video aportado por el equipo (14:46).

## 3. Organización de GitHub comunicada por el equipo

Cinco hitos: Incremento 1 (requisitos 1-3), Incremento 2 (4-9), Incremento 3 (10-11), Incremento 4 (12-13), Incremento 5 (14 y verificación final). Ocho tareas diferentes (#1, #2, #3, #4, #5, #7, #8 y #9), más el Issue #6 cerrado como duplicado. Tablero Projects: seis tarjetas en Hecho y dos en En progreso al momento de las capturas. El equipo confirmó que la vista quedó pública.

## 4. Comprobaciones que deben hacer los integrantes

- Ejecutar `python verificar_casos.py` desde la carpeta del proyecto y comparar su salida con los 95 resultados documentados.
- Revisar que todas las afirmaciones sobre conversaciones de IA correspondan al contenido original de los enlaces. El contenido íntegro de Diego y Jesús no está transcrito en los `.md`.
- Revisar los documentos PDF, el video y los enlaces de evidencias en incógnito.
- Cerrar los Issues solo cuando se completen realmente, verificar los porcentajes de los hitos y conservar commits auténticos.
- Comprobar la fecha y hora del campus virtual y entregar el **enlace al repositorio**, no solo el ZIP.

## 5. Nota técnica importante

La función `leer_lineas` aún utiliza `open()/read()/close()` y captura `UnicodeDecodeError`, pero no captura de manera expresa `OSError`. Los informes reflejan ese estado real del código. El documento de análisis se ha reconstruido a partir del código y las pruebas disponibles; contrastarlo con cualquier documento original de Alternativa E que no forme parte del paquete.
