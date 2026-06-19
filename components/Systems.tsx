import { Brain, FileText, ShoppingCart, Workflow, Shield, Code, ExternalLink } from "lucide-react";

const systems = [
  {
    icon: Brain,
    tag: "HERO PROJECT",
    title: "Hermes AI Agent Platform",
    description:
      "A production-grade AI agent ecosystem with 6 MCP servers, 40+ tools, 28+ skills, persistent memory, and async subagent orchestration.",
    metrics: ["6 MCP Servers", "40+ Tools", "28+ Skills", "Persistent Memory"],
    link: "https://github.com/Koslovski79/hermes-agent-framework",
  },
  {
    icon: FileText,
    tag: "PRODUCTION",
    title: "Payroll Platform",
    description:
      "SARS-compliant payroll system for South African SMEs. 9 Django apps, 7,100+ LOC, WhatsApp integration for payslip delivery.",
    metrics: ["7,100+ LOC", "9 Django Apps", "SARS Compliant", "WhatsApp Integration"],
    link: "https://github.com/Koslovski79/seagulls-payroll",
  },
  {
    icon: ShoppingCart,
    tag: "PRODUCTION",
    title: "POS Platform",
    description:
      "Full-stack restaurant POS with reservations, inventory, and reporting. 46 Django models, 3,600+ LOC, deployed and serving live transactions.",
    metrics: ["3,600+ LOC", "46 Models", "Reservations", "Inventory"],
    link: "https://github.com/Koslovski79/seagulls-pos",
  },
  {
    icon: Workflow,
    tag: "SELF-HOSTED",
    title: "N8N Automation Engine",
    description:
      "Self-hosted n8n instance with local LLM integration, recon pipelines, and threat intelligence workflows. Orchestrates multi-step automations across services.",
    metrics: ["Self-Hosted", "Local LLMs", "Recon Pipelines", "Multi-Step"],
    link: null,
  },
  {
    icon: Shield,
    tag: "RESEARCH",
    title: "AI Security Automation",
    description:
      "64+ MCP tools with Caido integration, GraphQL API testing, and prompt-driven security testing methodology.",
    metrics: ["64+ MCP Tools", "Caido Integration", "GraphQL APIs", "Prompt-Driven"],
    link: null,
  },
  {
    icon: Code,
    tag: "AI-ASSISTED",
    title: "Claude Code Workflows",
    description:
      "AI-assisted development workflows using Claude Code, MCP architecture, and custom skill systems. The tool I use to build everything else.",
    metrics: ["Claude Code", "MCP Architecture", "Custom Skills", "AI-First Dev"],
    link: "https://github.com/Koslovski79",
  },
];

export default function Systems() {
  return (
    <section id="systems" className="py-24 md:py-32">
      <p className="text-violet-400 font-medium tracking-wide text-sm uppercase mb-2">
        Systems I&apos;ve Built
      </p>
      <h2 className="text-3xl md:text-4xl font-bold text-slate-100 mb-12">
        Production tools, not toy projects.
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {systems.map((s) => {
          const Icon = s.icon;
          return (
            <div
              key={s.title}
              className="group bg-slate-900 border border-slate-800 rounded-xl p-6 hover:border-violet-500/50 transition-colors flex flex-col"
            >
              <div className="flex items-center justify-between mb-4">
                <Icon className="w-6 h-6 text-violet-400" />
                <span className="text-[10px] font-semibold tracking-wider text-slate-500 uppercase">
                  {s.tag}
                </span>
              </div>
              <h3 className="text-lg font-bold text-slate-100 mb-2">{s.title}</h3>
              <p className="text-sm text-slate-400 leading-relaxed mb-4 flex-1">
                {s.description}
              </p>
              <div className="flex flex-wrap gap-2 mb-4">
                {s.metrics.map((m) => (
                  <span
                    key={m}
                    className="text-xs bg-slate-800 text-slate-300 px-2 py-1 rounded-full"
                  >
                    {m}
                  </span>
                ))}
              </div>
              {s.link && (
                <a
                  href={s.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1 text-sm text-violet-400 hover:text-violet-300 font-medium mt-auto"
                >
                  View on GitHub
                  <ExternalLink className="w-3 h-3" />
                </a>
              )}
            </div>
          );
        })}
      </div>
    </section>
  );
}
