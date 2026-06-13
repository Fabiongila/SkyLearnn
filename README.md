![Group 23](https://github.com/user-attachments/assets/4e84251a-27b0-462b-bd5e-fb0bcadc4694)

### O sistema de gestão de aprendizagem mais elegante, leve e rico em funcionalidades do mundo.

# SkyLearn: sistema de gestão de aprendizagem open source

Sistema de gestão de aprendizagem construído com o framework web Django. Este projeto é ideal se quer desenvolver um sistema de gestão escolar/faculdade, ou simplesmente aprender a stack e enriquecer o seu portfólio. Em qualquer dos casos, este projeto é um ótimo ponto de partida.

O objetivo é criar o sistema de gestão de aprendizagem mais leve e completo possível. No entanto, isso só é possível com o seu apoio, por isso dê uma estrela ⭐️.

_Documentação em desenvolvimento_

Vamos melhorar o projeto com a sua contribuição! 👩‍💻👩‍💻

<img width="1440" alt="screenshot" src="https://github.com/user-attachments/assets/08644f49-6ae0-4695-86cc-afe331c6f61a">

## Funcionalidades atuais

- Dashboard: demografia escolar e análises. Restrito apenas a administradores
- Notícias e Eventos: todos os utilizadores podem aceder a esta página
- Admin gere estudantes (Adicionar, Atualizar, Eliminar)
- Admin gere docentes (Adicionar, Atualizar, Eliminar)
- Os estudantes podem adicionar e abandonar disciplinas
- Os professores submetem as notas dos estudantes: _Presença, Exame intermédio, Exame final, trabalho_
- O sistema calcula automaticamente o _Total, média, pontuação e classificações_ dos estudantes
- Comentário de classificação para cada estudante com **aprovado**, **reprovado** ou **aprovado com aviso**
- Página de resultado de avaliação para estudantes
- Página de resultado de classificação para estudantes
- Gestão de ano/época e semestre
- Avaliações e notas agrupadas por semestre
- Upload de vídeo e documentação para cada curso
- Gerador de PDF para talão de inscrição e resultado de avaliação dos estudantes
- Restrição de acesso a páginas
- Armazenamento dos resultados de quiz para cada utilizador
- Randomização da ordem das perguntas
- Resultados de quizzes anteriores podem ser vistos na página de categoria
- As respostas corretas podem ser mostradas após cada pergunta ou todas de uma vez no final
- Utilizadores autenticados podem retomar um quiz incompleto para o terminar e utilizadores não autenticados também podem completar um quiz se a sessão persistir
- O quiz pode ser limitado a uma tentativa por utilizador
- As perguntas podem ser atribuídas a uma categoria
- A taxa de sucesso de cada categoria pode ser monitorizada numa página de progresso
- Explicações para cada resultado de pergunta podem ser mostradas
- A nota de aprovação pode ser definida
- Tipo de pergunta de escolha múltipla
- Tipo de pergunta Verdadeiro/Falso
- Tipo de pergunta dissertativa................._Em breve_
- Mensagem personalizada exibida para quem aprova ou reprov a um quiz
- Permissão personalizada (`view_sittings`) adicionada, permitindo a utilizadores com essa permissão ver resultados de quizzes de outros utilizadores
- Página de marcação que lista quizzes concluídos, pode ser filtrada por quiz ou utilizador e serve para avaliar perguntas dissertativas

# Nota rápida para futuros contribuidores

Se quiser contribuir, comece por implementar algo da lista no ficheiro `TODO.md`.

# Requisitos

> Os seguintes programas são necessários para correr o projeto

- [Python3.8+](https://www.python.org/downloads/)

# Instalação

- Clone o repositório com

```bash
git clone https://github.com/SkyCascade/SkyLearn.git
```

- Crie e ative um ambiente virtual Python

```bash
pip install -r requirements.txt
```

- Crie o ficheiro `.env` na raiz do projeto

- Copie e cole tudo o que está no ficheiro `.env.example` para o `.env`. Não se esqueça de personalizar os valores das variáveis

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

```bash
python manage.py runserver
```

Por fim, aceda a este endereço: http://127.0.0.1:8000

#### _Veja [esta página](https://adilmohak.github.io/dj-lms-starter/) para mais informação e suporte._

# Referências

- Parte de quiz: https://github.com/tomwalker/django_quiz

#### Mostre o seu apoio com uma estrela ⭐️ neste projeto!
