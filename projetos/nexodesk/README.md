# NexoDesk — Central de Suporte TI

Aplicação web demonstrativa para organizar chamados de suporte técnico, acompanhar prioridades, registrar atualizações, consultar inventário de equipamentos e visualizar indicadores operacionais.

## Demonstração online

A aplicação foi publicada dentro do portfólio: https://vinicius589.github.io/portfolio-vinicius/projetos/nexodesk/

## Tecnologias

- HTML5
- CSS3 responsivo
- JavaScript (ES6+)
- LocalStorage para persistência local
- Exportação de chamados para CSV e backup da base em JSON

## Funcionalidades

- Painel com chamados abertos, em atendimento, resolvidos e atenção necessária.
- Cadastro de chamados com solicitante, ativo, categoria, prioridade e descrição.
- Atualização de status e prioridade, com histórico simples.
- Busca e filtros de chamados.
- Inventário demonstrativo de equipamentos com pesquisa.
- Indicadores e gráficos calculados a partir da base atual.
- Exportação CSV e backup JSON.
- Persistência no navegador e opção para restaurar os dados demonstrativos.
- Layout responsivo para telas menores.

## Como executar

Basta abrir `index.html` no navegador. Não há dependências externas de JavaScript nem etapa de build. A fonte da aplicação está inteiramente nesta página para facilitar a publicação estática em GitHub Pages.

## Como testar

1. Abra a demonstração.
2. Crie um chamado usando o botão **Novo chamado**.
3. Acesse a aba **Chamados**, pesquise o assunto e teste os filtros.
4. Abra o chamado, altere status ou prioridade e salve.
5. Confira os indicadores na aba **Relatórios**.
6. Exporte CSV e backup JSON.
7. Recarregue a página: os chamados ficam salvos no armazenamento local do navegador.

## Escopo e limitações

Este é um projeto de portfólio, não um service desk pronto para uso empresarial. Os dados iniciais são fictícios. As alterações ficam no `localStorage` deste navegador; não existe autenticação, API ou banco de dados compartilhado. O inventário é demonstrativo e não é editável nesta versão.

## Próximos passos possíveis

- API e banco de dados para múltiplos usuários.
- Login e permissões por perfil.
- Cadastro e edição de ativos.
- Testes automatizados de interface.
- Métricas de tempo de primeira resposta e resolução.

## Autor

Vinicius da Motta Campos — projeto de portfólio para demonstrar desenvolvimento web, fluxo de atendimento e organização de dados de suporte técnico.
