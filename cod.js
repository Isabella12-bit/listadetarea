document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("button").addEventListener("click", agregarTarea);
});

function agregarTarea() {
    const input = document.getElementById("nuevaTarea");
    const tarea = input.value.trim();
    if (tarea === "") return;
    
    const lista = document.getElementById("listaTareas");
    const item = document.createElement("li");
    item.innerHTML = `${tarea} <button onclick="eliminarTarea(this)">Eliminar</button>`;
    lista.appendChild(item);
    
    input.value = "";
}

function eliminarTarea(boton) {
    const item = boton.parentElement;
    item.remove();
}