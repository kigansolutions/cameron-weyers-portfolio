import { Terminal, Globe, Mail } from "lucide-react";

const links = [
  {
    icon: Terminal,
    label: "GitHub",
    href: "https://github.com/Koslovski79",
    handle: "@Koslovski79",
  },
  {
    icon: Globe,
    label: "LinkedIn",
    href: "https://www.linkedin.com/in/cameron-weyers-132a074b",
    handle: "Cameron Weyers",
  },
  {
    icon: Mail,
    label: "Email",
    href: "mailto:cameron@cameronweyers.io",
    handle: "cameron@cameronweyers.io",
  },
];

export default function Contact() {
  return (
    <section id="contact" className="py-24 md:py-32">
      <p className="text-violet-400 font-medium tracking-wide text-sm uppercase mb-2">
        Contact
      </p>
      <h2 className="text-3xl md:text-4xl font-bold text-slate-100 mb-12">
        Let&apos;s talk.
      </h2>

      <div className="space-y-4 max-w-md">
        {links.map((link) => {
          const Icon = link.icon;
          return (
            <a
              key={link.label}
              href={link.href}
              target={link.href.startsWith("mailto") ? undefined : "_blank"}
              rel={link.href.startsWith("mailto") ? undefined : "noopener noreferrer"}
              className="flex items-center gap-4 p-4 bg-slate-900 border border-slate-800 rounded-xl hover:border-violet-500/50 transition-colors group"
            >
              <Icon className="w-5 h-5 text-violet-400" />
              <div>
                <p className="text-sm font-semibold text-slate-100">{link.label}</p>
                <p className="text-sm text-slate-500 group-hover:text-slate-400 transition-colors">
                  {link.handle}
                </p>
              </div>
            </a>
          );
        })}
      </div>

      <footer className="mt-20 pt-8 border-t border-slate-800 text-sm text-slate-600">
        © 2026 Cameron Weyers. Built with Claude Code and Next.js.
      </footer>
    </section>
  );
}
