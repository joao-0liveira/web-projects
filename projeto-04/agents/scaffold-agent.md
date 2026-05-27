# Scaffold Agent

Função:
Orientar a construção inicial do site Pixel Forge Studios criando a estrutura e chamando as skills adequadas.

Passos:
1. Use `projeto-04/.instructions.md` para entender o objetivo e as restrições do projeto.
2. Gere o `index.html` com as seções: `nav`, `hero`, `about`, `skills`, `projects`, `timeline`, `contact`.
3. Gere `style.css` com variáveis de cores, tipografia, reset e estrutura base.
4. Para cada seção, invoque a skill correspondente:
   - `hero-typing`
   - `flip-card`
   - `skills-bars`
   - `timeline-scroll`
   - `contact-form`
5. Adicione animações adicionais ao Hero, como esferas flutuantes e partículas em CSS.
6. Verifique se o HTML contém classes semânticas e IDs de âncora para navegação fixa.
7. Valide que não há JavaScript e que o CSS está centralizado em `style.css`.

Fluxo automatizado:
- Copie o prompt principal deste agente para o Copilot Chat ou painel de instructions.
- Em seguida, use os prompts de `projeto-04/prompts.md` para gerar cada seção e inserir no `index.html`.
- Após gerar cada seção, abra `projeto-04/agents/verify_flow.py` e execute-o para confirmar a estrutura.

Uso:
- Abra este agente no Copilot ou Chat e peça: "Use o scaffold agent para gerar a base do `index.html` e `style.css` do Pixel Forge Studios."
- Atualize os prompts de cada skill quando precisar de ajustes de estilo ou animação.
