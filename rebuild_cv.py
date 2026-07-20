import fitz

# Module-level text width measurement
def measure(text, fontname, fontsize):
    f = getattr(fitz, "get_text_length", None)
    if f:
        return f(text, fontname=fontname, fontsize=fontsize)
    return len(text) * fontsize * 0.5

doc = fitz.open()

# --- Colors (matching the new portfolio palette) ---
dark = (0.098, 0.110, 0.106)      # --ink
med = (0.263, 0.286, 0.275)       # --ink-2
light = (0.463, 0.490, 0.475)     # --ink-3
green = (0.118, 0.361, 0.255)     # --green
rule = (0.85, 0.85, 0.82)

# --- Layout ---
left = 55
right = 540
width = right - left
page_w = 595
page_h = 842
top = 55
bottom_margin = 55

page = doc.new_page(width=page_w, height=page_h)
y = top

def new_page():
    global page, y
    page = doc.new_page(width=page_w, height=page_h)
    y = top

def ensure_space(needed):
    global y
    if y + needed > page_h - bottom_margin:
        new_page()

def write_line(text, x, size, color, font="helv"):
    global y
    page.insert_text((x, y + size - 1), text, fontname=font, fontsize=size, color=color)

def header(text, size=11, space_before=10, space_after=5):
    global y
    ensure_space(size + space_after + 30)
    y += space_before
    write_line(text, left, size, green)
    y += size + 4
    page.draw_line(fitz.Point(left, y), fitz.Point(right, y), color=rule, width=0.5)
    y += space_after

def text_block(text, size=9.5, color=med, leading=12, space_after=5):
    global y
    words = text.split()
    line = ""
    lines = []
    for w in words:
        test = (line + " " + w).strip()
        if measure(test, "helv", size) > width:
            lines.append(line)
            line = w
        else:
            line = test
    if line:
        lines.append(line)
    for ln in lines:
        ensure_space(leading)
        write_line(ln, left, size, color)
        y += leading
    y += space_after

def bullet(text, size=9.5, color=med, leading=12, indent=14, space_after=2):
    global y
    words = text.split()
    line = ""
    lines = []
    avail = width - indent
    for w in words:
        test = (line + " " + w).strip()
        if measure(test, "helv", size) > avail:
            lines.append(line)
            line = w
        else:
            line = test
    if line:
        lines.append(line)
    for i, ln in enumerate(lines):
        ensure_space(leading)
        if i == 0:
            write_line("\u2022", left + 4, size, green)
        write_line(ln, left + indent, size, color)
        y += leading
    y += space_after

def project(name, desc, bullets, tech):
    global y
    ensure_space(80)
    write_line(name, left, 10, dark)
    y += 13
    text_block(desc, size=9, color=med, leading=11, space_after=2)
    for b in bullets:
        bullet(b)
    write_line("Technologies: " + tech, left, 8.5, light)
    y += 12

def skill_group(name, items):
    global y
    ensure_space(40)
    write_line(name, left, 9.5, dark)
    y += 12
    text_block("  " + "  \u2022  ".join(items), size=9, color=med, leading=11, space_after=4)

# ── NAME ──
write_line("Cameron James Weyers", left, 18, dark)
y += 22

# ── CONTACT LINE ──
contact = "Bredasdorp, Western Cape, South Africa  |  cameronweyers@gmail.com  |  linkedin.com/in/cameron-weyers  |  github.com/kigansolutions"
words = contact.split(" ")
line = ""
lines = []
for w in words:
    test = (line + " " + w).strip()
    if measure(test, "helv", 8.5) > width:
        lines.append(line)
        line = w
    else:
        line = test
if line:
    lines.append(line)
for ln in lines:
    ensure_space(11)
    write_line(ln, left, 8.5, light)
    y += 11

# ── SUMMARY ──
header("SUMMARY")
paragraphs = [
    "AI Systems Builder and founder of Kigan Agentic AI Solutions — designing and shipping custom AI agents, RAG-backed where memory matters, that automate real business workflows from content drafting to reporting to day-to-day operations. Built from the operating side, not the demo side.",
    "Nine years as a business owner-operator, with a background in audit and accounting. Everything I build runs in production — I'm my own harshest client, and every system is judged by what it costs when it breaks, not how it looks in a slide."
]
for p in paragraphs:
    text_block(p)

# ── EXPERIENCE ──
header("EXPERIENCE")
write_line("Founder & AI Systems Builder", left, 10, dark)
y += 12
write_line("2024 \u2013 Present", left, 9, light)
write_line("Kigan Agentic AI Solutions \u00b7 Remote", left + 120, 9, med)
y += 13
for b in [
    "Design and build custom AI agents that automate content, research, and workflow tasks for clients — Claude Agent SDK, Trigger.dev, n8n, and direct API integrations.",
    "Shipped a weekly LinkedIn content agent and a full research-to-send newsletter pipeline, both running unattended in production.",
    "Adapted Nous Research's open agent framework into Hermes, a self-hosted platform running six MCP servers, 40+ tools, and daily automated briefings.",
    "Self-taught, in public: two years from spreadsheet automation to a full agentic platform, every build shipped to production, not demoed."
]:
    bullet(b)
y += 3

write_line("Owner & Systems Architect", left, 10, dark)
y += 12
write_line("2017 – Present", left, 9, light)
write_line("Seagulls Pub & Grill · Bredasdorp, South Africa", left + 120, 9, med)
y += 13
for b in [
    "Built and deployed custom business applications, automation systems, and AI-assisted operational tools.",
    "Designed SARS-compliant payroll automation and reporting systems, still running production payroll monthly.",
    "Managed business operations, financial reporting, procurement, staffing, and compliance for nine years on thin hospitality margins."
]:
    bullet(b)

# ── PROJECTS ──
header("PROJECTS")

project(
    "LinkedIn Drafting Agent",
    "Weekly agent that researches live discussion, drafts a post in my voice using the Claude Agent SDK, and files it to ClickUp for review — unattended, every Monday. Built for Kigan.",
    [
        "Sources live discussion via web search rather than relying on stale training data — Reddit blocks direct API access.",
        "Drafts in a consistent voice using a detailed style system prompt, deduplicated against prior topics.",
        "Hands off to a human review step via ClickUp — never auto-publishes."
    ],
    "Claude Agent SDK, Trigger.dev, ClickUp API"
)

project(
    "Newsletter Automation",
    "Research-to-send pipeline: sourcing, branded copy, charts and AI imagery, HTML build, Gmail draft — no manual step in between. Runs Kigan's own newsletter.",
    [
        "Fully automated content pipeline from research through branded, ready-to-send HTML email.",
        "Generates supporting charts and AI imagery matched to brand guidelines.",
        "Delivers directly to a Gmail draft for final review before send."
    ],
    "Python, OpenRouter, Gmail API"
)

project(
    "Hermes \u2014 AI Agent Platform (Adapted)",
    "Adapted Nous Research's open agent framework into a self-hosted, production-grade platform — Ubuntu VM, Tailscale-only, local LLM inference via Ollama. Infrastructure I live on, not a portfolio piece.",
    [
        "Built 28+ reusable AI skill modules with conditional activation and context-aware loading.",
        "Developed 6 MCP servers exposing 40+ tools for browser automation, API interaction, and workflow execution.",
        "Built RAG-based persistent memory architecture supporting vector search and session continuity, integrated with Gmail and Calendar."
    ],
    "Python, MCP, Ollama, LangGraph, CrewAI, Chroma/Qdrant, Tailscale, Linux"
)

project(
    "Seagulls Payroll Management Platform",
    "Designed and developed a full-stack payroll management platform for South African SMEs. SARS-compliant — PAYE, UIF, SDL, EMP201, IRP5.",
    [
        "Automated payroll calculations using South African tax regulations — PAYE, UIF, SDL.",
        "Statutory compliance reporting: EMP201, IRP5.",
        "Employee self-service portal with PDF payslip generation and WhatsApp delivery."
    ],
    "Django 4.2, PostgreSQL, Python, WhatsApp Integration"
)

project(
    "n8n AI Automation Workflows",
    "Built self-hosted automation systems combining local LLM inference, API orchestration, workflow automation, and scheduled intelligence gathering. Fully local AI processing with zero cloud inference costs.",
    [
        "Built AI-powered data analysis and summarisation pipelines using Ollama-hosted local models.",
        "Designed fault-tolerant workflows with validation, branching logic, and structured outputs.",
        "Wired local LLMs into Gmail, Sheets, and external APIs \u2014 manual daily admin replaced by triggers."
    ],
    "n8n, Ollama, REST APIs, JavaScript"
)

# ── THE ARC (Career History) ──
header("THE ARC")

def arc_row(year, role, org, note):
    global y
    ensure_space(50)
    write_line(year, left, 8.5, green)
    y += 11
    write_line(role, left, 9.5, dark)
    y += 12
    write_line(org, left, 8.5, light)
    y += 11
    text_block(note, size=9, color=med, leading=11, space_after=5)

arc_row("2024 \u2013 now", "Founder & AI Systems Builder", "Kigan Agentic AI Solutions",
    "Self-taught, in public, on live systems. Two years from spreadsheet automation to a full agentic platform.")

arc_row("2017 \u2013 now", "Owner", "Seagulls Pub & Grill \u00b7 Bredasdorp, South Africa",
    "Nine years on thin margins. Every system shipped is filtered through what it costs when it fails at 19:00 on a Friday.")

arc_row("2009 \u2013 2017", "Senior Sous Chef \u2192 Head Chef \u2192 Chef Patron",
    "Stoke Place (3 AA Rosettes) \u00b7 Macdonald Bear (2 AA Rosettes) \u00b7 The Sun Inn \u2014 UK",
    "Eight years of high-velocity systems under pressure: zero tolerance for anything that doesn't work when it has to.")

arc_row("2004 \u2013 2007", "Audit & Article Clerk", "Luyt Proudfoot Hall & Associates \u00b7 South Africa",
    "Where the habit started: build to the number, not the demo.")

# ── TECHNICAL SKILLS ──
header("TECHNICAL SKILLS")

skill_group("Agentic AI", [
    "Claude Code", "Prompt-Driven Development", "Hermes (Nous Research, adapted)", "LangGraph", "CrewAI", "MCP",
    "Multi-Agent Architectures", "LLM Orchestration"
])

skill_group("LLM Runtime", [
    "Ollama", "OpenRouter", "Local LLM Deployments", "RunPod"
])

skill_group("Automation & Integration", [
    "n8n (Self-Hosted)", "Make.com", "REST APIs", "Webhooks",
    "Workflow Automation", "Scheduled Automation", "Data Pipelines"
])

skill_group("Development", [
    "Python", "Django", "PostgreSQL", "Linux", "Git & GitHub"
])

skill_group("Memory & Data", [
    "RAG", "Chroma", "Qdrant", "SQLite", "Vector Embeddings", "Vector Search"
])

skill_group("Infrastructure", [
    "Ubuntu 24 LTS", "Tailscale", "Virtual Machines", "YAML Configuration"
])

# ── CONTINUOUS PROFESSIONAL DEVELOPMENT ──
header("CONTINUOUS PROFESSIONAL DEVELOPMENT", size=10)
text_block(
    "AI Automation & Agentic Systems  \u2022  Prompt Engineering  \u2022  Claude Code Ecosystem  \u2022  MCP Architecture  \u2022  Workflow Automation  \u2022  API Design & Integration  \u2022  Business Systems Architecture"
)

pages = doc.page_count
doc.save("cameron-weyers-cv.pdf")
doc.close()
print(f"CV rebuilt successfully \u2014 {pages} pages")