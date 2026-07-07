import fitz

# Module-level text width measurement
def measure(text, fontname, fontsize):
    f = getattr(fitz, "get_text_length", None)
    if f:
        return f(text, fontname=fontname, fontsize=fontsize)
    return len(text) * fontsize * 0.5

doc = fitz.open()

# --- Colors ---
dark = (0.1, 0.1, 0.15)
med = (0.35, 0.35, 0.4)
light = (0.55, 0.55, 0.6)
accent = (0.29, 0.27, 0.78)

# --- Layout ---
left = 50
right = 545
width = right - left
page_h = 842
top = 50
bottom_margin = 50

page = doc.new_page(width=595, height=page_h)
y = top

def new_page():
    global page, y
    page = doc.new_page(width=595, height=page_h)
    y = top

def ensure_space(needed):
    global y
    if y + needed > page_h - bottom_margin:
        new_page()

def write_line(text, x, size, color, font="helv"):
    global y
    page.insert_text((x, y + size - 1), text, fontname=font, fontsize=size, color=color)

def header(text, size=11, space_before=14, space_after=8):
    global y
    ensure_space(size + space_after + 30)
    y += space_before
    # Draw a thin line under the header
    write_line(text, left, size, accent)
    y += size + 4
    page.draw_line(fitz.Point(left, y), fitz.Point(right, y), color=(0.85, 0.85, 0.88), width=0.5)
    y += space_after

def text_block(text, size=9, color=med, leading=11, space_after=4):
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

def bullet(text, size=9, color=med, leading=11, indent=14, space_after=2):
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
            write_line("\u2022", left + 4, size, color)
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
    text_block("  " + "  \u2022  ".join(items), size=9, color=med, leading=11, space_after=6)

# ── NAME ──
write_line("Cameron James Weyers", left, 18, dark)
y += 24

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
    "AI Automation Specialist, Systems Architect, and Business Operator with hands-on experience designing and deploying AI-assisted development environments, agentic workflows, automation pipelines, business applications, and MCP-integrated tooling.",
    "Experienced in building production-grade systems using prompt-driven development methodologies, local and cloud-hosted LLMs, Docker infrastructure, workflow automation platforms, APIs, webhooks, and custom orchestration frameworks. Proven ability to rapidly prototype functional solutions, integrate multiple systems, automate complex workflows, and translate business requirements into working software.",
    "Combines strong technical problem-solving ability with operational leadership experience. Comfortable working independently, learning new technologies quickly, and building practical solutions in rapidly evolving AI-first environments."
]
for p in paragraphs:
    text_block(p)

# ── EXPERIENCE ──
header("EXPERIENCE")
write_line("Owner & Systems Architect", left, 10, dark)
y += 12
write_line("2017 \u2013 Present", left, 9, light)
write_line("Seagulls Pub & Grill", left + 120, 9, med)
y += 12
for b in [
    "Built and deployed custom business applications, automation systems, and AI-assisted operational tools.",
    "Designed payroll automation and reporting systems.",
    "Developed POS infrastructure supporting daily operations.",
    "Implemented AI tooling and workflow automation to improve operational efficiency.",
    "Managed business operations, financial reporting, procurement, staffing, and compliance."
]:
    bullet(b)

# ── PROJECTS ──
header("PROJECTS")

project(
    "AI Security Automation Platform",
    "Designed and deployed an AI-assisted security testing platform integrating Hermes AI agents, Model Context Protocol (MCP) tooling, Caido Web Proxy, and multiple bug bounty platforms into a unified automation environment.",
    [
        "Integrated 64+ MCP tools enabling prompt-driven security testing through natural language interaction.",
        "Connected Caido GraphQL APIs, Intigriti, YesWeHack, and Code4rena platforms into a unified workflow.",
        "Built modular automation pipelines covering reconnaissance, vulnerability discovery, proof-of-concept generation, and reporting.",
        "Designed reusable AI-driven workflows capable of orchestrating complex testing tasks through conversational commands.",
        "Resolved authentication, configuration, networking, and cross-platform deployment challenges across Windows and Linux environments."
    ],
    "MCP, Python, Go, GraphQL, Docker, APIs, Webhooks, Hermes, Caido"
)

project(
    "AI Agent Platform & MCP Ecosystem",
    "Architected a self-managed AI agent platform inspired by modern AI-assisted development environments, incorporating memory systems, skill libraries, MCP servers, tool orchestration, asynchronous task execution, and context management.",
    [
        "Built 28+ reusable AI skill modules with conditional activation and context-aware loading.",
        "Developed 6 MCP servers exposing 40+ tools for browser automation, security tooling, API interaction, and workflow execution.",
        "Implemented asynchronous agent delegation and context-compression pipelines for long-running workflows.",
        "Built persistent memory architecture supporting vector search, knowledge retrieval, and session continuity.",
        "Created custom guardrails, validation systems, and automated workflow controls."
    ],
    "Python, MCP, Ollama, Docker, Linux, APIs, Vector Search"
)

project(
    "Seagulls Payroll Management Platform",
    "Designed and developed a full-stack payroll management platform for South African SMEs.",
    [
        "Employee onboarding and document management.",
        "Automated payroll calculations using South African tax regulations.",
        "UIF, SDL, EMP201, IRP5 and statutory compliance reporting.",
        "Employee self-service portal.",
        "PDF payslip generation and WhatsApp delivery.",
        "Payroll reporting and analytics."
    ],
    "Django 4.2, PostgreSQL, Python, WhatsApp Integration"
)

project(
    "Seagulls Point-of-Sale Platform",
    "Built a comprehensive restaurant management and POS solution supporting end-to-end operational workflows.",
    [
        "Product, inventory, purchasing and supplier management.",
        "Reservation and table management.",
        "Kitchen Display System integration.",
        "Multi-tender payment handling.",
        "VAT reporting and compliance.",
        "Shared deployment architecture with payroll platform."
    ],
    "Django 4.2, PostgreSQL, Python"
)

project(
    "N8N AI Automation Workflows",
    "Built self-hosted automation systems combining local LLM inference, API orchestration, workflow automation, and scheduled intelligence gathering.",
    [
        "Developed automated bug bounty reconnaissance workflows using CRT.sh and HackerTarget APIs.",
        "Built AI-powered attack surface analysis using Ollama-hosted local models.",
        "Created automated daily threat-intelligence aggregation and summarisation pipelines.",
        "Designed fault-tolerant workflows with validation, branching logic, and structured outputs.",
        "Delivered fully local AI processing with zero cloud inference costs."
    ],
    "n8n, Ollama, REST APIs, JavaScript, SQLite"
)

# ── TECHNICAL SKILLS ──
header("TECHNICAL SKILLS")

skill_group("AI-Assisted Development", [
    "Prompt-Driven Development", "Claude Code Concepts & Workflows", "Agentic AI Systems",
    "MCP (Model Context Protocol)", "AI Tool Integration", "Prompt Engineering",
    "Multi-Agent Architectures", "LLM Orchestration"
])

skill_group("Automation & Integration", [
    "n8n (Self-Hosted)", "Make.com", "API Integrations", "Webhooks",
    "Workflow Automation", "Scheduled Automation", "Data Pipelines", "System Integration"
])

skill_group("Infrastructure & Development", [
    "Python", "Django", "PostgreSQL", "Docker", "Linux", "Virtual Machines",
    "Git & GitHub", "REST APIs", "YAML Configuration"
])

skill_group("AI Platforms & Tools", [
    "Hermes", "OpenClaw", "OpenRouter", "Manus", "AntiGravity", "Ollama",
    "RunPod", "Caido", "Local LLM Deployments"
])

# ── CONTINUOUS PROFESSIONAL DEVELOPMENT ──
header("CONTINUOUS PROFESSIONAL DEVELOPMENT", size=10)
text_block(
    "AI Automation & Agentic Systems  \u2022  Prompt Engineering  \u2022  Claude Code Ecosystem  \u2022  MCP Architecture  \u2022  Workflow Automation  \u2022  Docker & Containerisation  \u2022  API Design & Integration  \u2022  Business Systems Architecture"
)

pages = doc.page_count
doc.save("cameron-weyers-cv.pdf")
doc.close()
print(f"CV rebuilt successfully — {pages} pages")