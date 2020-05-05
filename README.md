# django-chartjs

Django and ChartJS experiments.

## This project was done with:

* Python 3.8.2
* Django 2.2.12
* Bootstrap 4.0
* ChartJS 2.9.3


## How to run project?

* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Run the migrations.

```
git clone https://github.com/rg3915/django-chartjs.git
cd django-chartjs
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Este projeto foi feito com:

* Python 3.8.2
* Django 2.2.12
* Bootstrap 4.0
* ChartJS 2.9.3

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-chartjs.git
cd django-chartjs
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Criando o projeto do zero

Baixe este boilerplate.

```
wget https://gist.githubusercontent.com/rg3915/b363f5c4a998f42901705b23ccf4b8e8/raw/39caa9f63aa693ed651cebd4bb503cebffc51f6d/boilerplatesimple.sh
```

Ele serve pra criar um projeto simples em Django com o settings pré-configurado.

```
source boilerplatesimple.sh
```

Após terminar o processo de instalação você pode deletar isso.

```
rm boilerplatesimple.sh
```

## Chart.js

O [Chart.js](https://www.chartjs.org/) é uma biblioteca Javascript para gerar gráficos.

Clicando em [Get Started](https://www.chartjs.org/docs/latest/) temos o seguinte exemplo:

```
<canvas id="myChart" width="400" height="400"></canvas>
<script>
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
</script>
```