---
toc: true
comments: true
layout: default
title: Data Structures Writeup
description: 
type: hacks
courses: { compsci: {week: 17} }
---

<div class="typewriter">
<h1 class="typewriterText">Data Structure Project Writeup</h1>
</div>
<head>
</head>

<body>
<h1>Collections</h1>
<p>A model in the context of a SQLite Database is a table: a collection of data related to each other. An example of a model and the one I integrated was the user table which takes in a userID, an id (for sql identification purposes) a profile picture as text as the image is sent in base64, and other attributes.</p>
<img src="/studentmodern/images/datawriteup/1.png">
<p>The code that initializes the table is as follows and on <a href="https://github.com/spooketti/BabyTronRealEstateServer/commit/6a8306943f4e699b5dd5294d956af2a443b82445">GitHub</a>
</p>
<img src="/studentmodern/images/datawriteup/2.png">

<h1>Lists and Dictionaries</h1>
<p>
Dictionaries and Lists are used in the user file as there is a dictionary with each key's values being a list after the values are queried from the database.
<img src="/studentmodern/images/datawriteup/3.png">
</p>


<h1>API and JSON</h1>
<p>The API is used to communicate between the frontend and the server. GET requests are used to retrieve data from the server and POST requests is more dynamic as it can be used for various purposes. In the context of the project it is used to set a value in the database, and retrieve data.</p>
<p>JSON or Javascript Object Notation is used to transmit a "name" for the value which is the key, and the value itself, so if I wanted to recieve a username, the key is "username" and the value would be the actual username value</p>
<h3>Example of POST request</h3>
<p>In the signup route, POST is used as it recieves values from the signup page, like the username password and etc, and then the server then sends a JWT (JSON Web Token) that acts as an authenticator for the user</p>
<img src="/studentmodern/images/datawriteup/4.png">
<h3>Example of GET</h3>
<p>Here the GET first runs token_required which just checks if the JWT sent from the client is valid, and if it is valid it will then get the values of the user.
</p>
<img src="/studentmodern/images/datawriteup/5.png">
<p>That actual validation in token_required is as follows</p>
<img src="/studentmodern/images/datawriteup/6.png">
<p>200 Status</p>
<img src="/studentmodern/images/datawriteup/7.png">
<p>400 Status</p>
<img src="/studentmodern/images/datawriteup/8.png">

<h1>Frontend Work</h1>
<p>The actual client is on the frontend and here is the GET/POST work on the frontend with this being the 200 status</p>
<img src="/studentmodern/images/datawriteup/9.png">
<p>The 401 unauthorized in the case the client does not have the correct credentials</p>
<img src="/studentmodern/images/datawriteup/10.png">
<p>These are the values receieved in the 200 request</p>
<img src="/studentmodern/images/datawriteup/11.png">
<p>Finally here is the javascript that handles the GET and POST requests</p>
<img src="/studentmodern/images/datawriteup/12.png">
<img src="/studentmodern/images/datawriteup/13.png">
</body>

  
 
