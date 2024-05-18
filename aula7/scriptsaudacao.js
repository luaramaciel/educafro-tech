document.getElementById("botao").addEventListener("click", function() {
    var nome = document.getElementById("nome").value;
    if (nome.trim() !== "") { // Verifica se o campo não está vazio
        alert("Olá, " + nome);
    } else {
        alert("Por favor, digite seu nome.");
    }
});
