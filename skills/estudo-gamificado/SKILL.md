---
name: estudo-gamificado
description: "Criar trilhas de estudo do início ao avançado com explicações detalhadas, exemplos visuais, exercícios com gabarito, missões e progresso. Usar para aprender um tema de forma estruturada ou transformar vídeos, documentos e links em material de estudo nesse formato."
---

# Estudo gamificado

Transforme um tema ou conjunto de fontes em um percurso que o usuário consiga começar, praticar, revisar e concluir. Reproduza o método do estudo de Design Patterns: fontes identificadas, pré-requisitos, explicações autorais, exemplos, exercícios e progressão por evidências.

Use português brasileiro por padrão neste perfil; preserve a língua solicitada. Python, 12 mundos, 30 exercícios e um repositório específico foram escolhas daquele estudo, não requisitos universais.

## Delimitar o aprendizado

- Identifique tema, objetivo prático e nível atual pelo pedido e contexto. Para “do zero”, ensine a base antes do conteúdo especializado.
- Reaproveite escolhas já informadas: linguagem, disponibilidade, formato e fontes. Pergunte apenas quando a informação ausente muda significativamente o resultado; avance no trabalho independente enquanto aguarda.
- Declare hipóteses importantes. Horas e semanas são estimativas, não promessas.
- Em programação, respeite a linguagem escolhida; sem preferência, proponha uma adequada e explique o motivo. Outros domínios não devem virar automaticamente cursos de programação.

## Mapear fontes e cobertura

- Expanda playlists/listas, inventarie e remova duplicatas por identificador. Preserve títulos, autores, links e ordem original, separando-a da ordem pedagógica.
- Distinga metadados, descrição, trechos consultados, texto integral e audiovisual revisado. Não apresente conteúdo inferido do título como resumo de uma aula assistida.
- Informe lacunas e a cobertura real. Legendas automáticas podem errar termos; não invente falas, timestamps, capítulos ou acesso bem-sucedido.
- Use fontes primárias para verificar conteúdo técnico. Sem fontes do usuário, selecione referências adequadas e crie explicações autorais.
- Respeite limites de reprodução de terceiros. Links não autorizam transcrições integrais; quando a reprodução não for permitida, entregue resumos identificados como tais. Textos fornecidos pelo usuário podem ser organizados conforme o pedido.
- Mantenha dados brutos e scripts de coleta na área de trabalho; entregue somente os materiais previstos.

## Construir o percurso

Ordene por dependências: fundamentos → conceitos → aplicação guiada → prática independente → comparação e análise de erros → integração avançada. Defina objetivos observáveis, não apenas assuntos.

Cada módulo ou “mundo” deve oferecer:

1. Pré-requisitos e habilidade a demonstrar.
2. Explicação detalhada da ideia, do problema e da utilidade; introdução do vocabulário antes de usá-lo.
3. Exemplo trabalhado com dados, etapas, resultado e raciocínio. Separe analogia de definição.
4. Visual que ajude a compreender uma relação, processo ou consequência.
5. Exercícios graduais, dicas opcionais, resultado esperado e gabarito comentado em seção separada.
6. Desafio de mudança ou transferência para outra situação.
7. Perguntas de recuperação de memória e critério de avanço.

Leia [material-e-organizacao.md](references/material-e-organizacao.md) ao produzir o caderno e os arquivos. Ele contém modelos de módulo, exercícios, acompanhamento e estrutura de pastas.

Cubra os assuntos principais antes dos raros. Apresente limitações, confusões frequentes e alternativas simples. “Avançado” exige decisões e integração, não apenas nomes difíceis. Declare o que fica fora da trilha.

## Explicar visualmente

- Use texto ou Mermaid para relações estáticas, com alternativa legível sem renderizador.
- Para “o que acontece se…”, prefira um exemplo interativo que permita mudar uma entrada e observar uma consequência. Use a skill de visualização quando disponível e pertinente, seguindo suas instruções.
- Para figuras/documentos compartilháveis, use ferramentas de exportação e as skills de formato disponíveis quando necessárias.
- Faça o exemplo inicial funcionar antes da interação. Evite decoração sem utilidade e números sem unidade.
- Verifique cálculos e interações. Para código, indique requisitos e dependências de definições anteriores; diferencie demonstração didática de solução pronta para uso real.

## Gamificar a prática

Modelo configurável: explicar 20 XP, prever 20, construir/resolver 40, verificar 20, chefe 50 e revisitar 10. Total: 160 XP por mundo. Adapte ao tema e à duração.

- Conceda XP uma vez por evidência, sem premiar repetição mecânica. Errar não desconta pontos.
- O chefe é uma nova situação que usa as habilidades do módulo.
- Separe XP de domínio: o portão de avanço depende de resolver, verificar, vencer o desafio e responder às perguntas de revisão.
- Recalcule teto e insígnias conforme o número real de mundos; não atribua conquistas ainda não demonstradas.
- Proponha revisões em 1, 3, 7 e 14 dias, ajustáveis. Comece por lembrar e explicar antes de reler.
- Forneça diário de previsão, tentativa, resultado, dificuldade e revisão. Não agende lembretes automaticamente sem pedido.

## Organizar e verificar

- Entregue uma primeira missão concreta para o mesmo dia. Não pare em índice ou lista de vídeos quando o pedido for criar o estudo completo.
- Em arquivos, forneça README, como estudar, trilha, exercícios/gabarito, fontes e progresso. Inclua laboratório e projeto final quando adequados. Ofereça caderno único quando facilitar a leitura.
- Separe exemplos resolvidos do projeto que o estudante deve construir. Declare o que é fornecido e o que é tarefa.
- Preserve formato e destino. Não publique um repositório, crie um site ou envie materiais a terceiros só porque isso ocorreu num estudo anterior.
- Quando houver pedido de organização em repositório, examine suas instruções, adapte os links e valide antes de publicar no escopo autorizado. Exclua caches e arquivos de trabalho.
- Confira links locais, contagens, sequência, resultados e coerência entre caderno único e partes. Teste comportamentos relevantes quando houver código.

O helper [validar_material.py](scripts/validar_material.py) confere UTF-8 e referências locais Markdown. Opcionalmente verifica sintaxe de arquivos Python: `python scripts/validar_material.py <pasta-do-material> --check-python`. Ele não confere precisão pedagógica nem executa testes.

## Entregar e acompanhar

Informe onde começar, o que foi criado e limitações materiais de acesso/cobertura. Linke os resultados solicitados e indique a primeira missão, sem prometer aprendizagem automática. Ao acompanhar o estudo, corrija o raciocínio, ajuste o próximo desafio e atualize progresso somente a partir das evidências da conversa.
