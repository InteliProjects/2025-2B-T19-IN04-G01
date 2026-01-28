# Guia Rápido de Commits - Agente de Desenvolvimento

## Tipos de Commits (Conventional Commits)

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| `feat` | Nova funcionalidade | `feat: adiciona autenticação de usuários` |
| `fix` | Correção de bug | `fix: corrige erro de validação no formulário` |
| `docs` | Atualização de documentação | `docs: atualiza README com instruções de setup` |
| `style` | Formatação, semântica não alterada | `style: corrige indentação em arquivo de config` |
| `refactor` | Refatoração de código | `refactor: melhora estrutura de dados em módulo X` |
| `perf` | Melhoria de performance | `perf: otimiza consulta de dados em dashboard` |
| `test` | Adiciona ou corrige testes | `test: adiciona testes para módulo de autenticação` |
| `chore` | Tarefas gerais | `chore: atualiza dependências do projeto` |

## Exemplos Avançados

### Com escopo:
```
feat(api): adiciona endpoint para criação de usuários
```

```
fix(docs)!: atualiza estrutura de pastas no README

BREAKING CHANGE: A estrutura de pastas foi modificada
para melhor organização dos documentos por sprint.
```

### Com corpo detalhado:
```
refactor(sprint:2): melhora performance do dashboard

- Implementa caching para dados frequentes
- Otimiza consultas ao banco de dados
- Adiciona carregamento lazy em gráficos pesados
```

## Processo Rápido

1. **Fazer alterações**
2. **Adicionar arquivos**: `git add .`
3. **Criar commit**: `git commit -m "tipo: mensagem descritiva"`
4. **Enviar alterações**: `git push`
5. **Criar Pull Request** se necessário

## Verificação Final

Antes de cada commit, verifique:
- [ ] O código está funcional
- [ ] A mensagem do commit segue o padrão
- [ ] Não há erros ou warnings
- [ ] A documentação está atualizada
- [ ] O commit faz sentido isoladamente