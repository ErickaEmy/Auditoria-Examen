# Informe de Auditoría de Sistemas - Examen de la Unidad I

**Nombres y apellidos:**  Ericka Esther Martinez Yufra
**Fecha:**  10/09/25
**URL GitHub:**  https://github.com/ErickaEmy/Auditoria-Examen

---

## 1. Proyecto de Auditoría de Riesgos

### Login
**Evidencia:**  
![Captura del login](https://github.com/ErickaEmy/Auditoria-Examen/blob/master/capturas/c1.png)  

**Descripción:**  
El inicio de sesión en tu sistema fue implementado de manera ficticia (sin base de datos ni validación real en el servidor). Para ello:

Se creó un archivo LoginService.js que contiene credenciales predefinidas (usuario: admin, contraseña: 123456).

Cuando el usuario envía sus datos en el formulario (Login.jsx), el servicio compara esos valores con las credenciales almacenadas en memoria.

Si coinciden, se genera un token falso (mock JWT) y se guarda junto con el usuario en el localStorage del navegador, simulando una sesión iniciada.

Si no coinciden, se muestra un mensaje de error en pantalla.

La aplicación principal (App.jsx) consulta al servicio (isAuthenticated()) para saber si hay un token guardado y así decidir si muestra el formulario de login o el sistema de auditoría de riesgos.
---

### Motor de Inteligencia Artificial
**Evidencia:**  
![Captura IA](https://github.com/ErickaEmy/Auditoria-Examen/blob/master/capturas/c2.png)  

**Descripción:**  
En el sistema se implementó un motor de Inteligencia Artificial mediante Flask y la librería openai. El archivo app.py expone dos endpoints:

/analizar-riesgos: recibe un activo tecnológico y retorna cinco posibles riesgos con sus respectivos impactos.

/sugerir-tratamiento: recibe un activo, un riesgo y un impacto, y devuelve un tratamiento recomendado.

El funcionamiento se basa en un cliente de OpenAI conectado a un modelo local de Ollama (ramiro:instruct), el cual interpreta los prompts diseñados en español para la gestión de riesgos ISO 27000. Gracias a este esquema, el sistema puede simular el análisis y tratamiento de riesgos, brindando respuestas dinámicas según el activo ingresado.
![Captura codigo](https://github.com/ErickaEmy/Auditoria-Examen/blob/master/capturas/c3.png) 
![Captura resultados1](https://github.com/ErickaEmy/Auditoria-Examen/blob/master/capturas/c4.png) 
![Captura resultados2](https://github.com/ErickaEmy/Auditoria-Examen/blob/master/capturas/c5.png) 
---

## 2. Hallazgos

### Activo 1: (Título del activo)
- **Evidencia:** ![Captura](ruta/a/la/captura.png)  
- **Condición:** (Situación encontrada en el activo).  
- **Recomendación:** (Acción correctiva o preventiva).  
- **Riesgo:** Probabilidad (Baja/Media/Alta).  

---

### Activo 2: (Título del activo)
- **Evidencia:** ![Captura](ruta/a/la/captura.png)  
- **Condición:**  
- **Recomendación:**  
- **Riesgo:**  

---

### Activo 3: (Título del activo)
- **Evidencia:** ![Captura](ruta/a/la/captura.png)  
- **Condición:**  
- **Recomendación:**  
- **Riesgo:**  

---

### Activo 4: (Título del activo)
- **Evidencia:** ![Captura](ruta/a/la/captura.png)  
- **Condición:**  
- **Recomendación:**  
- **Riesgo:**  

---

### Activo 5: (Título del activo)
- **Evidencia:** ![Captura](ruta/a/la/captura.png)  
- **Condición:**  
- **Recomendación:**  
- **Riesgo:**  

