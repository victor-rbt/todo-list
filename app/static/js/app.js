function addTask(){
    a = 'add_task';
    window.open(a, 'add_task', 'width=600, height=800');
}

function updateTask(value){
    var parametro = parseInt(value)
    $.ajax({
        url: '/update_task',
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify({'parametro': parametro})
    }).done(function(){
        alert("Tarefaasdasdasdas Atualizada!");
    })
}