# PuenteCultural Frontend

Interfaz web para profesorado que permite generar fichas docentes inclusivas a partir de:
- tema
- materia
- perfil del alumnado

El frontend consume la API del backend en `POST /api/v1/generate` y muestra el resultado en formato Markdown.

## Stack

- React 19 + JavaScript
- Vite
- Tailwind CSS
- Componentes UI ligeros (`class-variance-authority`, `clsx`, `tailwind-merge`)
- Renderizado Markdown con `react-markdown` + `remark-gfm`

## Requisitos

- Node.js 20+
- npm 10+
- Backend de PuenteCultural ejecutándose en `http://127.0.0.1:8000`

## Configuración

1. Instalar dependencias:

```bash
npm install
```

2. Configurar variables de entorno:

```bash
cp .env.example .env
```

Contenido esperado:

```env
VITE_API_URL=http://127.0.0.1:8000
```

## Scripts

- Desarrollo:

```bash
npm run dev
```

- Build de producción:

```bash
npm run build
```

- Previsualizar build:

```bash
npm run preview
```

- Linter:

```bash
npm run lint
```

## Flujo recomendado local

1. Levantar backend en `127.0.0.1:8000`.
2. Levantar frontend:

```bash
npm run dev -- --host 127.0.0.1 --port 5173
```

3. Abrir `http://127.0.0.1:5173`.

## Estructura principal

- `src/App.jsx`: pantalla principal para solicitud docente, resultado y historial.
- `src/api/client.js`: cliente HTTP hacia el backend.
- `src/components/ui/*`: componentes base reutilizables.

## Solución de problemas

- Error de conexión con backend:
  - Verifica que el backend esté activo.
  - Revisa que `VITE_API_URL` apunte al host/puerto correcto.

- Error CORS en navegador:
  - Verifica que el backend tenga habilitado `http://127.0.0.1:5173` y `http://localhost:5173` en CORS.

- `npm run build` falla por tipos/lint:
  - Ejecuta `npm run lint` y corrige los errores reportados.
