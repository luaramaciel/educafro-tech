function verificarIdade(idade) {
    if (idade > 18) {
        console.log("Pode beber");
    } else {
        console.log("Não pode beber");
    }
}

// Exemplo de uso da função
verificarIdade(20); // Resultado esperado: "Pode beber"
verificarIdade(16); // Resultado esperado: "Não pode beber"
