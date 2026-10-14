# Skills de estudo

Skills reutilizáveis para criar materiais de aprendizado no Codex.

## Estudo gamificado

Abra a [definição da skill](estudo-gamificado/SKILL.md). Ela transforma um tema ou fontes em uma trilha com fundamentos, explicações, exemplos visuais, exercícios com gabarito, missões, XP, revisões e projeto final.

O método foi usado no módulo de [Design Patterns](<../Design Patterns/README.md>) deste repositório. A skill adapta conteúdo, quantidade de módulos, exemplos e projeto ao assunto escolhido.

### Arquivos

- [SKILL.md](estudo-gamificado/SKILL.md): instruções e critérios do método.
- [Metadados](estudo-gamificado/agents/openai.yaml): nome e prompt sugerido.
- [Modelos de material e organização](estudo-gamificado/references/material-e-organizacao.md): módulos, exercícios, diário e pastas.
- [Verificador](estudo-gamificado/scripts/validar_material.py): links locais, UTF-8 e sintaxe Python opcional.

### Instalar

A skill já está instalada no computador em que foi criada. Para instalar em outra máquina com Codex, peça:

```text
Use $skill-installer para instalar a skill estudo-gamificado
do repositório https://github.com/VikThorSkynet/Estudos
na pasta skills/estudo-gamificado.
```

Para instalação manual, copie a pasta inteira `estudo-gamificado` para a pasta de skills do Codex: `$CODEX_HOME/skills`, quando configurada, ou `~/.codex/skills`. Preserve as subpastas e o arquivo `SKILL.md`.

### Usar

```text
Use $estudo-gamificado para estudar redes de computadores
do zero ao avançado. Tenho 4 horas por semana.
```

Outro exemplo:

```text
Use $estudo-gamificado para criar um estudo de SQL.
Já sei o básico e quero praticar consultas e modelagem.
Organize os materiais em uma pasta SQL neste repositório.
```

Você pode acrescentar vídeos, playlists, documentos ou links, informar o nível atual e escolher o formato de entrega. Publicação no GitHub deve fazer parte do pedido; a skill não presume essa autorização para todos os estudos.

### Verificar materiais

Na raiz deste repositório:

```text
python skills/estudo-gamificado/scripts/validar_material.py "Design Patterns" --check-python
```

O verificador não executa código, não acessa a rede e não avalia a precisão pedagógica. Use `--check-python` quando houver exemplos Python; a conferência de links também funciona para outros temas.
