
/**
 * Wait until the page is loades
 */
 document.addEventListener('DOMContentLoaded', function() {
    
    /**
     * Get every element that is going to be modified
     */
    const postBody = document.getElementById('receitasItems');
    const contaJS = document.getElementById('contaJS');

    console.log(contaJS.innerHTML);

    /**
     *  Send a request to get the data
     */
    $.ajax({
        type: 'GET',
        url: `/profiles/receitas-json/${contaJS.innerHTML}`,
        success: function(response){

            //console.log(response)
          
            const feed = response.receitas

            feed.forEach(element => {
                let color = ""
                console.log(element.valor)
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
                  <td>${element.dataPagamentoEsperado}</td>
                </tr>
              `
            })
        },
        error: function(response){
            console.log(error)
        }
    })
    
    
})

