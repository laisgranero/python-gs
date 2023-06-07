# README

## Descrição do projeto

Esse código faz parte do Share a Bite, uma plataforma de compartilhamento de alimentos que conecta fornecedores a organizações dedicadas ao combate à fome para que haja o aproveitamento de alimentos que seriam desperdiçados por alguma razão. 

A Share a Bite nasceu diante do problema da grande quantidade de desperdício de alimentos enfrentado no Brasil, um país onde mais de 33 milhões de pessoas sofrem de fome ou insegurança alimentar. Nossa missão é contribuir com a redução do desperdício de alimentos e da fome no Brasil através da tecnologia, encurtando a distância entre aqueles que têm recursos alimentares à disposição e aqueles que necessitam deles para sobreviver. Através da nossa plataforma, empresas, varejistas ou produtores de alimentos poderão cadastrar seus alimentos que estiverem em boas condições para que ONGs e outras instituições de caridade solicitem os que forem adequados às suas necessidades. O aplicativo também apresenta previsões e formas de entrega desses alimentos.

## Funcionalidades do programa

O programa oferece as seguintes funcionalidades:

1. Para fornecedores:
   1.1. Cadastro de alimentos excedentes:
   - Os fornecedores podem cadastrar alimentos na plataforma informando o nome do alimento e a data de vencimento dele;
   - Utilizando as funcionalidades da biblioteca Datetime para coletar a data atual, conseguimos criar a função calcula_validade() para verificar se o alimento já está vencido ou próximo do vencimento independente do dia em que o código for acessado;
   - Se o alimento estiver vencido, ele não poderá ser compartilhado na plataforma;
   - Caso o alimento vença em menos de 30 dias da data atual, o fornecedor recebe um aviso de que ele precisa ser trocado o quanto antes;
   - Os alimentos cadastrados são armazenados em uma lista e suas validades em outra, para que sejam consultadas por organizações durante a solicitação.

2. Para organizações de combate à fome:
  2.1. Solicitação de alimentos cadastrados na plataforma:
   - Mostramos ao usuário uma lista com os alimentos disponíveis para solicitação e a quantidade de dias restantes para que ele vença;
   - O usuário seleciona o alimento desejado e o adiciona à sua lista de pedidos;
   - Ao ser adicionado a uma lista de pedidos, o alimento é removido da lista de alimentos disponível. O mesmo acontece com a sua validade.

3. Para ambos: 
   3.1. Encerramento do programa:
   - O programa pode ser encerrado a qualquer momento a partir da seleção da opção 3.
   - Nessa etapa são exibidos os pedidos feitos pelo usuário, se aplicável.

## Disclaimers

- O cálculo de validade considera apenas meses com 30 dias e anos com 365 dias, sem levar em conta fatores como meses com quantidade diferente de 30 dias ou anos bissextos. Isso faz com que ele se torne menos preciso, mas ainda é útil para essa solução;
