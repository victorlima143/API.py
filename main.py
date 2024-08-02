from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

#criar o modelo doe dados
class TodoItem(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

#simula um "banco de dados" em memoria
todo_list: List[TodoItem] = []

#rotas para criar uma nova tarefa
@app.post("/todos/", response_model=TodoItem)
def create_todo(todo: TodoItem):
    #adicionar a tarefa na lista
    todo_list.append(todo)
    return

#rota para ler todas as tarefas
@app.get("/todos", response_model=List[TodoItem])
def read_todo():
    return todo_list

#rota para ler uma tarefa em especifico pelo ID
@app.get("/todos/{todo_id}", response_model=TodoItem)
def read_todo(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404,detail="Tarefa não encontrada")

#rota para atualizar uma tarefa existente
@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: int, updated_todo: TodoItem):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            return updated_todo
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

#rota para deletar uma tafera pelo id
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            del todo_list[index]
            return {"message": "Tarefa deletada com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")