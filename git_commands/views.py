import importlib
from django.shortcuts import render
from django.http import response, HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
git_commands_to_group_dict = {"remote": "synch", "add": "save", "commit": "save", "log": "save", "diff": "save", "pull": "publish", "push": "publish", "branch": "branches", "checkout": "branches", "merge": "branches", "revert": "branches", "stash": "branches"}
git_group_dict = {
    # Команды для синхронизации локального репозитория с удалённым.
    'synch': [
        "Команды для синхронизации локального репозитория с удалённым.",
        "git remote add origin https://github.com/YandexPracticum/first-project.git — находясь в папке с локальным репозиторием, привязываем его к удалённому (URL у вас будет свой);",
        "git push -u origin main — заливаем все файлы из локального репозитория в удалённый, который уже привязали."
    ],
    # Команды для того чтобы сделать сохранение — коммит.
    'save': [
        "Команды для того чтобы сделать сохранение — коммит.",
        "git add название_файла — готовим выбранный файл к коммиту;",
        "Команды для того чтобы сделать сохранение — коммит.",
        "git add название_файла — готовим выбранный файл к коммиту;",
        "git add -A — чтобы ничего не потерять, можно подготовить к коммиту сразу все файлы, в которых были изменения;",
        'git commit -m "комментарий к коммиту" — делаем коммит. К сохранённым файлам оставляем комментарий для того, чтобы проще было понять, какие сделаны изменения.',
        "Забыл что-то добавить в коммит— git commit --amend:",
        "Запуск команды откроет Vim. Он предложит изменить комментарий к последнему коммиту. Нажмите i, чтобы начать писать, и введите новый комментарий к коммиту. Как закончите, нажмите esc, введите :wq и нажмите Enter. Так вы сохраните новый комментарий и выйдете из Vim.",
        "git log — посмотреть подробный лог коммитов.",
        "git log --oneline — посмотреть короткий просмотр коммитов.",
        "git diff — посмотреть изменения в «рабочей зоне»; они маркируются гитом как modifided, new или deleted.",
        "git diff --staged — посмотреть изменения, добавленные в staged.",
        "git diff a9928ab 11bada1 — сравнить изменения двух коммитов."
    ],
    # Команды для публикации изменений:
    'publish': [
        "Команды для публикации изменений:",
        "git pull — забрать изменения, сделанные другими разработчиками;",
        "git push — опубликовать изменения в удалённый репозиторий."
    ],

    # Команды для работы с ветками:
    'branches':  [
    "Команды для работы с ветками:",
    "git branch название_ветки — создать новую ветку.",
    "git checkout название_ветки — переключиться в ветку.",
    "git checkout -b название_ветки — создать ветку и сразу переключиться в неё.",
    "git branch -D название_ветки — удалить ветку. Чтобы всё прошло хорошо, нужно переключиться из удаляемой ветки.",
    "git merge название_ветки — скопировать все изменения из ветки в ветку. Чтобы перенести изменения из ветки develop в ветку main, нужно находиться в ветке main и ввести git merge develop;",
    "git revert -m основной_родитель хеш_коммита — отмена коммита слияния веток. Опция -m со значением больше 0 указывает на основную ветку, которая будет сохранена.",
    "git revert хеш_коммита — отмена изменений выбранного коммита. Он не был создан при слиянии, поэтому имеет одного предка.",
    "git stash — скрытие незакоммиченных изменений в текущей рабочей ветке. Опция save название_стэша даёт этим изменениям имена.",
    "git stash pop — возврат последних изменений в любой ветке.",
    "git stash list — показ списка спрятанных во всех ветках изменений и, если для стэша не задано имя, последнего коммита в этой ветке.",
    "git stash apply stash@{n} — возврат выбранных спрятанных изменений из листа стэша, где n — номер в нём.",
    "git stash clear — очистка листа стеша.</p>"
    ],

    # Работа с командной строкой - bash
    'bash': [
    "Работа с командной строкой - bash",
    "pwd — покажи в какой я папке",
    "ls — покажи файлы в папке, где я сейчас",
    "cd first-project — перейди в папку first-project",
    "cd first-project/html — перейди в папку html, находящуюся в папке first-project",
    "cd .. — перейди на уровень выше в родительскую папку",
    "cd ~ — перейди в домашнюю директорию (у нас это /Users/stas_basov)",
    "mkdir second-project — в текущей папке создай папку с именем second-project",
    "rm about.html — удали файл about.html",
    "rmdir images — удали папку images",
    "rm -r second-project — удали папку second-project и всё, что она содержит",
    "touch index.html — создай файл index.html в текущей папке",
    "touch index.html style.css script.js — если нужно создать несколько файлов, их имена можно вводить через пробел",
    ],

    'navigation': [
    "Быстрая навигация",
    "↑ — показать предыдущую команду из буфера.",
    "↓ — показать следующую команду из буфера.",
    "Tab — автоматически дописать команду или путь.",
    "Ctrl + A — перейти в начало строки.",
    "Ctrl + E — перейти в конец строки.",
    ],
}


def index(request):
    return render(request, 'git_commands/main_git.html')

def get_git_command(request, git_command):

    if git_command in git_commands_to_group_dict:
        redirect_url = reverse("git", args=(git_commands_to_group_dict[git_command], ))
        return HttpResponseRedirect(redirect_url)

    else:
        return get_git_command_by_group(request, git_command)


def get_git_command_by_group(request, git_command):

    if git_command in git_group_dict:
        description = git_group_dict[git_command]
        data = {
            # "command_group_name": description[0],
            # "command_group_description": description[1::]
            "command": description[0],
            "command_info": description[1:]
        }
        return render(request, 'git_commands/info_git.html', context=data)

    else:
        return response.HttpResponseNotFound(f"Not found - {git_command}")
