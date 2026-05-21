const taskInput = document.getElementById('taskInput');
const addbtn = document.getElementById('addBtn');
const taskList = document.getElementById('taskList');

addbtn.addEventListener('click', () => {
    const text = taskInput.ariaValueMax.trim();
    if (text === '') {
        alert('Ingrese un valor');
        return;
    }

    const li = document.createElement('li');

    const span = document.createElement('span');
    span.textContent = text;

    span.addEventListener('click', () => {
        span.classList.toggle('done');
    });

    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Eliminar';

    deleteBtn.addEventListener('click', () => {
        li.remove();
    });
    li.appendChild(span);
    li.appendChild(deleteBtn);
    taskList.appendChild(li);
    taskInput.value = '';
});