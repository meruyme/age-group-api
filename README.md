# Age group API

## Descrição

A API tem por objetivo realizar o gerenciamento de grupos de faixa etária.

## Configuração do projeto

### Tecnologias

A API foi desenvolvida usando Python 3.9.6, com o framework FastAPI. O banco de dados escolhido foi o MongoDB. Para o gerenciamento das dependências do projeto, foi escolhido o [pip-tools](https://pypi.org/project/pip-tools/).
### Instruções de execução

Crie, na raiz do projeto, um arquivo .env para armazenar suas variáveis de ambiente. Um arquivo de exemplo pode ser encontrado [aqui](.env_example).

Para a criação dos containers no Docker e execução do sistema, execute:
> make local-up

Após iniciar o projeto, é possível encontrar uma documentação detalhada de todas as rotas da API na seguinte URL:
> http://localhost:8001/api/docs

### Testes

Para a criação dos testes, foi utilizada a biblioteca Pytest. 

Para executá-los, utilize o seguinte comando:
> make local-test
