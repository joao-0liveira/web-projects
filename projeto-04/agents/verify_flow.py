from pathlib import Path

base = Path(__file__).resolve().parent.parent.parent
project_dir = base / 'projeto-04'

required_files = [
    project_dir / '.instructions.md',
    project_dir / 'copilot-instructions.md',
    project_dir / 'prompts.md',
    project_dir / 'index.html',
    project_dir / 'style.css',
    project_dir / 'agents' / 'scaffold-agent.md',
    project_dir / 'agents' / 'generate-projects-agent.md',
    project_dir / 'skills' / 'hero-typing' / 'SKILL.md',
    project_dir / 'skills' / 'flip-card' / 'SKILL.md',
    project_dir / 'skills' / 'skills-bars' / 'SKILL.md',
    project_dir / 'skills' / 'timeline-scroll' / 'SKILL.md',
    project_dir / 'skills' / 'contact-form' / 'SKILL.md',
]

missing = [str(path.relative_to(base)) for path in required_files if not path.exists()]

if missing:
    print('Faltam arquivos no fluxo de projeto:')
    for path in missing:
        print(' -', path)
    raise SystemExit(1)

print('Arquivos básicos encontrados: OK')

html = (project_dir / 'index.html').read_text(encoding='utf-8')
css = (project_dir / 'style.css').read_text(encoding='utf-8')
agent = (project_dir / 'agents' / 'scaffold-agent.md').read_text(encoding='utf-8')

required_ids = ['#hero', '#about', '#skills', '#projects', '#timeline', '#contact']
for anchor in required_ids:
    if anchor not in html:
        print('Falta seção no index.html:', anchor)
        raise SystemExit(1)

print('IDs de seção no index.html: OK')

required_css_snippets = ['@keyframes typing', '.project-card', '.skill-fill', 'scroll-snap-type', '.contact-form']
for snippet in required_css_snippets:
    if snippet not in css:
        print('Falta trecho CSS importante:', snippet)
        raise SystemExit(1)

print('Trechos importantes em style.css: OK')

if 'Use o scaffold agent' not in agent and 'Fluxo automatizado' not in agent:
    print('Agente scaffold sem instruções de fluxo automatizado. Verifique scaffold-agent.md')
    raise SystemExit(1)

print('Agentes têm fluxo definido: OK')
print('\nVerificação completa: fluxo automatizado configurado corretamente.')
