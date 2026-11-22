# Red de Museos del Caribe — Alternativa E

Proyecto de Fundamentos de Programación, Universidad del Magdalena. Equipo: Leandro García, Diego Mejía y Jesús Jiménez.

## Código y ejecución

Sistema de consola en Python para crear museos, registrar y simular visitantes, generar informes, comparar museos y cargar archivos CSV.

- `business_logic.py`: reglas y cálculos de las clases `Museo` y `RedDeMuseos`.
- `user_interface.py`: menú y entrada/salida del programa.
- `datos/`: archivos CSV de ejemplo y de prueba.
- `verificar_casos.py`: ejecuta los casos de verificación.
- `casos_de_verificacion_incremento_1.md` hasta `casos_de_verificacion_incremento_5.md`: casos por incremento.
- `evidencias_ia/`: enlaces a las conversaciones de los integrantes con IA (período indicado por el equipo: 19 al 22 de noviembre de 2026).
- `video/ENLACE_VIDEO.md`: enlace al video del proyecto.

No se necesitan dependencias externas: basta con Python 3.

Desde la carpeta raíz del proyecto:

```bash
python user_interface.py
```

Para ejecutar todas las verificaciones:

```bash
python verificar_casos.py
```

También se pueden ejecutar los casos de un incremento: `python verificar_casos.py --incremento 1` (cambiando el número entre 1 y 5). El verificador genera `resultados_verificacion.md`; antes de entregar, ejecutarlo y revisar los resultados.

Para probar la opción 6 (archivos CSV): `datos/museos.csv` y `datos/visitantes.csv`.

## Video explicativo

[Ver video en YouTube](https://youtu.be/X3JT-Q_iUZs?si=FN4ytb5Qx00YbDII)

**Duración: 14 minutos y 46 segundos (14:46).** Según lo confirmado por el equipo, los tres integrantes aparecen en cámara y el video se reproduce sin iniciar sesión. Estos datos fueron reportados por el equipo y no se verificaron independientemente aquí.

## Documentación final incorporada

Se incorporaron los tres informes del trabajo en `documentacion/`: `Documento_de_Analisis.pdf`, `Informe_Integral.pdf` e `Informe_del_Uso_de_IA.pdf`.

La ejecución completa de la versión de código y datos conservada registró **95 casos, 95 OK y 0 fallas** el 22 de noviembre de 2026. El registro detallado se incluye en `resultados_verificacion.md`. No se atribuye esa ejecución a un integrante. El equipo debe contrastar la documentación con su revisión final.

## Material pendiente para la entrega final

**Este repositorio no está completo todavía.** Antes del plazo deben añadirse:

- Los tres documentos de `documentacion/` ya se incluyen. Revisar la versión final antes de entregar.
- El equipo confirmó acceso público al video, duración de **14:46** y aparición en cámara de los **tres integrantes**; ya no figura como pendiente por esos motivos.
- Registro auténtico de trabajo colaborativo en GitHub: milestones, issues, project y commits de cada integrante.
- El equipo confirmó acceso sin cuenta a las conversaciones e indicó como período general **19 al 22 de noviembre de 2026**. Completar las referencias precisas a las interacciones en el informe de IA.
- `resultados_verificacion.md` ya se incluye como evidencia de ejecución automatizada. Se recomienda que el equipo lo reproduzca en su computador y confirme los resultados.

Los documentos de análisis, informe integral e informe de IA **sí están** incluidos en este paquete. El video está alojado en YouTube y se incluye su enlace, no el archivo de video.

## Nota sobre versiones

Estos archivos Python son la versión más reciente localizada entre los archivos del proyecto aportados por los estudiantes y contienen las validaciones para los casos de borde. No deben mezclarse con la copia más antigua del archivo `red-museos-caribe_proyecto (1).zip`.

El archivo `datos/visitantes_vacias.csv` se creó como dato auxiliar de prueba para el caso A16; no contiene datos personales.

## Material de apoyo para la presentación

- `documentacion/Presentacion_Arquitectura_del_Codigo.pptx`: presentación complementaria, no exigida de forma independiente en los términos de referencia. Se ajustaron los nombres de atributos y métodos para coincidir con el código de esta entrega.
