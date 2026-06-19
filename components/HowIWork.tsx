import { Search, Layout, Wrench, Cpu, CheckCircle, Rocket } from "lucide-react";

const steps = [
  { icon: Search, label: "Identify Problem" },
  { icon: Layout, label: "Design Architecture" },
  { icon: Wrench, label: "Select Tools" },
  { icon: Cpu, label: "AI Implements" },
  { icon: CheckCircle, label: "I Review" },
  { icon: Rocket, label: "Ship to Production" },
];

export default function HowIWork() {
  return (
    <section id="how" className="py-24 md:py-32">
      <p className="text-violet-400 font-medium tracking-wide text-sm uppercase mb-2">
        How I Work
      </p>
      <h2 className="text-3xl md:text-4xl font-bold text-slate-100 mb-12">
        Architecture is mine. Implementation is AI-accelerated.
      </h2>

      {/* Workflow diagram */}
      <div className="flex flex-col md:flex-row items-center justify-center gap-2 md:gap-0 mb-16">
        {steps.map((step, i) => {
          const Icon = step.icon;
          return (
            <div key={step.label} className="flex items-center">
              <div className="flex flex-col items-center gap-2 px-3">
                <div className="w-12 h-12 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center">
                  <Icon className="w-5 h-5 text-violet-400" />
                </div>
                <span className="text-xs text-slate-400 text-center whitespace-nowrap">
                  {step.label}
                </span>
              </div>
              {i < steps.length - 1 && (
                <span className="text-slate-600 text-xl mx-1 hidden md:block">→</span>
              )}
              {i < steps.length - 1 && (
                <span className="text-slate-600 text-xl md:hidden">↓</span>
              )}
            </div>
          );
        })}
      </div>

      {/* Three columns */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div>
          <h3 className="text-lg font-bold text-emerald-400 mb-3">I Own</h3>
          <ul className="space-y-2 text-sm text-slate-400">
            <li>• System design & architecture decisions</li>
            <li>• Tool and technology selection</li>
            <li>• Problem decomposition</li>
            <li>• Quality judgement & troubleshooting</li>
            <li>• Operational ownership</li>
          </ul>
        </div>
        <div>
          <h3 className="text-lg font-bold text-violet-400 mb-3">AI Owns</h3>
          <ul className="space-y-2 text-sm text-slate-400">
            <li>• Implementation detail</li>
            <li>• Boilerplate & refactors</li>
            <li>• Documentation generation</li>
            <li>• Research synthesis</li>
            <li>• Pattern matching at scale</li>
          </ul>
        </div>
        <div>
          <h3 className="text-lg font-bold text-slate-100 mb-3">Result</h3>
          <ul className="space-y-2 text-sm text-slate-400">
            <li>• Production systems shipped faster</li>
            <li>• Fewer bugs through AI-assisted review</li>
            <li>• Fraction of traditional development cost</li>
            <li>• Real users, real transactions, real impact</li>
            <li>• 10,700+ LOC in production today</li>
          </ul>
        </div>
      </div>
    </section>
  );
}
