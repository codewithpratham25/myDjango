document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#red').onclick = function(){
        document.querySelector('#hello').style.color = 'red'
    }
    document.querySelector('#blue').onclick = function(){
        document.querySelector('#hello').style.color = 'blue'
    }
    document.querySelector('#yellow').onclick = function(){
        document.querySelector('#hello').style.color = 'yellow'
    }
})