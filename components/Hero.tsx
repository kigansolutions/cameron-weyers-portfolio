import { ArrowDown, ExternalLink } from "lucide-react";

export default function Hero() {
  return (
    <section className="min-h-screen flex flex-col justify-center items-center text-center py-24 md:py-32">
      <p className="text-violet-400 font-medium tracking-wide text-sm uppercase mb-4">
        AI Systems Architect
      </p>
      <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight text-slate-100">
        Cameron Weyers
      </h1>
      <h2 className="text-xl md:text-2xl text-slate-400 font-medium mt-4 max-w-2xl">
        I architect AI systems that run in production.
      </h2>

      <div className="flex flex-wrap justify-center gap-4 md:gap-8 mt-10">
        <div className="flex flex-col items-center">
          <span className="text-2xl md:text-3xl font-bold text-emerald-400">3</span>
          <span className="text-xs md:text-sm text-slate-500 mt-1">Production Systems</span>
        </div>
        <div className="flex flex-col items-center">
          <span className="text-2xl md:text-3xl font-bold text-emerald-400">10,700+</span>
          <span className="text-xs md:text-sm text-slate-500 mt-1">LOC Shipped</span>
        </div>
        <div className="flex flex-col items-center">
          <span className="text-2xl md:text-3xl font-bold text-emerald-400">6</span>
          <span className="text-xs md:text-sm text-slate-500 mt-1">MCP Servers</span>
        </div>
      </div>

      <div className="flex flex-col sm:flex-row gap-4 mt-12">
        <a
          href="#systems"
          className="inline-flex items-center gap-2 px-6 py-3 bg-violet-500 hover:bg-violet-400 text-white font-semibold rounded-lg transition-colors"
        >
          View My Work
          <ArrowDown className="w-4 h-4" />
        </a>
        <a
          href="#contact"
          className="inline-flex items-center gap-2 px-6 py-3 border border-slate-700 hover:border-slate-500 text-slate-300 font-semibold rounded-lg transition-colors"
        >
          Get in Touch
          <ExternalLink className="w-4 h-4" />
        </a>
      </div>
    </section>
  );
}
