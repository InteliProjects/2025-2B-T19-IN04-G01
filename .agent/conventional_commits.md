# Instruções para Commits e Pull Requests - Projeto de Administração Tecnológica

## Commits com Conventional Commits

Todos os commits neste projeto devem seguir o padrão **Conventional Commits**. Isso ajuda a manter um histórico de commits compreensível e automatiza a geração de changelogs.

### Estrutura do Commit

```
<tipo>[!][escopo opcional]: <descrição>

[corpo opcional]

[rodapé opcional]
```

### Tipos de Commits

- **feat**: Nova funcionalidade
- **fix**: Correção de bug
- **docs**: Atualizações de documentação
- **style**: Mudanças que não afetam o significado do código (espaço em branco, formatação, etc.)
- **refactor**: Mudanças que não corrigem um bug nem adicionam uma funcionalidade
- **perf**: Melhoria de performance
- **test**: Adicionando ou corrigindo testes
- **chore**: Outras mudanças que não modificam arquivos de src ou test

### Escopo

O escopo é opcional e fornece informações contextualizadas sobre o commit. Exemplos:
- `docs:readme`: Documentação do README
- `src:api`: Alterações na API
- `sprint:1`: Alterações relacionadas à sprint 1

### Exclamação (!)

Adicione uma exclamação após o tipo/escopo para indicar uma mudança de breaking change.

### Exemplos de Commits

```
feat: Adiciona nova funcionalidade de login

Adiciona autenticação de usuários com email e senha
e implementa proteção de rotas para áreas restritas.
```

```
fix(docs)!: Atualiza estrutura de pastas no README

BREAKING CHANGE: A estrutura de pastas foi modificada
para melhor organização dos documentos por sprint.
```

```
refactor(sprint:2): melhora estrutura de dashboard
```

## Processo de Commits

1. Faça modificações no código
2. Adicione os arquivos alterados: `git add <arquivos>`
3. Crie o commit com mensagem seguindo o padrão: `git commit -m "<tipo>: <mensagem>"`
4. Envie as alterações: `git push`

## Processo de Pull Requests

1. Crie uma branch para a feature/fix: `git checkout -b feature/minha-feature`
2. Faça os commits seguindo o padrão de conventional commits
3. Envie a branch: `git push origin feature/minha-feature`
4. Crie um Pull Request usando o template fornecido no repositório
5. Preencha todos os campos obrigatórios no PR
6. Aguarde revisão e aprovação da equipe

## Recomendações

- Mantenha os commits pequenos e focados em uma única responsabilidade
- Escreva mensagens de commit claras e descritivas
- Use o corpo do commit para explicações mais detalhadas quando necessário
- Sempre que possível, crie commits que façam sentido isoladamente