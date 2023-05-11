<!--hide-->
# 📒 Todo List API in Python Flask by CL4UD3PT

This is a project that teach on how to create an API using the Flask framework using Python and Pipenv.

## About the project to build

Build a REST API that exposes 3 endpoints to the internet:

```txt
GET /todos
POST /todos
DELETE /todos/<int:position>
```

### 1) GET /todos

Will return the list of all todos like this:

```javascript
[
    {
        "done": true,
        "label": "Sample Todo 1"
    },
    {
        "done": true,
        "label": "Sample Todo 2"
    }
]
```

### 2) POST /todos

This will add a new todo to the list with the following request body:

```javascript
{
    "done": true,
    "label": "Sample Todo 1"
}
```

And return the updated list of todos.

### 3) DELETE /todos/<int:position>

This will remove one todo, based on a given position in the todos list, at the end of the url and return the updated list of todos.

### 🌱 How to start this project

This project comes with the necessary files to start working immediately.

We recommend opening this very same repository using a provisioning tool like [Codespaces](https://4geeks.com/lesson/what-is-github-codespaces) (recommended) or [Gitpod](https://4geeks.com/lesson/how-to-use-gitpod). Alternatively, you can clone it on your local computer using the `git clone` command.

Run `pipenv run start` command in terminal to star the Backend. Don't forget to go to PORTS and change port 3001 to `Visibility: Public` if using Insomnia or Postman to test requests.

💡 Important: Remember to save and upload your code to GitHub by creating a new repository, updating the remote (`git remote set-url origin <your new url>`), and uploading the code to your new repository using the `add`, `commit` and `push` commands from the git terminal.


This and many other projects are built by students as part of the 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) by [Alejandro Sanchez](https://twitter.com/alesanchezr) and many other contributors. Find out more about our [Full Stack Developer Course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer), and [Data Science Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning).
