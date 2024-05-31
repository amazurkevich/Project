import importlib
from django.shortcuts import render
from django.http import response, HttpResponseRedirect

# Create your views here.
git_commands_dict = {"remote": "synch", "add": "save", "commit": "save", "log": "save", "diff": "save", "pull": "publish", "push": "publish", "branch": "branches", "checkout": "branches", "merge": "branches", "revert": "branches", "stash": "branches"}



def get_git_command(request, git_command):
    # Команды для синхронизации локального репозитория с удалённым.
    if git_command in git_commands_dict:
       return HttpResponseRedirect(f"http://127.0.0.1:8000/git_commands/{git_commands_dict[git_command]}")


    if git_command == 'synch':
        return response.HttpResponse("""
            <h3>Команды для синхронизации локального репозитория с удалённым.</h3>
            <p>git remote add origin https://github.com/YandexPracticum/first-project.git — находясь в папке с локальным репозиторием, привязываем его к удалённому (URL у вас будет свой);</p>
            <p>git push -u origin main — заливаем все файлы из локального репозитория в удалённый, который уже привязали.</p>
            """)

    # Команды для того чтобы сделать сохранение — коммит.
    elif git_command == 'save':
        return response.HttpResponse("""
            <h3>Команды для того чтобы сделать сохранение — коммит.</h3>
            <p>git add название_файла — готовим выбранный файл к коммиту;</p>
            <p>git add -A — чтобы ничего не потерять, можно подготовить к коммиту сразу все файлы, в которых были изменения;</p>
            <p>git commit -m "комментарий к коммиту" — делаем коммит. К сохранённым файлам оставляем комментарий для того, чтобы проще было понять, какие сделаны изменения.</p>
            <p>Забыл что-то добавить в коммит— git commit --amend:</p>
            <p>Запуск команды откроет Vim. Он предложит изменить комментарий к последнему коммиту. Нажмите i, чтобы начать писать, и введите новый комментарий к коммиту. Как закончите, нажмите esc, введите :wq и нажмите Enter. Так вы сохраните новый комментарий и выйдете из Vim.</p>
            <p>git log — посмотреть подробный лог коммитов.</p>
            <p>git log --oneline — посмотреть короткий просмотр коммитов.</p>
            <p>git diff — посмотреть изменения в «рабочей зоне»; они маркируются гитом как modifided, new или deleted.</p>
            <p>git diff --staged — посмотреть изменения, добавленные в staged.</p>
            <p>git diff a9928ab 11bada1 — сравнить изменения двух коммитов.</p>
            """)

    # Команды для публикации изменений:
    elif git_command == 'publish':
        return response.HttpResponse("""
            <h3>Команды для публикации изменений:</h3>
            <p>git pull — забрать изменения, сделанные другими разработчиками;</p>
            <p>git push — опубликовать изменения в удалённый репозиторий.</p>
            """)

    # Команды для работы с ветками:
    elif git_command == 'branches':
        return response.HttpResponse("""
            <h3>Команды для работы с ветками:</h3>
            <p>git branch название_ветки — создать новую ветку.</p>
            <p>git checkout название_ветки — переключиться в ветку.</p>
            <p>git checkout -b название_ветки — создать ветку и сразу переключиться в неё.</p>
            <p>git branch -D название_ветки — удалить ветку. Чтобы всё прошло хорошо, нужно переключиться из удаляемой ветки.</p>
            <p>git merge название_ветки — скопировать все изменения из ветки в ветку. Чтобы перенести изменения из ветки develop в ветку main, нужно находиться в ветке main и ввести git merge develop;</p>
            <p>git revert -m основной_родитель хеш_коммита — отмена коммита слияния веток. Опция -m со значением больше 0 указывает на основную ветку, которая будет сохранена.</p>
            <p>git revert хеш_коммита — отмена изменений выбранного коммита. Он не был создан при слиянии, поэтому имеет одного предка.</p>
            <p>git stash — скрытие незакоммиченных изменений в текущей рабочей ветке. Опция save название_стэша даёт этим изменениям имена.</p>
            <p>git stash pop — возврат последних изменений в любой ветке.</p>
            <p>git stash list — показ списка спрятанных во всех ветках изменений и, если для стэша не задано имя, последнего коммита в этой ветке.</p>
            <p>git stash apply stash@{n} — возврат выбранных спрятанных изменений из листа стэша, где n — номер в нём.</p>
            <p>git stash clear — очистка листа стеша.</p>
            """)

    # Работа с командной строкой - bash
    elif git_command == 'bash':
        return response.HttpResponse("""
            <h3>Работа с командной строкой - bash</h3>
            <p>pwd — покажи в какой я папке;</p>
            <p>ls — покажи файлы в папке, где я сейчас;</p>
            <p>cd first-project — перейди в папку first-project;</p>
            <p>cd first-project/html — перейди в папку html, находящуюся в папке first-project;</p>
            <p>cd .. — перейди на уровень выше в родительскую папку;</p>
            <p>cd ~ — перейди в домашнюю директорию (у нас это /Users/stas_basov);</p>
            <p>mkdir second-project — в текущей папке создай папку с именем second-project;</p>
            <p>rm about.html — удали файл about.html;</p>
            <p>rmdir images — удали папку images;</p>
            <p>rm -r second-project — удали папку second-project и всё, что она содержит;</p>
            <p>touch index.html — создай файл index.html в текущей папке;</p>
            <p>touch index.html style.css script.js — если нужно создать несколько файлов, их имена можно вводить через пробел.</p>
            """)

    # Быстрая навигация
    elif git_command == 'navigation':
        return response.HttpResponse("""
            <h3>Быстрая навигация</h3>
            <p>↑ — показать предыдущую команду из буфера.</p>
            <p>↓ — показать следующую команду из буфера.</p>
            <p>Tab — автоматически дописать команду или путь.</p>
            <p>Ctrl + A — перейти в начало строки.</p>
            <p>Ctrl + E — перейти в конец строки.</p>
            """)

    else:
        return response.HttpResponseNotFound(f"Not found - {git_command}")
