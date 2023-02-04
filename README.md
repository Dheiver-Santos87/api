# api

Esta API é uma aplicação Streamlit que usa um modelo de aprendizado profundo (CNN) treinado em imagens de câncer de mama para prever se uma imagem de mama é benigna, maligna ou normal. O usuário pode fazer upload de uma imagem de mama e a API retornará uma previsão sobre a condição da imagem.

A API começa carregando o modelo treinado, que foi salvo no arquivo my_model.h5. Em seguida, a API fornece um uploader de arquivos para que o usuário possa fazer upload da imagem de interesse. Depois que a imagem é carregada, a API processa a imagem, redimensionando-a para 224x224 pixels e expandindo suas dimensões. Finalmente, a API usa o modelo para fazer uma previsão sobre a condição da imagem e retorna o resultado para o usuário.

A API foi criada por Dr. Dheiver Francisco Santos, e pode ser encontrada em seu Instagram @santos.dheiver e em seu site dheiver.com.br. Algumas sugestões de melhoria para a API incluem adicionar uma descrição detalhada sobre o funcionamento da aplicação e do modelo, adicionar uma barra de progresso durante o processamento da imagem, e adicionar uma opção para o usuário selecionar o tamanho da imagem (resolução) antes de fazer o upload.

Este é um aplicativo de Streamlit que permite fazer upload de uma imagem de mama e prever se a imagem é benigna, maligna ou normal. O seguinte é um passo a passo para usar a API:

Instale as bibliotecas necessárias: streamlit, tensorflow, numpy e PIL
Carregue o modelo usando a função load_model() e salve-o como uma variável global.
Adicione um upload de arquivo na sua aplicação para permitir que o usuário faça o upload de uma imagem de mama.
Processar a imagem usando a função predict_class() para prever se a imagem é benigna, maligna ou normal.
Exibir o resultado da previsão para o usuário.
Observe que este código de exemplo é apenas um ponto de partida e pode ser personalizado para atender às suas necessidades.

Exemplo de Integração da API a um back-end e front-end usando Flask e React:

Back-end com Flask:
a. Instale o Flask usando o gerenciador de pacotes Python (pip):
$ pip install Flask
b. Crie uma nova aplicação Flask, adicionando o seguinte código a um arquivo chamado "app.py":
c. Inicie o servidor Flask executando o seguinte comando no terminal:
$ python app.py

Front-end com React:
a. Instale o React usando o gerenciador de pacotes NPM (npm):
$ npm install -g create-react-app
b. Crie uma nova aplicação React, executando o seguinte comando no terminal:
$ npx create-react-app my-app
c. Adicione o seguinte código ao arquivo "src/App.js"
No backend, criar uma rota para receber as requisições de previsão de imagem, onde a rota pode usar a função predict_class para executar a previsão usando o modelo carregado e retornar a previsão para o front-end.

No front-end, usar React para desenvolver a interface do usuário e fazer requisições à rota criada no backend para enviar a imagem selecionada pelo usuário e exibir a previsão retornada pelo backend na tela.

Esses são os passos gerais para integrar a API a um back-end e front-end usando Flask e React. É importante notar que esses passos precisam ser implementados em detalhes e pode haver outras etapas envolvidas, como a configuração de servidores e outras dependências.
