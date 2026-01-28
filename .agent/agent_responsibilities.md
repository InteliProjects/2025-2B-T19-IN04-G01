# Instruções para o Agente de Desenvolvimento

## Responsabilidades do Agente

O agente de desenvolvimento é responsável por executar tarefas de versionamento e colaboração no projeto de Administração Tecnológica seguindo as melhores práticas estabelecidas.

## Commits com Conventional Commits

O agente deve garantir que todos os commits sigam o padrão **Conventional Commits**:

1. **Sempre** usar um dos tipos especificados:
   - `feat`: Nova funcionalidade
   - `fix`: Correção de bug
   - `docs`: Atualizações de documentação
   - `style`: Mudanças de formatação
   - `refactor`: Refatoração de código
   - `perf`: Melhorias de performance
   - `test`: Adição ou correção de testes
   - `chore`: Tarefas gerais

2. **Sempre** incluir uma descrição clara e concisa da mudança

3. **Opcionalmente** usar escopo para indicar a parte do projeto afetada

4. **Quando apropriado** usar `!` para indicar breaking changes e incluir BREAKING CHANGE no corpo do commit

## Pull Requests

O agente deve:

1. **Criar branches com nomes descritivos**:
   - `feature/nome-da-funcionalidade`
   - `fix/nome-da-correcao`
   - `docs/atualizacao-documentacao`
   - `sprint/sprint-x-nome-tarefa`

2. **Criar pull requests usando o template** do repositório

3. **Preencher todos os campos obrigatórios** no template de PR

4. **Associar o PR às issues relevantes** quando possível

5. **Garantir que os checks passem** antes de solicitar revisão

## Critérios de Qualidade

Antes de criar commits ou PRs, o agente deve verificar:

- [ ] O código está funcional e testado
- [ ] A documentação foi atualizada conforme necessário
- [ ] O código segue as convenções do projeto
- [ ] Não há código comentado desnecessariamente
- [ ] Não há console.logs ou debugs temporários
- [ ] Os commits seguem o padrão de conventional commits
- [ ] O PR tem um título e descrição claros
- [ ] Todas as verificações do checklist no template de PR foram feitas

## Processo de Integração Contínua

O agente deve:

1. Atualizar a branch local com a branch principal antes de criar um PR
2. Resolver conflitos de merge quando necessário
3. Manter as branches atualizadas
4. Garantir que todos os testes e verificações passem

## Boas Práticas

- Realizar commits frequentes com mudanças focadas
- Escrever mensagens de commit claras e descritivas
- Manter o histórico de commits limpo e organizado
- Revisar o código antes de submeter para PR
- Garantir que as mudanças estejam alinhadas com os objetivos do projeto e do sprint correspondente