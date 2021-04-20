<br />
<p align="center">
  <a href="https://github.com/Czembri/contentAgregator">
    <img src="https://cdn.iconscout.com/icon/free/png-256/django-2-282855.png" width="80" height="80">
  </a>

  <h3 align="center">IamCodeAddicted</h3>

  <p align="center">
    Great move to become a true journalist!
    <br />
    <a href="https://github.com/Czembri/IamCodeAddicted"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="#">Report Bug</a>
    ·
    <a href="#">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
     <li><a href="#endpoints">Endopints</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Main site](https://user-images.githubusercontent.com/57504533/115377618-16a34380-a1d0-11eb-9d97-ba307fdd5fb5.png "Main")

Project has been created for the recruitment purposes. It allows You to add Your own movies to the site, buy tickets, use REST API and more...

### Built With

* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)


<!-- GETTING STARTED -->
## Getting Started

Clone this repo to your local machine simply using https://github.com/Czembri/IamCodeAddicted.git
You need to have installed python 3.8 > and postgres database (better for you to keep the database in docker container). 

### Installation

1. Open terminal in the source directory
2. Create and activate a virtual environment
   * Windows:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
   * Linux/MacOS
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
   
3. Install requirements.txt
  * windows
   ```sh
   python -m pip install -r requirements.txt
   ```
  * Linux/MacOS
   ```sh
   python3 -m pip install -r requirements.txt
   ```
4. Create app_config.ini file and fill it with suitable data.
   ```ini
   [DATABASE]
    engine = 
    name = 
    user = 
    password = 
    host = 
    port = 
   ```
5. Upgrade Your database using:
  ```sh
    python manage.py migrate
  ```
6. Seed Your database using:
  ```sh
  python manage.py loaddata movies.json
  ```


<!-- USAGE EXAMPLES -->
## Usage

### see the details of every movie

![Discover](https://user-images.githubusercontent.com/57504533/115379486-db097900-a1d1-11eb-8162-63932311209f.png "discover")


### buy a ticket

![Buy](https://user-images.githubusercontent.com/57504533/115379598-f70d1a80-a1d1-11eb-8985-513ffba3098a.png "buy")


### Enjoy Your dashboard of bought tickets (if you don't want to go to see the movie just delete it!)

![Dashboard](about:blank "dashboard")


### Get Your JWT token and enjoy the usage of the API
![GetJWT](https://user-images.githubusercontent.com/57504533/115380015-6a169100-a1d2-11eb-9b0e-66e95a86267b.png "jwt")
![GetJWT2](https://user-images.githubusercontent.com/57504533/115380141-8fa39a80-a1d2-11eb-8446-784fa0cc75b8.png "jwt2")
![GetJWT3](https://user-images.githubusercontent.com/57504533/115380173-99c59900-a1d2-11eb-8264-a5ee7f27b050.png "jwt3")


## Endpoints
[ API ]

### register user

method: POST
/api/register/


### get JWT Token

method: POST
/api/login/ or /api/token/
refresh token: /api/refresh/


### get list of movie, create movie

method: GET
/api/

method: POST
/api/


### get list of bought tickets, buy a ticket, delete a ticket

method: GET
/api/purchase/

method: POST
/api/purchase/<int:movie_id>

method: DELETE
/api/purchase/<int:movie_id>


[ APP ]

'/' - main page

'/login/' - login page 

'/register/' -register page

'/logout/' - session cleared, logout page

'/bought/' - bought tickets

'/movie/<int:pk>/' - movie details

'/buy/' - buy ticket

<!-- ROADMAP -->
## Roadmap

-- to do



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MY License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Twitter - [@CzembrowskaOla](https://twitter.com/CzembrowskaOla)

Project Link: [https://github.com/Czembri/contentAgregator](https://github.com/Czembri/IamCodeAddicted)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
