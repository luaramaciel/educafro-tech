function contagemRegressiva(maximo) {
    // Verifica se o número máximo é um número positivo
    if (maximo >= 0 && Number.isInteger(maximo)) {
        for (let i = maximo; i >= 0; i--) {
            console.log(i);
        }
    } else {
        console.log("Por favor, forneça um número inteiro positivo como parâmetro.");
    }
}

// Exemplo de uso da função
contagemRegressiva(5); // Deverá imprimir de 5 a 0
contagemRegressiva(10); // Deverá imprimir de 10 a 0
contagemRegressiva(-3); // Deverá imprimir "Por favor, forneça um número inteiro positivo como parâmetro."
contagemRegressiva(7.5); // Deverá imprimir "Por favor, forneça um número inteiro positivo como parâmetro."
