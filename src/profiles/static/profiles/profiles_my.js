
/**
 * Wait until the page is loades
 */
document.addEventListener('DOMContentLoaded', function() {
    
    /**
     * Get every element that is going to be modified
     */
    const postBody = document.getElementById('contasItems');

    /**
     *  Send a request to get the data
     */
    $.ajax({
        type: 'GET',
        url: '/profiles/contas-json',
        success: function(response){

            console.log(response)
          
            const feed = response.contas

            feed.forEach(element => {
                postBody.innerHTML += `
                <tr>
                  <td><a href="/profiles/conta/${element.nome}">${element.nome}</a></td>
                  <td>${element.instituicao}</td>
                  <td>${element.tipo}</td>
                  <td>R$${element.saldo}</td>
                </tr>
              `
            })
        },
        error: function(response){
            console.log(error)
        }
    })
    
    
})

