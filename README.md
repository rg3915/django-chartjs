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

O <a href="https://www.chartjs.org/" target="_blank">Chart.js</a> é uma biblioteca Javascript para gerar gráficos.

Clicando em <a href="https://www.chartjs.org/docs/latest/" target="_blank">Get Started</a> temos o seguinte exemplo:

```javascript
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

### Criando os templates

Para ver este exemplo funcionando precisamos criar um template:

```
cd myproject/core
mkdir -p templates/includes
```

Vamos um <a href="https://gist.github.com/rg3915/0144a2408ec54c4e8008999631c64a30" target="_blank">template base</a>.

```
cd templates
wget https://gist.githubusercontent.com/rg3915/0144a2408ec54c4e8008999631c64a30/raw/be05f2f8a483c6ddab3705c13bff0ac5fc2223be/base.html
wget https://gist.githubusercontent.com/rg3915/0144a2408ec54c4e8008999631c64a30/raw/ecbd782e23b3886ce64b318ef5ea194ed89b8ab3/index.html#

# Vá para a subpasta includes
wget https://gist.githubusercontent.com/rg3915/0144a2408ec54c4e8008999631c64a30/raw/ee78c798ed1fd57e2ba7328342ac3f4ab20268be/nav.html
```

### Criando views e url.

Vamos criar a url

```
# core/urls.py
from django.urls import path
from myproject.core import views as v


app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
]
```

E a views.py

```
from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    return render(request, template_name)
```

### Rodando a aplicação

Antes de rodar, faça

```
# Vá para a pasta onde está o manage.py
cd ../..
python contrib/env_gen.py
python manage.py migrate
```

E por fim, rode a aplicação.

```
python manage.py runserver
```

### Inserindo o gráfico

Vamos copiar o exemplo de <a href="https://www.chartjs.org/docs/latest/" target="_blank">Get Started</a> para dentro de index.html.

Veja o resultado em index.html.

E em `base.html` acrescente, no final do arquivo

```
    ...
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script>
```

# Parte 2

## Trabalhando com dados reais

Vamos trabalhar com dados reais vindos do banco de dados.

Para isso vamos criar alguns modelos: *product* e *category*.

### models.py

Vamos editar o arquivo `models.py`.

```
cat << EOF > models.py
from django.db import models


class Category(models.Model):
    title = models.CharField('categoria', max_length=50, unique=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField('título', max_length=100, unique=True)
    price = models.DecimalField('preço', max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category,
        verbose_name='categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.title
EOF
```

### Migrações

Vamos criar as migrações do banco.

```
python manage.py makemigrations
python manage.py migrate
```

### Inserindo alguns dados

Para isso abra o `shell_plus`.

```
python manage.py shell_plus
```

E rode o script a seguir:

```
# Criando as categorias
categories = ('Bebida', 'Sobremesa', 'Lanche', 'Fruta', 'Refeição')
[Category.objects.create(title=category) for category in categories]

# Criando os produtos
import csv
import io
import urllib.request
from pprint import pprint


def csv_online_to_list(url: str) -> list:
    '''
    Lê um CSV a partir de uma url.
    '''
    url_open = urllib.request.urlopen(url)
    reader = csv.DictReader(io.StringIO(
        url_open.read().decode('utf-8')), delimiter=',')
    csv_data = [line for line in reader]
    return csv_data


products = csv_online_to_list('https://raw.githubusercontent.com/rg3915/django-chartjs/master/fix/products.csv')

pprint(products)

aux = []

for product in products:
    data = {
        'title': product['title'],
        'price': product['price']
    }
    category_title = product.get('category')
    category = Category.objects.filter(title=category_title).first()
    obj = Product(**data)
    if category:
        obj = Product(category=category, **data)
    aux.append(obj)

Product.objects.bulk_create(aux)
```


### Visualizando os dados no Admin

Talvez você ainda não tenha criado um super usuário...

```
python manage.py createsuperuser --username="admin"
```

Edite `admin.py`

```
cat << EOF > myproject/core/admin.py
from django.contrib import admin
from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category',)
    search_fields = ('title',)
    list_filter = ('category',)


admin.site.register(Category)
EOF
```

