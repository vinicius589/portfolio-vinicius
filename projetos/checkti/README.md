# CheckTI — Guia de primeiros testes

Projeto pequeno de estudo para praticar HTML, CSS e JavaScript com um tema ligado à manutenção e ao suporte técnico de computadores.

## Demonstração

https://vinicius589.github.io/portfolio-vinicius/projetos/checkti/

## O que faz

A pessoa escolhe um problema comum e recebe uma lista de verificações iniciais:

- Computador não liga
- Computador está lento
- Computador sem internet
- Computador sem áudio

Cada item pode ser marcado. A página atualiza o progresso e permite limpar as marcações.

## Tecnologias usadas

- **HTML:** estrutura da página e dos botões.
- **CSS:** cores, cartões e adaptação para telas menores.
- **JavaScript:** lista de verificações, seleção do problema e atualização do progresso.

Não usa banco de dados, bibliotecas externas, login ou servidor.

## Como executar

1. Baixe este repositório ou abra a pasta `projetos/checkti`.
2. Abra o arquivo `index.html` no navegador.
3. Selecione um problema e marque as etapas verificadas.

## O que estudar no código

- Como os botões usam `data-problem` para identificar o problema escolhido.
- Como o objeto `problemas` guarda os títulos e as etapas.
- Como `addEventListener` reage aos cliques.
- Como o JavaScript cria os itens do checklist.
- Como a largura da barra de progresso é calculada.

## Limitações

O projeto é apenas um guia de verificações iniciais. Não identifica automaticamente a causa de uma falha nem substitui a avaliação de um técnico. Os passos são orientações genéricas e devem ser seguidos apenas quando forem seguros.

## Autor

Vinicius da Motta Campos — projeto de portfólio em desenvolvimento web básico.
