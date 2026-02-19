import { useMemo, useState } from 'react'
import { BookOpenCheck, ClipboardCheck, LoaderCircle, Sparkles } from 'lucide-react'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'

import { generateGuide } from './api/client'
import { Button } from './components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './components/ui/card'
import { Input } from './components/ui/input'
import { Textarea } from './components/ui/textarea'

const quickTopics = [
  'La Guerra Civil Española',
  'La Generación del 27',
  'Present Perfect vs Past Simple',
]

const quickProfiles = [
  'Mayoría de estudiantes de Colombia y Venezuela',
  'Grupo mixto con alumnado de Marruecos, Perú y Rumanía',
  'Clase de recién llegados con nivel intermedio de español',
]

function App() {
  const [draft, setDraft] = useState({
    tema: quickTopics[0],
    materia: 'Historia',
    perfil_alumnos: quickProfiles[0],
  })
  const [loading, setLoading] = useState(false)
  const [resultado, setResultado] = useState('')
  const [error, setError] = useState('')
  const [lastPayload, setLastPayload] = useState(null)
  const [history, setHistory] = useState([])

  const canSubmit = useMemo(
    () => draft.tema.trim().length >= 3 && draft.perfil_alumnos.trim().length >= 5,
    [draft],
  )

  const updateField = (key, value) => {
    setDraft((prev) => ({ ...prev, [key]: value }))
  }

  const normalizeError = (message) => {
    try {
      const parsed = JSON.parse(message)
      if (parsed?.detail) return String(parsed.detail)
      return message
    } catch {
      return message
    }
  }

  const onGenerate = async () => {
    setLoading(true)
    setError('')
    setResultado('')

    const payload = {
      tema: draft.tema.trim(),
      materia: draft.materia,
      perfil_alumnos: draft.perfil_alumnos.trim(),
    }

    try {
      const data = await generateGuide(payload)
      setResultado(data.resultado)
      setLastPayload(payload)
      setHistory((prev) => [payload, ...prev].slice(0, 5))
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Ocurrió un error inesperado.'
      setError(normalizeError(message))
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="min-h-screen bg-slate-50 text-slate-900">
      <section className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <header className="mb-6 rounded-2xl bg-gradient-to-r from-brand-700 to-brand-500 p-6 text-white shadow-sm">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div>
              <p className="text-sm font-medium text-emerald-100">PuenteCultural · Plataforma Docente IA</p>
              <h1 className="mt-1 text-2xl font-bold sm:text-3xl">Generador de Fichas Inclusivas</h1>
              <p className="mt-2 max-w-3xl text-sm text-emerald-50">
                Diseñado para profesorado: plantea el tema, el perfil del aula y obtén una guía lista para clase.
              </p>
            </div>
            <div className="rounded-xl bg-white/15 px-4 py-2 text-sm">
              <span className="inline-flex items-center gap-2">
                <Sparkles size={16} />
                Backend IA conectado
              </span>
            </div>
          </div>
        </header>

        <div className="grid gap-6 lg:grid-cols-[420px,1fr]">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <BookOpenCheck size={18} />
                Solicitud Docente
              </CardTitle>
              <CardDescription>Completa estos campos para generar una ficha contextualizada.</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="space-y-2">
                <label className="text-sm font-medium text-slate-700" htmlFor="tema">
                  Tema
                </label>
                <Input
                  id="tema"
                  value={draft.tema}
                  placeholder="Ej: La Guerra Civil Española"
                  onChange={(e) => updateField('tema', e.target.value)}
                />
              </div>

              <div className="space-y-2">
                <label className="text-sm font-medium text-slate-700" htmlFor="materia">
                  Materia
                </label>
                <select
                  id="materia"
                  className="w-full rounded-xl border border-slate-300 bg-white px-3 py-2 text-sm focus:border-brand-500 focus:outline-none focus:ring-2 focus:ring-brand-100"
                  value={draft.materia}
                  onChange={(e) => updateField('materia', e.target.value)}
                >
                  <option>Historia</option>
                  <option>Literatura</option>
                  <option>Ingles</option>
                </select>
              </div>

              <div className="space-y-2">
                <label className="text-sm font-medium text-slate-700" htmlFor="perfil">
                  Perfil del alumnado
                </label>
                <Textarea
                  id="perfil"
                  value={draft.perfil_alumnos}
                  onChange={(e) => updateField('perfil_alumnos', e.target.value)}
                  placeholder="Describe origen cultural, nivel de idioma, necesidades específicas..."
                />
              </div>

              <div className="rounded-xl border border-slate-200 bg-slate-50 p-3">
                <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-slate-500">Sugerencias rápidas</p>
                <div className="flex flex-wrap gap-2">
                  {quickTopics.map((topic) => (
                    <button
                      key={topic}
                      className="rounded-full border border-slate-200 bg-white px-3 py-1 text-xs text-slate-700 hover:bg-slate-100"
                      onClick={() => updateField('tema', topic)}
                      type="button"
                    >
                      {topic}
                    </button>
                  ))}
                  {quickProfiles.map((profile) => (
                    <button
                      key={profile}
                      className="rounded-full border border-slate-200 bg-white px-3 py-1 text-xs text-slate-700 hover:bg-slate-100"
                      onClick={() => updateField('perfil_alumnos', profile)}
                      type="button"
                    >
                      Perfil ejemplo
                    </button>
                  ))}
                </div>
              </div>

              <Button className="w-full" disabled={!canSubmit || loading} onClick={onGenerate}>
                {loading ? (
                  <span className="inline-flex items-center gap-2">
                    <LoaderCircle className="animate-spin" size={16} />
                    Generando ficha...
                  </span>
                ) : (
                  'Generar ficha docente'
                )}
              </Button>

              {error ? <p className="rounded-xl bg-red-50 px-3 py-2 text-sm text-red-700">{error}</p> : null}
            </CardContent>
          </Card>

          <div className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <ClipboardCheck size={18} />
                  Resultado listo para clase
                </CardTitle>
                <CardDescription>
                  Formato markdown para revisión rápida, copia y adaptación pedagógica final.
                </CardDescription>
              </CardHeader>
              <CardContent>
                {resultado ? (
                  <div className="space-y-4">
                    <div className="md-output max-h-[60vh] overflow-auto rounded-xl border border-slate-200 bg-white p-4">
                      <ReactMarkdown remarkPlugins={[remarkGfm]}>{resultado}</ReactMarkdown>
                    </div>
                    <div className="flex flex-wrap gap-2">
                      <Button
                        variant="secondary"
                        onClick={async () => {
                          await navigator.clipboard.writeText(resultado)
                        }}
                      >
                        Copiar resultado
                      </Button>
                      {lastPayload ? (
                        <p className="text-xs text-slate-500">
                          Última ejecución: {lastPayload.materia} · {lastPayload.tema}
                        </p>
                      ) : null}
                    </div>
                  </div>
                ) : (
                  <p className="rounded-xl border border-dashed border-slate-300 bg-slate-50 px-4 py-8 text-center text-sm text-slate-500">
                    Todavía no hay resultado. Completa el formulario y genera tu primera ficha.
                  </p>
                )}
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>Historial rápido</CardTitle>
                <CardDescription>Últimas solicitudes para repetir o ajustar una guía.</CardDescription>
              </CardHeader>
              <CardContent>
                {history.length === 0 ? (
                  <p className="text-sm text-slate-500">Aún no hay solicitudes guardadas en esta sesión.</p>
                ) : (
                  <ul className="space-y-2">
                    {history.map((item, index) => (
                      <li className="rounded-xl border border-slate-200 bg-slate-50 p-3" key={`${item.tema}-${index}`}>
                        <p className="text-sm font-semibold text-slate-800">{item.tema}</p>
                        <p className="text-xs text-slate-500">{item.materia}</p>
                      </li>
                    ))}
                  </ul>
                )}
              </CardContent>
            </Card>
          </div>
        </div>
      </section>
    </main>
  )
}

export default App
