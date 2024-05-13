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
  fetch("http://localhost:105/lista_remedio",{
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
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