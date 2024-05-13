async function buscaRemedio(){
    var inputRemedio = document.getElementById("inputRemedio").value.toUpperCase();
    opcoes = {
      method: "POST",
      mode: "cors", // no-cors, *cors, same-origin
      credentials: "same-origin", // include, *same-origin, omit
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({"nome_remedio": inputRemedio}), // body data type must match "Content-Type" header
    }
    let resposta = await fetch("http://127.0.0.1:9000/buscaRemedioBase", opcoes);
    let objetoResposta = await resposta.json();
    console.log(objetoResposta)
}


function buscarRemedio() {
    var inputRemedio = document.getElementById("inputRemedio").value.toUpperCase();
    var tabela = document.getElementById("tabela-corpo");
    var linhas = tabela.getElementsByTagName("tr");
// Iterar sobre todas as linhas da tabela
    for (var i = 0; i < linhas.length; i++) {
      var colunaNome = linhas[i].getElementsByTagName("td")[0];
      if (colunaNome) {
        var textoNome = colunaNome.textContent || colunaNome.innerText;
        if (textoNome.toUpperCase().indexOf(inputRemedio) > -1) {
          linhas[i].style.display = "";
        } else {
          linhas[i].style.display = "none";
        }
      }
    }
  }