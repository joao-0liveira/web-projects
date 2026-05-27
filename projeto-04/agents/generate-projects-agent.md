# Generate Projects Agent

Função:
Gerar os cards de projetos da seção Projetos com base em dados de jogos e descrições.

Entradas esperadas:
- Nome do jogo
- Descrição curta
- Tipo de desenvolvimento (ex: "Jogo de plataforma", "Experiência visual")
- Imagem placeholder

Saída esperada:
- HTML de cada card dentro de um container `projects-grid`
- CSS para flip card 3D com animações suaves e foco acessível

Exemplo de dados:
- Moonlight Escape | Jogo de exploração noturna com mecânicas de plataforma
- Cyber Nexus | RPG de combate rápido em estética neon
- Neon Grid Racer | Corrida arcade com visual retrofuturista
- Void Guard | Torre de defesa com efeitos de partículas e interface futurista- Shadow Drift | Experiência de corrida sci-fi com neon e gravidade zero
- Pulse Engine | Demo de hub de desenvolvimento com interface dinâmica
Fluxo automatizado:
1. Receba os dados de projeto.
2. Use a skill `flip-card` para gerar HTML e CSS do card.
3. Insira os cards gerados em `projeto-04/index.html` na seção `#projects`.
4. Ajuste o CSS para responsividade e acessibilidade.
5. Execute `python projeto-04/agents/verify_flow.py` para confirmar que os cards e a seção existem.

Uso:
- Copie este agente para o Copilot Chat e peça: "Use os dados abaixo para gerar cards 3D de projetos e atualizar a seção de projetos do Pixel Forge Studios."
- Substitua ou adicione novos projetos e use a habilidade `flip-card` para cada card.

Dica:
- Mantenha o HTML dos cards limpo e sem scripts.
- Confirme que cada card tem `project-card`, `card-inner`, `card-front` e `card-back`.
