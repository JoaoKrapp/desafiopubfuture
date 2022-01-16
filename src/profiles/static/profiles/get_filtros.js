
/**
 * Wait until the page is loades
 */
 document.addEventListener('DOMContentLoaded', function() {
    
    /**
     * Get every element that is going to be modified
     */
    const postBody = document.getElementById('receitasItems');
    const contaJS = document.getElementById('contaJS');
    const dataInicioJS = document.getElementById('dataInicioJS');
    const dataFinalJS = document.getElementById('dataFinalJS');
    const checkboxJS = document.getElementById('checkboxJS');
    const descricaoJS = document.getElementById('descricaoJS');

    console.log(dataInicioJS)
    console.log(dataFinalJS)
    console.log(checkboxJS)
    console.log(descricaoJS)

    /**
     *  Send a request to get the data
     */
    $.ajax({
        type: 'GET',
        url: `/profiles/receitas-json/${contaJS.innerHTML}/filtrar/?dataInicio=${dataInicioJS.innerHTML}&dataFinal=${dataFinalJS.innerHTML}&checkbox=${checkboxJS.innerHTML}&descricao=${descricaoJS.innerHTML}`,
        success: function(response){

            const feed = response.data

            feed.forEach(element => {
                let color = ""
                if (element.valor > 0) {
                    color = "table-success"
                }
                if(element.valor < 0){
                    color = "table-danger"
                }
                postBody.innerHTML += `
                <tr class="${color}">
                  <td>${element.descricao}</td>
                  <td>R$${element.valor}</td>
                  <td>${element.criado}</td>
                  <td>${element.dataPagamento}</td>
                </tr>
              `
            })
        },
        error: function(response){
            console.log(error)
        }
    })
    
    
})

