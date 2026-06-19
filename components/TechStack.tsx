const groups = [
  {
    label: "AI & Agents",
    tags: [
      "Claude Code",
      "MCP",
      "Hermes",
      "OpenRouter",
      "Ollama",
      "Prompt Engineering",
      "Local LLMs",
      "Agentic Workflows",
    ],
  },
  {
    label: "Automation",
    tags: ["n8n", "Make", "Webhooks", "REST APIs", "GraphQL", "Workflow Orchestration"],
  },
  {
    label: "Development",
    tags: ["Python", "Django", "PostgreSQL", "Docker", "Linux", "Git", "FastAPI"],
  },
  {
    label: "Infrastructure",
    tags: ["Vercel", "Tailwind CSS", "Next.js", "Redis", "Qdrant"],
  },
];

export default function TechStack() {
  return (
    <section id="stack" className="py-24 md:py-32">
      <p className="text-violet-400 font-medium tracking-wide text-sm uppercase mb-2">
        Tech Stack
      </p>
      <h2 className="text-3xl md:text-4xl font-bold text-slate-100 mb-12">
        Tools I use to build.
      </h2>

      <div className="space-y-8">
        {groups.map((group) => (
          <div key={group.label}>
            <h3 className="text-sm font-semibold text-slate-500 uppercase tracking-wider mb-3">
              {group.label}
            </h3>
            <div className="flex flex-wrap gap-2">
              {group.tags.map((tag) => (
                <span
                  key={tag}
                  className="text-sm bg-slate-800 text-slate-300 px-3 py-1 rounded-full"
                >
                  {tag}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
