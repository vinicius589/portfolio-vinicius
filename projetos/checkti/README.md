# CheckTI — Checklist inicial de suporte

Projeto de estudo para praticar HTML, CSS e JavaScript com um tema de manutenção e suporte técnico de computadores.

## Demonstração

https://vinicius589.github.io/portfolio-vinicius/projetos/checkti/

## O que faz

A pessoa descreve o problema com as próprias palavras. O JavaScript compara a descrição com palavras-chave e monta uma checklist inicial para um dos tipos de problema previstos:

- Computador que não liga
- Computador lento ou travando
- Falta de internet
- Falta de áudio
- Computador liga, mas não aparece imagem
- Aquecimento ou desligamento inesperado
- Teclado, mouse ou touchpad sem funcionar

Também há botões para selecionar rapidamente alguns problemas comuns. Cada passo pode ser marcado, a página mostra o progresso e permite limpar as marcações.

## Tecnologias usadas

- **HTML:** estrutura da página, formulário e checklists.
- **CSS:** visual da página e adaptação para telas menores.
- **JavaScript:** leitura do texto, identificação por palavras-chave, criação das etapas e atualização do progresso.

O projeto não usa banco de dados, bibliotecas externas, login, servidor ou API de IA. A identificação é feita por regras simples e uma lista de palavras-chave no próprio código; por isso, não entende todos os tipos de descrição e não gera diagnósticos novos como uma inteligência artificial faria.

## Como executar

1. Abra a pasta `projetos/checkti`.
2. Abra o arquivo `index.html` no navegador.
3. Escreva o sintoma principal e clique em **Montar checklist**, ou selecione um dos casos comuns.
4. Marque cada etapa depois de fazer a verificação.

## O que estudar no código

- Como o formulário recebe a descrição digitada.
- Como a função `normalizarTexto` trata acentos e letras maiúsculas.
- Como `identificarProblema` compara a descrição com palavras-chave.
- Como o objeto `problemas` guarda os passos de cada caso.
- Como `addEventListener` reage a envios, cliques e marcações.
- Como a barra de progresso é atualizada.

## Limitações e segurança

O CheckTI só seleciona checklists que já estão cadastradas no código. Se não reconhecer a descrição, pede ao usuário que tente explicar o sintoma de outra forma, em vez de inventar instruções. As etapas são verificações iniciais, não um diagnóstico definitivo. Não abra a fonte de alimentação nem mexa em componentes internos com o equipamento ligado. Se houver cheiro de queimado, líquido, faíscas, cabos danificados ou aquecimento extremo, interrompa os testes e procure assistência qualificada.

## Autor

Vinicius da Motta Campos — projeto de portfólio para praticar desenvolvimento web básico.
