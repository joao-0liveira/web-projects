# Agents do Pixel Forge Studios

Este diretório contém agentes e suporte para construir o projeto `projeto-04` de forma orientada por Copilot.

## Objetivo

- `scaffold-agent.md`: cria a base do site (`index.html` e `style.css`) e define o fluxo de cada skill.
- `generate-projects-agent.md`: gera e atualiza os cards da seção `Projetos` a partir de dados de jogos.
- `verify_flow.py`: verifica automaticamente a estrutura mínima do projeto.

## Como usar

1. Abra `projeto-04/copilot-instructions.md` para obter o estilo e as regras do projeto.
2. Use `projeto-04/.instructions.md` para manter o foco no objetivo e nas seções obrigatórias.
3. No Copilot Chat ou no painel de instructions, peça para executar o `scaffold-agent`.
4. Use `projeto-04/prompts.md` para gerar cada seção com prompts específicos.
5. Se precisar criar ou atualizar cards de projeto, use `generate-projects-agent.md`.
6. Execute `python projeto-04/agents/verify_flow.py` para verificar se todos os arquivos e IDs essenciais existem.

## Teste automatizado de fluxo

- O arquivo `verify_flow.py` valida:
  - Presença dos principais arquivos.
  - IDs de seções obrigatórias em `index.html`.
  - Classes de suporte em `style.css`.
  - Presença dos agentes e skills.

## Sugestão de fluxo

1. `scaffold-agent.md` → gera a base.
2. `skills/` → cada `SKILL.md` descreve como gerar uma parte específica.
3. `generate-projects-agent.md` → cria ou atualiza os cards de projeto.
4. `verify_flow.py` → valida o fluxo.

## Execução

```powershell
cd c:\Users\JP\web-projects
python projeto-04/agents/verify_flow.py
```

## Como usar passo a passo

1. Abra `projeto-04/copilot-instructions.md` para ver o contexto do projeto e as regras de estilo.
2. Abra `projeto-04/.instructions.md` para confirmar as 6 seções obrigatórias e as restrições sem JavaScript.
3. Use `projeto-04/prompts.md` para copiar prompts específicos de cada seção.
4. No Copilot ou Chat, peça para gerar o HTML e CSS da seção desejada usando a skill correspondente.
5. Cole os trechos gerados em `projeto-04/index.html` e `projeto-04/style.css`.
6. Rode `python projeto-04/agents/verify_flow.py` sempre que quiser verificar a estrutura do fluxo.

## Próximos passos recomendados

- Personalize os textos e as descrições dos jogos em `index.html`.
- Substitua os placeholders de imagem por imagens reais quando tiver assets próprios.
- Ajuste os delays e as curvas de animação em `style.css` para refinar a experiência.
- Use a skill `flip-card` para criar mais cards de projeto e manter o layout responsivo.
- Atualize `prompts.md` com novos prompts específicos se quiser testar variações de estilo.
