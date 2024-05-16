// Evento para buscar remedio apertando enter
let elemento_busca = document.getElementById("inputRemedio")
elemento_busca.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    event.preventDefault()
    buscaRemedio()
  }
}); 

// Recriei esse função usando await pois um erro estava acontecendo nas =>
async function buscaRemedio(){
    let inputRemedio = document.getElementById("inputRemedio").value;
    opcoes = {
      method: "POST",
      mode: "cors", // no-cors, *cors, same-origin
      credentials: "same-origin", // include, *same-origin, omit
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({"nome_remedio": inputRemedio}), // body data type must match "Content-Type" header
    }
    let resposta = await fetch("http://127.0.0.1:1000/busca_remedio_base", opcoes);
    let objetoResposta = await resposta.json();
    const tabelaCorpo = document.getElementById("tabela-corpo");
      tabelaCorpo.innerHTML = "";
      objetoResposta.forEach((remedio)=>{

        const tr = document.createElement("tr");
        const tdNome = document.createElement("td");
        tdNome.textContent = remedio[1];
        const tdQuantidade = document.createElement("td");
        tdQuantidade.textContent = remedio[2];
        const tdDosagem = document.createElement("td");
        tdDosagem.textContent = remedio[3];
        const tdValidade = document.createElement("td");
        tdValidade.textContent = remedio[4];
        const tdDescricao = document.createElement("td");
        tdDescricao.textContent = remedio[5];
        const tdDoador = document.createElement("td");
        tdDoador.textContent = remedio[6];
        tr.appendChild(tdNome);
        tr.appendChild(tdQuantidade);
        tr.appendChild(tdDosagem);
        tr.appendChild(tdValidade);
        tr.appendChild(tdDescricao);
        tr.appendChild(tdDoador);
        tabelaCorpo.appendChild(tr);
      })
}


function buscarRemedio() {
  let inputRemedio = document.getElementById("inputRemedio").value.toUpperCase();
  fetch("http://127.0.0.1:1000/busca_remedio_base",{
    method: "POST",
    mode: "no-cors", // no-cors, *cors, same-origin
    credentials: "same-origin", // include, *same-origin, omit
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({"nome_remedio": inputRemedio}), // body data type must match "Content-Type" header
  })
    .then((response) => response.json())
    .then((data) => {
      const tabelaCorpo = document.getElementById("tabela-corpo");
      tabelaCorpo.innerHTML = "";
      data.forEach((remedio)=>{

        const tr = document.createElement("tr");
        const tdNome = document.createElement("td");
        tdNome.textContent = remedio[0];
        const tdQuantidade = document.createElement("td");
        tdQuantidade.textContent = remedio[1];
        const tdDosagem = document.createElement("td");
        tdDosagem.textContent = remedio[2];
        const tdValidade = document.createElement("td");
        tdValidade.textContent = remedio[3];
        tr.appendChild(tdNome);
        tr.appendChild(tdQuantidade);
        tr.appendChild(tdDosagem);
        tr.appendChild(tdValidade);
        tabelaCorpo.appendChild(tr);
      })

  })
}