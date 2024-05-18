// Array com 10 nomes diferentes
var nomes = ["Ana", "João", "Maria", "Pedro", "Carla", "Miguel", "Sofia", "Lucas", "Lara", "Gustavo"];

// Função para obter o nome na posição fornecida
function nomeNaPosicao(posicao) {
    // Verifica se a posição fornecida está dentro dos limites do array
    if (posicao >= 0 && posicao < nomes.length) {
        console.log("Nome na posição", posicao, ":", nomes[posicao]);
    } else {
        console.log("Posição inválida.");
    }
}

// Exemplo de uso da função
nomeNaPosicao(3); // Deverá imprimir o nome na posição 3 do array
nomeNaPosicao(8); // Deverá imprimir o nome na posição 8 do array
nomeNaPosicao(12); // Deverá imprimir "Posição inválida."
