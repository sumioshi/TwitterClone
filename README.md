# 🐦 Twitter Clone

Este é um projeto de um clone simplificado do Twitter desenvolvido como parte de um desafio final. A aplicação permite que usuários se registrem, façam login, publiquem tweets, visualizem um feed e excluam seus próprios tweets. Todo o projeto foi desenvolvido com foco na simplicidade, seguindo as diretrizes fornecidas.

## 📋 Funcionalidades

- **Registro de Usuário**: Usuários podem se registrar com um nome de usuário e senha.
- **Autenticação**: Sistema de login para acessar o feed.
- **Feed de Tweets**: Visualização dos tweets em ordem cronológica, do mais recente para o mais antigo.
- **Postagem de Tweets**: Usuários logados podem criar novos tweets.
- **Exclusão de Tweets**: Apenas o autor de um tweet pode excluí-lo.
- **Sistema de Mensagens**: Feedbacks visuais para ações de sucesso ou erro, como login bem-sucedido ou falha de autenticação.

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- **Python 3.8+**
- **pipenv** (gerenciador de ambientes e dependências)

### Passos para Executar o Projeto

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/twitter-clone.git
    cd twitter-clone
    ```

2. **Instale as dependências do projeto:**

    ```bash
    pipenv install
    ```

3. **Ative o ambiente virtual:**

    ```bash
    pipenv shell
    ```

4. **Realize as migrações do banco de dados:**

    ```bash
    python manage.py migrate
    ```

5. **Crie um superusuário (opcional, para acessar o painel de administração):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

7. **Acesse a aplicação no navegador:**

    - URL: `http://127.0.0.1:8000/`

### 🧑‍💻 Credenciais de Teste

- Para facilitar os testes, você pode usar as seguintes credenciais pré-criadas:
    - **Usuário:** testuser
    - **Senha:** testpassword

## 📚 Estrutura do Projeto

- **Página de Login**: Tela inicial onde usuários não autenticados são direcionados.
- **Página de Registro**: Caso o usuário não tenha conta, ele pode criar uma.
- **Feed de Tweets**: Uma vez logado, o usuário tem acesso ao feed onde são exibidos todos os tweets.
- **Postagem de Tweets**: Um formulário no topo do feed permite que o usuário poste novos tweets.
- **Exclusão de Tweets**: Botão de exclusão disponível apenas para o autor do tweet.

## 🛠️ Tecnologias Utilizadas

- **Django 5.0**: Framework principal para o desenvolvimento do back-end.
- **Bootstrap 5.3**: Utilizado para estilização e responsividade.
- **Font Awesome**: Biblioteca de ícones.
- **SQLite**: Banco de dados padrão para desenvolvimento.

## 📝 Descrição do Enunciado e Implementação

O desafio consistia em construir um clone simplificado do Twitter com as seguintes funcionalidades:

1. **Login e Registro**: Implementamos páginas de login e registro com controle de acesso para impedir que usuários não autenticados acessem o feed.

2. **Feed de Tweets**: Criamos um feed funcional, exibindo tweets em ordem cronológica e permitindo a criação de novos tweets.

3. **Permissões para Exclusão**: Implementamos controle de permissões, garantindo que apenas o autor de um tweet possa excluí-lo.

4. **Sistema de Feedback**: Implementamos mensagens de feedback, como sucesso no login ou falha de autenticação.

Toda a comunicação entre o front-end e o back-end foi feita de forma fluida, seguindo o padrão REST para facilitar as operações de login, postagem e exibição de tweets.

## 🛡️ Considerações de Segurança

- Proteção CSRF (Cross-Site Request Forgery) habilitada.
- Restrições de acesso a rotas protegidas para usuários não autenticados.
- Senhas armazenadas de forma segura utilizando hash.

## 🖼️ Prévia Visual
https://github.com/user-attachments/assets/9af31210-278c-44a7-9d3e-3216ab58c05d

---

Espero que você aproveite este projeto! Qualquer dúvida ou sugestão, fique à vontade para entrar em contato.

