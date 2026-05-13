# Correcciones

**Integrantes:**
- Frankin Libreros Morales  
- Lina Peréz Henao  
- Daniel Eduardo Mejía  

---

## Error 1
- **Archivo:** app.py  
- **Problema:** El endpoint `/` devolvía `"status": "ok"` pero los tests esperaban `"running"`.  
- **Solución:** Se ajustó el valor de retorno para cumplir con las pruebas del pipeline (`status` esperado en test_app.py).

---

## Error 2
- **Archivo:** app.py  
- **Problema:** El endpoint `/health` no incluía el campo `uptime_seconds` requerido por los tests.  
- **Solución:** Se agregó cálculo de uptime usando `time.time()` y se incluyó en la respuesta como `uptime_seconds`.

---

## Error 3
- **Archivo:** app.py  
- **Problema:** El endpoint `/metrics` no tenía el Content-Type correcto para Prometheus.  
- **Solución:** Se forzó el header `"Content-Type": "text/plain"` para que Prometheus pueda scrapear correctamente.

---

## Error 4
- **Archivo:** app.py  
- **Problema:** El endpoint `/metrics` inicialmente devolvía formato incorrecto (Flask lo interpretaba como HTML).  
- **Solución:** Se ajustó el retorno a formato Prometheus válido (texto plano estructurado con HELP y TYPE).

---

## Error 5
- **Archivo:** test_app.py  
- **Problema:** Inconsistencia entre tests y API (esperaban campos y valores diferentes a los implementados inicialmente).  
- **Solución:** Se corrigieron las aserciones para alinearlas con la API real:  
  - `/` → status `"running"`  
  - `/health` → `uptime_seconds` presente  
  - `/metrics` → contiene `app_cpu_percent`

---

## Error 6
- **Archivo:** prometheus.yml  
- **Problema:** Prometheus no estaba apuntando correctamente al servicio dentro de Docker (uso incorrecto de localhost o endpoint mal definido).  
- **Solución:** Se configuró correctamente el target como `api:5000` usando el nombre del servicio Docker Compose.

---

## Error 7
- **Archivo:** docker-compose.yml  
- **Problema:** Los servicios no estaban correctamente enlazados entre API y Prometheus.  
- **Solución:** Se ajustaron los nombres de servicios para permitir comunicación interna por DNS de Docker (`api` como hostname).

---

## Error 8
- **Archivo:** Docker / Puertos  
- **Problema:** Conflicto de puerto 5000 en el host debido a servicios locales (Flask/Docker/WSL).  
- **Solución:** Se cambió el mapeo de puertos a `5001:5000` para evitar colisión.

---

## Error 9
- **Archivo:** CI/CD Pipeline (`.github/workflows/ci.yml`)  
- **Problema:** Los tests podían fallar si pytest no estaba instalado explícitamente en el runner.  
- **Solución:** Se agregó instalación de pytest en el step de dependencias.

---

## Error 10
- **Archivo:** CI/CD Pipeline (`.github/workflows/ci.yml`)  
- **Problema:** Los tests de endpoints no fallaban correctamente si el servicio no respondía (curl sin validación).  
- **Solución:** Se agregó `curl -f` para asegurar que el pipeline falle si el endpoint no responde correctamente.

---

## Error 11
- **Archivo:** CI/CD Pipeline (`.github/workflows/ci.yml`)  
- **Problema:** El contenedor podía no iniciar completamente antes de ejecutar tests.  
- **Solución:** Se aumentó el `sleep` y se estabilizó el arranque del contenedor antes de ejecutar validaciones.

---

## Resultado final

- Todos los endpoints funcionando correctamente  
- Tests unitarios pasando  
- Docker Compose operativo  
- Prometheus en estado **UP**  
- Pipeline CI/CD ejecutándose correctamente en GitHub Actions  

---

## Estado final del proyecto

✔ API REST funcional  
✔ Métricas compatibles con Prometheus  
✔ Infraestructura Docker correcta  
✔ Pipeline CI/CD en verde  
✔ Entrega lista