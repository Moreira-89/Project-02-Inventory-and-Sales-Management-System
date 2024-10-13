# Projeto: Sistema de Gestão de Estoque e Vendas para Oficina Mecânica <br>

Este projeto visa desenvolver um sistema de gestão de estoque e vendas para uma oficina mecânica. O objetivo principal é otimizar a organização do estoque, garantir a disponibilidade de peças e melhorar a eficiência no atendimento ao cliente. O sistema incluirá funcionalidades para gerenciamento de contas, clientes, produtos e pedidos. <br>

Para acessar o sistema basta clicar >> [aqui](https://sistema-gerenciamento-estoque-vendas.streamlit.app/) <<

### Funcionalidades

- __Gestão de Contas:__ Controle de usuários e permissões para acesso ao sistema.
- __Gestão de Clientes:__ Cadastro, atualização e gerenciamento de informações dos clientes.
- __Gestão de Produtos:__ Controle de entrada e saída de peças e produtos.
- __Gestão de Pedidos:__ Controle e registro de pedidos de serviços e peças.

### Estrutura do Projeto

- `app/`: Diretório principal que contém toda a lógica da aplicação.
    - `main.py`: Arquivo de entrada principal da aplicação.
    - `pages/`: Diretório que organiza todas as páginas do projeto. Contém subdiretórios específicos para cada parte do sistema, como `dashboard`, `reports`, `customers`, `inventory`, `orders`, e `authentication`.
    - `utils/`: Contém funções auxiliares, como autenticação e carregamento de dados.

- `assets/`: Diretório que armazena arquivos estáticos (imagens, CSVs, e outros tipos de arquivos que podem ser usados na aplicação).
- `.streamlit/`: Configurações do Streamlit, como o arquivo `config.toml`, que controla aspectos visuais (tema, layout) e de comportamento do aplicativo.
- `requirements.txt`: Lista de dependências necessárias para rodar o projeto. Isso inclui bibliotecas como streamlit, pandas, entre outras.

## Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/) - Framework para aplicações web em Python
- [Pandas](https://pandas.pydata.org/) - Biblioteca para análise de dados
- [NumPy](https://numpy.org/) - Biblioteca para computação numérica <br>

Para instalar todas as bibliotecas na versão corretas que o projeto utiliza é só colocar o seguinte código no terminal da sua IDE: 

```python
pip install -r requirements.txt
```

