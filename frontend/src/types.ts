export type Materia = 'Historia' | 'Literatura' | 'Ingles'

export interface GeneratePayload {
    tema: string
    materia: Materia
    perfil_alumnos: string
}

export interface GenerateResponse {
    resultado: string
}

export interface TeacherDraft {
    tema: string
    materia: Materia
    perfil_alumnos: string
}
