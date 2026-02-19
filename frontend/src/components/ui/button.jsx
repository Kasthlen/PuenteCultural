import { cva } from 'class-variance-authority'

import { cn } from '../../lib/utils'

const buttonVariants = cva(
    'inline-flex items-center justify-center rounded-xl px-4 py-2 text-sm font-semibold transition focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
    {
        variants: {
            variant: {
                primary: 'bg-emerald-600 text-white hover:bg-emerald-700',
                secondary: 'bg-slate-100 text-slate-800 hover:bg-slate-200',
                ghost: 'bg-transparent text-slate-700 hover:bg-slate-100',
            },
        },
        defaultVariants: {
            variant: 'primary',
        },
    },
)

export function Button({ className, variant, ...props }) {
    return <button className={cn(buttonVariants({ variant }), className)} {...props} />
}
