### Termos e acordos

Ao iniciar este projeto, você concorda com as diretrizes do Código de Ética e Conduta e do
Manual da Pessoa Estudante da Trybe.

# Boas vindas ao repositório do projeto de Algorithms!

Você já usa o GitHub diariamente para desenvolver os exercícios, certo? Agora, para desenvolver os projetos, você deverá seguir as instruções a seguir. Fique atento a cada passo, e se tiver qualquer dúvida, nos envie por _Slack_! #vqv 🚀

Aqui você vai encontrar os detalhes de como estruturar o desenvolvimento do seu projeto a partir desse repositório, utilizando uma branch específica e um _Pull Request_ para colocar seus códigos.

---
# Sumário

- [Boas vindas ao repositório do projeto de Algorithms!](#boas-vindas-ao-repositório-do-projeto-de-algorithms)
- [Sumário](#sumário)
- [Habilidades](#habilidades)
  - [Entregáveis](#entregáveis)
    - [⚠️ É importante que seus arquivos tenham exatamente estes nomes! ⚠️](#️-é-importante-que-seus-arquivos-tenham-exatamente-estes-nomes-️)
  - [O que deverá ser desenvolvido](#o-que-deverá-ser-desenvolvido)
  - [Desenvolvimento](#desenvolvimento)
    - [Data de Entrega](#data-de-entrega)
  - [Instruções para entregar seu projeto:](#instruções-para-entregar-seu-projeto)
    - [ANTES DE COMEÇAR A DESENVOLVER:](#antes-de-começar-a-desenvolver)
    - [Durante o desenvolvimento](#durante-o-desenvolvimento)
  - [Linter](#linter)
  - [Testes](#testes)
  - [Requisitos do projeto](#requisitos-do-projeto)
      - [1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)](#1---número-de-estudantes-estudando-no-mesmo-horário-algoritmo-de-busca)
      - [2 - Palíndromos (Recursividade)](#2---palíndromos-recursividade)
      - [3 - Anagramas (Algoritmo de ordenação)](#3---anagramas-algoritmo-de-ordenação)
    - [Requisitos bônus:](#requisitos-bônus)
      - [4 - Encontrando números repetidos (Algoritmo de busca)](#4---encontrando-números-repetidos-algoritmo-de-busca)
      - [5 - Palíndromos (Iteratividade)](#5---palíndromos-iteratividade)
    - [Depois de terminar o desenvolvimento](#depois-de-terminar-o-desenvolvimento)
    - [Revisando um pull request](#revisando-um-pull-request)
- [Avisos Finais](#avisos-finais)

    `Requisitos obrigatórios:`
    - [1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)](#1---número-de-estudantes-estudando-no-mesmo-horário-algoritmo-de-busca)
    - [2 - Palíndromos (Recursividade)](#2---palíndromos-recursividade)
    - [3 - Anagramas (Algoritmo de ordenação)](#3---anagramas-algoritmo-de-ordenação)

    `Requisitos bônus:`
    - [4 - Encontrando números repetidos (Algoritmo de busca)](#4---encontrando-números-repetidos-algoritmo-de-busca)
    - [5 - Palíndromos (Iteratividade)](#5---palíndromos-iteratividade)
- [Depois de terminar o desenvolvimento](#depois-de-terminar-o-desenvolvimento)
- [Revisando um pull request](#revisando-um-pull-request)
- [Avisos Finais](#avisos-finais)

# Habilidades

  - Estrutura de dados

  - Complexidade de algoritimos

  - Capacidade de interpretação do problema;

  - Capacidade de resolução do problema, de forma otimizada;
  
  - Analisar corretamente a ordem de complexidade de um algoritmo.

  - Recursividade

  - Algoritmos de ordenação e algoritmos de busca

---

## Entregáveis

Para entregar o seu projeto você deverá criar um _Pull Request_ neste repositório. Este _Pull Request_ deverá conter os arquivos `challenge_anagrams.py`, `challenge_find_the_duplicate.py`, `challenge_palindromes_iterative.py`, `challenge_palindromes_recursive.py` e `challenge_study_schedule.py`, que conterão seu código `Python`, respectivamente.

### ⚠️ É importante que seus arquivos tenham exatamente estes nomes! ⚠️

Você pode adicionar outros arquivos se julgar necessário. Qualquer dúvida, procure a monitoria.

Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://course.betrybe.com/intro/git/) sempre que precisar!

---

## O que deverá ser desenvolvido

Para fixar os conteúdos de algoritmos e estrutura de dados vistos até agora, você fará um projeto que tem como principal objetivo resolver problemas e otimizar algoritmos do tipo que aparecem em inúmeros processos de entrevista por _whiteboard_ e que vão acelerar muito a sua capacidade de resolver problemas!

Pessoas desenvolvedoras de software, além de serem muito boas em implementações, devem, também, ser boas resolvendo problemas e otimizando algoritmos. No projeto de hoje, vamos treinar, ainda mais, a sua capacidade de resolução de problemas e otimização de código, que envolve algumas habilidades:

  - Lógica;

  - Capacidade de interpretação do problema;

  - Capacidade de interpretação de um código legado;

  - Capacidade de resolução do problema, de forma otimizada;

  - Resolver o problemas/Otimizar algoritmos mesmo sob pressão.

Tendo essas habilidades descritas acima, junto com algumas outras, farão de você uma pessoa desenvolvedora que terá muita facilidade em diversas situações problemáticas do dia-a-dia.

---

## Desenvolvimento

Este repositório é composto por uma pasta, `challenges`. Essa pasta contém todos os arquivos que você utilizará nesse projeto.

Cada arquivo `.py`, dentro da pasta `challenges`, representa um requisito. Ou seja, os arquivos não tem ligação uns com os outros. Logo, os problemas devem ser resolvidos de forma separada.

Este repositório já contém um _template_ com a estrutura de diretórios e arquivos,. Veja abaixo:

```md
.
├── challenges
│   ├── challenge_anagrams.py
│   ├── challenge_find_the_duplicate.py
│   ├── challenge_palindromes_iterative.py
│   ├── challenge_palindromes_recursive.py
│   └── challenge_study_schedule.py
├── README.md
├── requirements.txt
└── setup.cfg
```

Apesar do projeto já possuir uma estrutura base, você quem deve implementar as funções. Novos arquivos podem ser criados conforme a necessidade.

Lembre-se de primeiro **criar e ativar o ambiente virtual**, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r dev-requirements.txt
```

O arquivo `requirements.txt` contém todos as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse artigo: https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1

Para verificar se você está seguindo o guia de estilo do Python corretamente, execute o comando:

```bash
$ python3 -m flake8
```

Para executar cada arquivo separadamente, execute o comando:

```bash
$ python3 nome_do_arquivo.py
```

---

### Data de Entrega

  - Serão `X` dias de projeto.
  - Data de entrega para avaliação final do projeto: `DD/MM/YYYY - 14:00h`.

---

## Instruções para entregar seu projeto:

### ANTES DE COMEÇAR A DESENVOLVER:

1. Clone o repositório

- `git clone https://github.com/tryber/sd-0x-project-algorithms.git`.
- Entre na pasta do repositório que você acabou de clonar:
  - `sd-0x-project-algorithms`

2. Crie o ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

3. Crie uma branch a partir da branch `master`

- Verifique que você está na branch `master`
  - Exemplo: `git branch`
- Se não estiver, mude para a branch `master`
  - Exemplo: `git checkout master`
- Agora crie uma branch à qual você vai submeter os `commits` do seu projeto
  - Você deve criar uma branch no seguinte formato: `nome-github-nome-do-projeto`
  - Exemplo: `git checkout -b exemplo-project-algorithms`

4. Adicione as mudanças ao _stage_ do Git e faça um `commit`

- Verifique que as mudanças ainda não estão no _stage_
  - Exemplo: `git status` (deve aparecer listada a pasta _exemplo_ em vermelho)
- Adicione o novo arquivo ao _stage_ do Git
  - Exemplo:
    - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
    - `git status` (deve aparecer listado o arquivo _exemplo/README.md_ em verde)
- Faça o `commit` inicial
  - Exemplo:
    - `git commit -m 'iniciando o projeto algorithms'` (fazendo o primeiro commit)
    - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

5. Adicione a sua branch com o novo `commit` ao repositório remoto

- Usando o exemplo anterior: `git push -u origin exemplo-project-name`

6. Crie um novo `Pull Request` _(PR)_

- Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/tryber/sd-0x-project-algorithms/pulls)
- Clique no botão verde _"New pull request"_
- Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
- Clique no botão verde _"Create pull request"_
- Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
- **Não se preocupe em preencher mais nada por enquanto!**
- Volte até a [página de _Pull Requests_ do repositório](https://github.com/tryber/sd-0x-project-algorithms/pulls) e confira que o seu _Pull Request_ está criado

---

### Durante o desenvolvimento

* ⚠ **PULL REQUESTS COM ISSUES NO LINTER NÃO SERÃO AVALIADAS, ATENTE-SE PARA RESOLVÊ-LAS ANTES DE FINALIZAR O DESENVOLVIMENTO!** ⚠

* Faça `commits` das alterações que você fizer no código regularmente

* Lembre-se de sempre após um (ou alguns) `commits` atualizar o repositório remoto

* Os comandos que você utilizará com mais frequência são:
  1. `git status` _(para verificar o que está em vermelho - fora do stage - e o que está em verde - no stage)_
  2. `git add` _(para adicionar arquivos ao stage do Git)_
  3. `git commit` _(para criar um commit com os arquivos que estão no stage do Git)_
  4. `git push` _(para enviar o commit para o repositório remoto após o passo anterior)_
  5. `git push -u nome-da-branch` _(para enviar o commit para o repositório remoto na primeira vez que fizer o `push` de uma nova branch)_

---

## Linter

Para garantir a qualidade do código, vamos utilizar neste projeto o linter `Flake8`.
Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comandos abaixo:

  ```bash
python3 -m flake8
```

⚠️ **PULL REQUESTS COM ISSUES DE LINTER NÃO SERÃO AVALIADAS.
ATENTE-SE PARA RESOLVÊ-LAS ANTES DE FINALIZAR O DESENVOLVIMENTO!** ⚠️

---

## Testes

Com as dependências já instaladas basta executar o comando:

```bash
python3 -m pytest
```

Com esse comando irá executar todos os testes do projeto.

Caso o teste falhe e você queira ter um print melhor do erro basta executar o seguinte comando:

```bash
python3 -m pytest -s -vv
```

Caso precise executar apenas um arquivo de testes basta executar o comando:

```bash
python3 -m pytest tests/nomedoarquivo.py
```

## Requisitos do projeto

#### 1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)

Você trabalha na maior empresa de educação do Brasil. Um certo dia, sua/seu `PM` quer saber qual horário tem a maior quantidade de pessoas acessando o conteúdo da plataforma ao mesmo tempo. Com esse dado em mãos, o/a PM saberá qual é o melhor horário para disponibilizar os materiais de estudo para ter o maior engajamento possível no sistema.

Toda vez que uma pessoa estudante abre o sistema, é cadastrado no banco de dados o horário de entrada. Da mesma forma funciona quando o estudante sai do sistema, é cadastrado no banco de dados o horário de saída. Esses dados estarão contidos em uma lista de tuplas (`permanence_period`) onde cada tupla representa o período de permanência de uma pessoa estudante com seu horário de entrada e de saída

Seu trabalho é descobrir qual o melhor horário para disponibilizar os conteúdos. Para achar o horário, será utilizada `força bruta`. Ou seja, para achar o melhor horário, a função que você desenvolver será chamada várias vezes com valores diferentes para a variável `target_time`, e serão analisados os retornos da função.

_Dica:_ Quando vou saber qual o melhor horário? Quando o contador retornado pela função for o maior.

**Exemplo:**

```md
# Nos arrays temos 6 estudantes

# estudante             1       2       3       4       5       6
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

target_time = 5  # saída: 3, pois a quarta, a quinta e a sexta pessoa estudante ainda estavam estudando nesse horário.
target_time = 4  # saída: 3, pois a quinta e a sexta pessoa estudante começaram a estudar nesse horário e a quarta ainda estava estudando.
target_time = 3  # saída: 2, pois a terceira e a quarta pessoa estudante ainda estavam estudando nesse horário.
target_time = 2  # saída: 4, pois a primeira, a segunda, a terceira e a quarta pessoa estudante estavam estudando nesse horário.
target_time = 1  # saída: 2, pois a segunda e a quarta pessoa estudante estavam estudando nesse horário.

Para esse exemplo, depois de rodar a função para todos esses `target_times`, julgamos que o melhor horário é o `2`, pois esse retornou `4`, já que 4 estudantes estavam presentes nesse horário!
```

- Este requisito será testado executando 10.000 vezes sobre uma mesma entrada. Tais execuções, **no avaliador**, devem acontecer integralmente em menos de 0.02 segundos. O tempo de execução do código na sua máquina pode variar em relação ao avaliador, então é importante levar somente ele em consideração.

**Dica:** use um algoritmo de, no máximo, complexidade `O(n)`

- Algoritmo deve utilizar a solução iterativa;

- Caso o `target_time` passado seja nulo, o valor retornado pela função deve ser `None` (considere o horário 0 como um horário válido);

- Código deve ser feito dentro do arquivo `challenges/challenge_study_schedule.py`.

**O que será verificado:**

- 1.1 - Retorne, para uma entrada específica, a quantidade de estudantes presentes

- 1.2 - Retorne `None` se em `permanence_period` houver alguma entrada inválida

- 1.3 - Retorne `None` se  `target_time` recebe um valor vazio

- 1.4 - A função poderá, em menos que 0.02s, ser executada 10.000 vezes para uma entrada pequena (tempo da execução do avaliador no Pull Request)

#### 2 - Palíndromos (Recursividade)

Dado uma _string_, determine se ela é um palíndromo ou não. Escreva uma função que irá determinar se uma _string_ é um palíndromo ou não. Um palíndromo é uma _string_, uma palavra, em que não faz diferença se ela é lida da esquerda para a direita ou vice-versa, pois ela mantêm o mesmo sentido. Por exemplo, `"ABCBA"`.

_Curiosidade:_ Existem frases palíndromas também, porém nesse exercício iremos fazer uma função que identifique apenas as palavras palíndromas.

**Exemplos:**

```md
word = "ANA"
# saída: True

word = "SOCOS"
# saída: True

word = "REVIVER"
# saída: True

word = "COXINHA"
# saída: False

word = "AGUA"
# saída: False
```

- O algoritmo deve ser feito utilizando a solução recursiva;

- Não se preocupe com a analise da complexidade desse algoritmo;

- Se for passado uma _string_ vazia, retorne `False`;

- Código deve ser feito dentro do arquivo `challenges/challenge_palindromes_recursive.py`.

**O que será verificado:**

- 2.1 - Retorne `true` se a palavra passada por parâmetro for um palíndromo

- 2.2 - Retorne `false` se a palavra passada por parâmetro não for um palíndromo

- 2.3 - Retorne `false` se nenhuma palavra for passada por parâmetro

#### 3 - Anagramas (Algoritmo de ordenação)

Faça um algoritmo que consiga comparar duas _strings_ e identificar se uma é um anagrama da outra. Ou seja, sua função irá receber duas strings de parâmetro e o retorno da função será um _booleano_, `True` ou `False`.

Mas o que é um anagrama? Vamos ver sua definição para entendermos melhor:

> "Um anagrama é uma espécie de jogo de palavras criado com a reorganização das letras de uma palavra ou expressão para produzir outras palavras ou expressões, utilizando todas as letras originais exatamente uma vez."

**Exemplo:**

```md
first_string = "amor"
second_string = "roma"
# saída: True
# Explicação: Nesse caso o retorno da função é True, pois a palavra "roma" é um anagrama de "amor".


first_string = "pedra"
second_string = "perda"
# saída: True
# Explicação: Nesse caso o retorno também é True. Na palavra "pedra", trocamos o "d" de lugar com o "r" e formamos "perda", sendo assim um anagrama.  


first_string = "pato"
second_string = "tapo"
# saída: True


# Agora vamos pra um exemplo onde não existe um anagrama
first_string = "coxinha"
second_string = "empada"
# saída: False
```

- Este requisito será testado executando 10.000 vezes sobre uma mesma entrada. Tais execuções, **no avaliador**, devem acontecer integralmente em menos de 2 segundos. O tempo de execução do código na sua máquina pode variar em relação ao avaliador, então é importante levar somente ele em consideração.

**Dica:** use um algoritmo de, no máximo, complexidade `O(n log n)`

- Utilize qualquer algoritmo que quiser (_Selection sort_, _Insertion sort_, _Bubble sort_, _Merge sort_, _Quick sort_ ou _TimSort_), desde que atinja a complexidade `O(n log n)`. Ou seja, preste bastante atenção na escolha do algoritmo e na implementação do mesmo;

- ⚠ *Você deverá implementar sua própria função de ordenação*, ou seja, o uso de funções prontas não é permitido. **Exemplos de funções não permitidas:** _*sort*, *sorted* e *Counter*._

- A função retorna `True` caso uma _string_ seja um anagrama da outra;

- A função retorna `False` caso uma _string_ **não seja** um anagrama da outra;

- Código deve ser feito dentro do arquivo `challenges/challenge_anagrams.py`.

**O que será verificado:**

- 3.1 - Retorne `true` se as palavras passadas forem anagramas

- 3.2 - Retorne `false` se as palavras passadas por parâmetro não forem anagramas

- 3.3 - Retorne `false` se alguma das palavras passadas por parâmetro for uma string vazia

- 3.4 - Execute a função, somando 10.000 execuções para uma entrada pequena, em menos que 8.2s (tempo da execução do avaliador no Pull Request)

### Requisitos bônus:

#### 4 - Encontrando números repetidos (Algoritmo de busca)

Dada um _array_ de números inteiros contendo `n + 1` inteiros, chamado de `nums`, onde cada inteiro está no intervalo `[1, n]`.

Retorne apenas um número duplicado em `nums`.

**Exemplo:**

```md
nums = [1, 3, 4, 2, 2]
# saída: 2

nums = [3, 1, 3, 4, 2]
# saída: 3

nums = [1, 1]
# saída: 1

nums = [1, 1, 2]
# saída: 1

nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
# saída: 7
```
- Caso não passe nenhum valor ou uma string ou não houver números repetidos retorne false;

- Este requisito será testado executando 10.000 vezes sobre uma mesma entrada. Tais execuções, **no avaliador**, devem acontecer integralmente em menos de 0.01 segundos. O tempo de execução do código na sua máquina pode variar em relação ao avaliador, então é importante levar somente ele em consideração.

**Dica:** use um algoritmo de, no máximo, complexidade `O(n log n)`

- O array montado deve:

  - Ter apenas números inteiros positivos maiores do que 1;

  - Ter apenas um único número repetindo duas ou mais vezes, todos os outros números devem aparecer apenas uma vez;

  - Ter, no mínimo, dois números.

- Código deve ser feito dentro do arquivo `challenge_find_the_duplicate.py`.

_Dica:_ Ordene o array.

**O que será verificado:**

- 4.1 - Retorne o número repetivo se a função receber, como parâmetro, uma lista com números repetidos

- 4.2 - Retorne `false` se a função não receber nenhum parâmetro

- 4.3 - Retorne `false` se a função receber, como parâmetro, uma string

- 4.4 - Retorne `false` se a função receber, como parâmetro, uma lista sem números repetidos

- 4.5 - Retorne `false` se a função receber, como parâmetro, apenas um valor

- 4.6 - Retorne `false` se a função receber, como parâmetro, um número negativo

- 4.7 - Execute a função, somando 10.000 execuções para uma entrada pequena, em menos que 0.01s (tempo da execução do avaliador no Pull Request)

#### 5 - Palíndromos (Iteratividade)

Resolva o mesmo problema, apresentado no [requisito dois](####-2---Palíndromos-(Recursividade)), porém dessa vez utilizando a solução iterativa.

- Este requisito será testado executando 10.000 vezes sobre uma mesma entrada. Tais execuções, **no avaliador**, devem acontecer integralmente em menos de 0.005 segundos. O tempo de execução do código na sua máquina pode variar em relação ao avaliador, então é importante levar somente ele em consideração.

**Dica:** use um algoritmo de, no máximo, complexidade `O(n)`

- Algoritmo deve utilizar a solução iterativa;

- Código deve ser feito dentro do arquivo `challenge_palindromes_iterative.py`.

**O que será verificado:**

- 5.1 - Retorne `true` se a palavra passada como parâmetro for um palíndromo, executando uma função iterativa

- 5.2 - Retorne true se a palavra passada como parâmetro for um palíndromo, executando uma função iterativa

- 5.3 - Retorne `false` se nenhuma palavra for passada como parâmetro, executando uma função iterativa

- 5.4 - Execute a função, somando 10.000 execuções para uma entrada pequena, em menos que 0.005s (tempo da execução do avaliador no Pull Request)

---

### Depois de terminar o desenvolvimento

Para **"entregar"** seu projeto, siga os passos a seguir:

* Vá até a página **DO SEU** _Pull Request_, adicione a label de _"code-review"_ e marque seus colegas
  * No menu à direita, clique no _link_ **"Labels"** e escolha a _label_ **code-review**
  * No menu à direita, clique no _link_ **"Assignees"** e escolha **o seu usuário**
  * No menu à direita, clique no _link_ **"Reviewers"** e digite `students`, selecione o time `tryber/students-sd-0x`

Se ainda houver alguma dúvida sobre como entregar seu projeto, [aqui tem um video explicativo](https://vimeo.com/362189205).

⚠ Lembre-se que garantir que todas as _issues_ comentadas pelo **Lint** estão resolvidas! ⚠

---

### Revisando um pull request

À medida que você e as outras pessoas que estudam na Trybe forem entregando os projetos, vocês receberão um alerta via Slack para também fazer a revisão dos Pull Requests dos seus colegas. Fiquem atentos às mensagens do "Pull Reminders" no Slack!

Use o material que você já viu sobre [Code Review](https://course.betrybe.com/real-life-engineer/code-review/) para te ajudar a revisar os projetos que chegaram para você.

---

# Avisos Finais

Ao finalizar e submeter o projeto, não se esqueça de avaliar sua experiência preenchendo o formulário. Leva menos de 3 minutos!

Link: [FORMULÁRIO DE AVALIAÇÃO DE PROJETO](https://be-trybe.typeform.com/to/ZTeR4IbH)

O avaliador automático não necessariamente avalia seu projeto na ordem em que os requisitos aparecem no readme. Isso acontece para deixar o processo de avaliação mais rápido. Então, não se assuste se isso acontecer, ok?

---
