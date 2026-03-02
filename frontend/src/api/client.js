// En desarrollo usamos el servidor local de python, en producción usamos rutas relativas
// para evitar problemas con variables mal configuradas en DigitalOcean.
const isDev = import.meta.env.DEV
const API_BASE_URL = isDev ? 'http://127.0.0.1:8000' : ''

export async function generateGuide(payload) {
    const url = `${API_BASE_URL}/api/v1/generate`

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
    })

    if (!response.ok) {
        const text = await response.text()
        throw new Error(text || 'No fue posible generar la ficha docente.')
    }

    return response.json()
}
