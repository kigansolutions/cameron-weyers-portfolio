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

def header(text, size=11, space_before=16, space_after=8):
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

def bullet(text, size=9.5, color=med, leading=12, indent=14, space_after=3):
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
    y += 13

def skill_group(name, items):
    global y
    ensure_space(40)
    write_line(name, left, 9.5, dark)
    y += 12
    text_block("  " + "  \u2022  ".join(items), size=9, color=med, leading=11, space_after=6)

# ── NAME ──
write_line("Cameron James Weyers", left, 18, dark)
y += 22

# ── CONTACT LINE ──
contact = "Bredasdorp, Western Cape, South Africa  |  cameronweyers@gmail.com  |  linkedin.com/in/cameron-weyers-132a074b  |  github.com/Koslovski79"
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
    "AI Systems Builder and Automation Specialist with hands-on experience designing and deploying agentic AI systems, workflow automation, and business software — built from the operating side.",
    "Experienced in building production-grade systems using prompt-driven development, local and cloud-hosted LLMs, Docker infrastructure, workflow automation platforms, APIs, and custom orchestration frameworks. Background in audit and accounting, with nine years as a business owner-operator. Proven ability to rapidly prototype functional solutions, integrate multiple systems, and translate business requirements into working software.",
    "Everything I build runs in production, not just in demos. Comfortable working independently, learning new technologies quickly, and building practical solutions in rapidly evolving AI-first environments."
]
for p in paragraphs:
    text_block(p)

# ── EXPERIENCE ──
header("EXPERIENCE")
write_line("Owner & Systems Architect", left, 10, dark)
y += 12
write_line("2017 \u2013 Present", left, 9, light)
write_line("Seagulls Pub & Grill \u00b7 Bredasdorp, South Africa", left + 120, 9, med)
y += 13
for b in [
    "Built and deployed custom business applications, automation systems, and AI-assisted operational tools.",
    "Designed SARS-compliant payroll automation and reporting systems.",
    "Developed POS infrastructure supporting daily hospitality operations.",
    "Implemented AI tooling and workflow automation to improve operational efficiency.",
    "Managed business operations, financial reporting, procurement, staffing, and compliance."
]:
    bullet(b)

# ── PROJECTS ──
header("PROJECTS")

project(
    "Hermes \u2014 AI Agent Platform (Adapted)",
    "Adapted and tuned Nous Research's open agent framework into a self-hosted, production-grade agentic platform. Ubuntu VM, Tailscale-only, with local LLM inference via Ollama. Six MCP servers, 40+ tools, 28+ skills. Daily morning briefings, Telegram nudges, voice via Whisper, and a Streamlit dashboard. Infrastructure I live on, not a portfolio piece.",
    [
        "Built 28+ reusable AI skill modules with conditional activation and context-aware loading.",
        "Developed 6 MCP servers exposing 40+ tools for browser automation, security tooling, API interaction, and workflow execution.",
        "Implemented asynchronous agent delegation and context-compression pipelines for long-running workflows.",
        "Built persistent memory architecture supporting vector search, knowledge retrieval, and session continuity.",
        "Integrated Gmail, Calendar, and tool access via MCP connectors \u2014 private by design, running on own infrastructure."
    ],
    "Python, MCP, Ollama, LangGraph, CrewAI, Chroma/Qdrant, Tailscale, Linux"
)

project(
    "AI Security Automation Platform",
    "Designed and deployed an AI-assisted security testing platform integrating Hermes AI agents, MCP tooling, Caido Web Proxy, and multiple bug bounty platforms into a unified automation environment.",
    [
        "Integrated 64+ MCP tools enabling prompt-driven security testing through natural language interaction.",
        "Connected Caido GraphQL APIs, Intigriti, YesWeHack, and Code4rena platforms into a unified workflow.",
        "Built modular automation pipelines covering reconnaissance, vulnerability discovery, proof-of-concept generation, and reporting.",
        "Designed reusable AI-driven workflows capable of orchestrating complex testing tasks through conversational commands."
    ],
    "MCP, Python, Go, GraphQL, Docker, Hermes, Caido"
)

project(
    "Seagulls Payroll Management Platform",
    "Designed and developed a full-stack payroll management platform for South African SMEs. SARS-compliant — PAYE, UIF, SDL, EMP201, IRP5.",
    [
        "Employee onboarding and document management.",
        "Automated payroll calculations using South African tax regulations.",
        "UIF, SDL, EMP201, IRP5 and statutory compliance reporting.",
        "Employee self-service portal with PDF payslip generation and WhatsApp delivery.",
        "Payroll reporting and analytics."
    ],
    "Django 4.2, PostgreSQL, Python, WhatsApp Integration"
)

project(
    "Seagulls Point-of-Sale Platform",
    "Built a comprehensive restaurant management and POS solution supporting end-to-end operational workflows. Designed for the way a real Friday service moves, not the way a demo does.",
    [
        "Product, inventory, purchasing and supplier management.",
        "Reservation and table management.",
        "Kitchen Display System integration.",
        "Multi-tender payment handling.",
        "VAT reporting and compliance.",
        "46 models in production."
    ],
    "Django 4.2, PostgreSQL, Python"
)

project(
    "n8n AI Automation Workflows",
    "Built self-hosted automation systems combining local LLM inference, API orchestration, workflow automation, and scheduled intelligence gathering. Fully local AI processing with zero cloud inference costs.",
    [
        "Developed automated bug bounty reconnaissance workflows using CRT.sh and HackerTarget APIs.",
        "Built AI-powered attack surface analysis using Ollama-hosted local models.",
        "Created automated daily threat-intelligence aggregation and summarisation pipelines.",
        "Designed fault-tolerant workflows with validation, branching logic, and structured outputs.",
        "Wired local LLMs into Gmail, Sheets, and external APIs \u2014 manual daily admin replaced by triggers."
    ],
    "n8n, Ollama, REST APIs, JavaScript, SQLite"
)

project(
    "OpenClaw \u2014 Local Agent Runtime",
    "Terminal-based agentic environment using OpenRouter for prompt-driven script execution and LLM benchmarking across providers \u2014 the testbed behind the choices made on client work.",
    [
        "Multi-LLM routing across providers for benchmarking and comparison.",
        "Prompt-driven script execution and automated testing pipelines.",
    ],
    "OpenRouter, Python, multi-LLM routing"
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
    text_block(note, size=9, color=med, leading=11, space_after=8)

arc_row("2024 \u2013 now", "AI Systems Builder", "Hermes \u00b7 automation \u00b7 payroll \u2014 everything in production",
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
    "Hermes (Nous Research, adapted)", "LangGraph", "CrewAI", "MCP",
    "Claude Code", "Prompt-Driven Development", "Multi-Agent Architectures", "LLM Orchestration"
])

skill_group("LLM Runtime", [
    "Ollama", "OpenRouter", "Local LLM Deployments", "RunPod"
])

skill_group("Automation & Integration", [
    "n8n (Self-Hosted)", "Make.com", "REST APIs", "Webhooks",
    "Workflow Automation", "Scheduled Automation", "Data Pipelines"
])

skill_group("Development", [
    "Python", "Django", "PostgreSQL", "Docker", "Linux", "Git & GitHub"
])

skill_group("Memory & Data", [
    "Chroma", "Qdrant", "SQLite", "Vector Embeddings", "Vector Search"
])

skill_group("Infrastructure", [
    "Ubuntu 24 LTS", "Tailscale", "Virtual Machines", "YAML Configuration"
])

# ── CONTINUOUS PROFESSIONAL DEVELOPMENT ──
header("CONTINUOUS PROFESSIONAL DEVELOPMENT", size=10)
text_block(
    "AI Automation & Agentic Systems  \u2022  Prompt Engineering  \u2022  Claude Code Ecosystem  \u2022  MCP Architecture  \u2022  Workflow Automation  \u2022  Docker & Containerisation  \u2022  API Design & Integration  \u2022  Business Systems Architecture"
)

pages = doc.page_count
doc.save("cameron-weyers-cv.pdf")
doc.close()
print(f"CV rebuilt successfully \u2014 {pages} pages")