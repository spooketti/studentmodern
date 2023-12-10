---
toc: true
comments: true
layout: default
title: The Internet HW
description: Answers to the lesson on the internet
type: hacks
courses: { compsci: {week: 8} }
---

<img src="https://cdn.discordapp.com/attachments/674826245443289088/1181027847582789734/image.png?ex=657f90e5&is=656d1be5&hm=8407938418d900bd1b7c1194deef979187fd2d1600e77e9ff4a3ab3af73439eb&">

<img src="https://cdn.discordapp.com/attachments/674826245443289088/1181028026201427978/image.png?ex=657f910f&is=656d1c0f&hm=55b9e7f34daaa4faac5c6790efaf03cddbbd32a246963baf90baa8e7a5078239&">

# Homework Questions
<div class="typewriter">
<h1 class="typewriterText">Reflection on the internet lesson</h1>
</div>
<head>
</head>

<body>
<div class="typewriter">
<h1 class="typewriterText">IP Addresses</h1>
</div>
<ul>
<li>1.1.1.1.<span style="color:red">1</span>: Invalid because there aer five numbers</li>
<li>23.23.23.23: Valid becaues they are within 0-255 and there are 4 numbers</li>
<li>134.<span style="color:red">492</span>.100.0: Invalid because one number is over 255</li>
<li>255.<span style="color:red">256</span>.55.255: Invalid because one number is over 255</li>
<li>2.93.255.19: Valid because there are 4 numbers within 0-255</li>
</ul>
If Dian Du is at home on his home network and sends a message to every computer on the network, this is an example of a broadcast for it is LAN-wide and goes to every computer on the network.
<div class="typewriter">
<br>
<h1 class="typewriterText">Models</h1>
<ul>
<li>ASCII: is not neccessarily a protocol; however, it is on the application layer as it is used for character encoding (represents text)</li>
<li>FTP: is on the application layer because it enables the transfer of files between client and server over network</li>
<li>TLS:Is on the application layer in presentation because it translates data sent between computers into what humans can read</li>
<li>USB: A physical object: so physical layer and this is the outlier of the 4</li>
</ul>
Telnet is on the application layer and the purpose of the application layer is provide network services to the user and is the interface between software and network.
</div>

<h1 class="typewriterText">DNS</h1>
<pre>
Bob would need to buy bob.is.the.best.com and the subdomains are
best.com
the.best.com
is.the.best.com
bob.is.the.best.com
</pre>
<span style="font-size:xx-small">SRIJAN!!!!!</span>

<h1 class=typewriterText>HTTP and HTTPS</h1>
1)
HTTP vs HTTPS: HTTP sends plaintext as HTTPS sends encrypted text
HTTPS uses the SSl/TLS protocol that encrypts the data being transmitted between browser and server
<br>
2)
We used HTTP and the benefits of this are simplicity and speed; however, the problems are that it is insecure and has privacy concerns.


<h1 class=typewriterText>TCP and UDP</h1>
1)
He should use UDP because it is low cost and quick
Some issues of this protocol is that it has little data checking, unreliable and some packets may be out of order or generally missing, one potential issue would be in video streaming as if a packet is lost, the video will either freeze or the video quality will drop.
<br>
2)
It is important that all the packets arrive because it results in accurate and reliable data, and it uses Checksum verification (a mathematical sum generated from the data) which is used to verify each packet arrived.
<br>
3)
In TCP, Server B can ensure they recieved the packets by using ACK packets, which is to say Server B will send a packet back to A as a form of confirmation.

UDP does not do this in general for packets are usually lost in UDP.

Another use of this could be flow control as TCP doesnt overwhelm the reciever with data faster than it can process.


</body>

  
 
