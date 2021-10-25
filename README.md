<div id="top"></div>

<br />
<div align="center">
    <img src="docs/Logo512.png" alt="Logo" width="80" height="80">


  <h3 align="center">PostIn</h3>

  <p align="center">
    Uma rede social mais humana!
    <br />
</div>

<details>
  <summary>Indice</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o projeto</a>
    </li>
    <li>
      <a href="#instalando">Instalando</a>
    </li>
  </ol>
</details>

## Sobre o projeto

Este é nosso projeto final da matéria de Engeharia de Software, do curso Técnico em Informatica Integrado ao Ensino Médio, do Instituto Federal de Educação Ciência e Técnologia do Rio Grande do Sul - Campus Farroupilha.
Nosso intuito com esse projeto é criar uma rede social sem nenhum sistema de inteligencia artificial que molde seu feed.

## Instalando

Este é um exemplo de como rodar o projeto localmente.


### Antes de começar

Garanta que o docker e o docker compose estão instalados corretamente. Para isso é possível seguir o guia oficial de ambas ferramentas, disponíveis no site do docker.

Além disso é necessário ter o python 3.X instalado, então para isso é só seguir a orientação oficial no site deles.

Documentação:

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Python](https://www.python.org)

### Subindo o projeto

Para subir o projeto é extremamente simples. Só executar:

```bash
docker-compose up
```

Isso vai subir o banco de dados e outras possíveis dependências do backend. Se quiser subir o projeto local junto só descomentar a primeira parte do docker-compose.yml, porém para desensvolviemnto é melhor deixar comentado e usar o comando

```bash
python3 manage.py runserver
```

Dessa maneira terá disponível o hot-reload, que ao salvar um arquivo o servidor reinicia para mostrar as mudanças, dessa maneira desenvolvendo com maior agilidade.

Caso esse comando dê algum erro, possívelmente é um problema com dependências do python, então para instalar todas necessárias do projeto é só usar o comando

```bash
pip install -r requirements.txt
```
