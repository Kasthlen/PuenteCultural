import { cn } from '../../lib/utils'

export function Textarea({ className, ...props }) {
    return (
        <textarea
            className={cn(
                'w-full min-h-28 rounded-xl border border-slate-300 bg-white px-3 py-2 text-sm text-slate-900 placeholder:text-slate-400 focus:border-emerald-500 focus:outline-none focus:ring-2 focus:ring-emerald-200',
                className,
            )}
            {...props}
        />
    )
}
