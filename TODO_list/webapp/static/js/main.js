function jqueryParseData (response, status) {
    console.log(response);
    console.log(status);
}

function taskInProjectParseData (response, status) {
    console.log(response.tasks);
    console.log(status);
}


function jqueryAjaxError(response, status) {
    console.log(response);
    console.log(status);
    console.log('error');
}

function projectsLoadIndex() {
    $.ajax({
        url: 'http://localhost:8000/api/v1/projects/',
        method: 'GET',
        dataType: 'json',
        contentType: 'application/json',
        success: jqueryParseData,
        error: jqueryAjaxError
    })
}

function tasksLoadIndex() {
    $.ajax({
        url: 'http://localhost:8000/api/v1/tasks/',
        method: 'GET',
        dataType: 'json',
        contentType: 'application/json',
        success: jqueryParseData,
        error: jqueryAjaxError
    })
}

function taskInProjectLoadIndex() {
    $.ajax({
        url: 'http://localhost:8000/api/v1/projects/2',
        method: 'GET',
        dataType: 'json',
        contentType: 'application/json',
        success: taskInProjectParseData,
        error: jqueryAjaxError
    })
}
function takeToken() {
    $.ajax({
        url: 'http://localhost:8000/api/v1/login/',
        method: 'post',
        data: JSON.stringify({username: 'admin', password: 'admin'}),
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){localStorage.setItem('apiToken', response.token);},
        error: function (response, status) {
            console.log(response);
        }
    });
}

function createTasksLoadIndex() {
    $.ajax({
        url: 'http://localhost:8000/api/v1/tasks/',
        method: 'POST',
        contentType: 'application/json',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        data: JSON.stringify({description: 'test', full_descr: 'full_test', project: 2, 'status': 1, 'type': 1}),
        dataType: 'json',
        success: jqueryParseData,
        error: jqueryAjaxError
    })
}

function deleteTasksLoadIndex() {
    $.ajax({
        url: 'http://localhost:8000/api/v1/tasks/39/',
        method: 'DELETE',
        contentType: 'application/json',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        dataType: 'json',
        success: jqueryParseData,
        error: jqueryAjaxError
    })
}

$(document).ready(function () {
    console.log('Задание 2.1 выбор проектов');
    projectsLoadIndex();
    console.log('Задание 2.2 выбор Задач');
    tasksLoadIndex();
    console.log('Задание 2.3 выбор задач проекта');
    taskInProjectLoadIndex();
    console.log('Задание 2.4 добавление задачи');
    takeToken();
    createTasksLoadIndex();
    console.log('Задание 2.4 удачение задачи');
    deleteTasksLoadIndex();
});