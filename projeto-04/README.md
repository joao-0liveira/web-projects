# Pixel Forge Studios - Projeto 04

Este diretório contém a estrutura do projeto `projeto-04`, um portfólio fictício de desenvolvedor de jogos indie com foco em CSS avançado e animações no estilo Cyberpunk / Gamer.

## Estrutura do projeto

- `copilot-instructions.md`: contexto global para o Copilot, estilo e restrições do projeto.
- `.instructions.md`: instruções específicas do projeto e seções obrigatórias.
- `prompts.md`: prompts reutilizáveis para gerar cada seção do site.
- `skills/`: skills modulares com descrições e exemplos por seção.
- `agents/`: fluxos de automação que guiam a criação do site e validam o projeto.
- `index.html`: esqueleto do site com seções principais.
- `style.css`: CSS base com tema escuro, animações e layout responsivo.

## Como usar

1. Abra `copilot-instructions.md` para ver o estilo e as regras gerais do projeto.
2. Leia `.instructions.md` para confirmar as seis seções obrigatórias.
3. Use `prompts.md` para escolher o prompt certo para cada seção.
4. Abra `agents/scaffold-agent.md` para seguir o fluxo de criação inicial do site.
5. Use as skills em `skills/` para refinar cada bloco:
   - `hero-typing`: seção Hero animada.
   - `flip-card`: cards de projeto 3D.
   - `skills-bars`: barras de skill animadas.
   - `timeline-scroll`: linha do tempo horizontal.
   - `contact-form`: formulário de contato animado.
6. Gere HTML e CSS com o Copilot e cole o resultado em `index.html` e `style.css`.
7. Execute o verificador de fluxo:

```powershell
cd c:\Users\JP\web-projects
python projeto-04/agents/verify_flow.py
```

## Próximos passos

- Personalizar os textos e nomes dos jogos na seção `Projetos`.
- Substituir imagens placeholders por imagens reais do portfólio.
- Ajustar a paleta de cores, curvas de animação e pontos de foco no CSS.
- Criar mais cards de projeto usando a skill `flip-card`.
- Adicionar novos prompts a `prompts.md` para testar variações de layout.
- Use `agents/generate-projects-agent.md` sempre que quiser ampliar a seção de projetos de forma estruturada.

## Notas finais

O objetivo desta estrutura é oferecer um fluxo de trabalho autônomo com Copilot, onde cada arquivo tem um papel claro:
- `copilot-instructions.md` para o assistente entender o estilo do projeto.
- `prompts.md` para gerar trechos específicos.
- `skills/` para dividir a produção em partes independentes.
- `agents/` para orquestrar a criação e verificar a qualidade do fluxo.
