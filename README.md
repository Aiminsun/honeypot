# Telnet honeypot
This is a simple honey pod to monitor and log incoming cli telnet connection
attempts. <br />
The honey pod opens a port and waits for incoming connections. For every connection, the program sends welcome message, and asks for user name and password. Whatever the connected side sends, the program saves in file.

<pre>

usage: honeypot.py [-h] [-p PORT] [-f FILENAME] [-u USERNAME] [-w PASSWORD]
                   [-o OUTPUT] [-I IP] [-a ATTEMPTS] [-d DENIED]

Simple honey pod for telnet CLI network connections attempts

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Port number to listen for connections. Default: 23
  -f FILENAME, --filename FILENAME
                        Text file name with welcome message to be sent to the
                        attacker. Default: No filename fill be loaded and no
                        message will be displayed
  -u USERNAME, --username USERNAME
                        Promt that will be sent to attacker to ask for
                        username. Default: "Username:"
  -w PASSWORD, --password PASSWORD
                        Promt that will be sent to attacker to ask for
                        password. Default: "Password:"
  -o OUTPUT, --output OUTPUT
                        Output file to log login attempts. Default: output.log
  -I IP, --ip IP        Bind to specific IP. Default: localhost
  -a ATTEMPTS, --attempts ATTEMPTS
                        Connections attempts counter. Default: 5
  -d DENIED, --denied DENIED
                        Fail message to send to attacker. Default: "Access
                        denied"

</pre>

## Usage
Forward connection from router to the port using this program.

## Example
I started the program on port 999 using :
<pre>
sudo ./honeypot.py -p 999 -f welcome.txt
</pre>
And I forwarded ports 22 and 23 from my router to port 999 of the computer
(Raspberry pi) After some time the output file output.log contained the
following:
<pre>
2018-04-03 13:03:33.436315 Logged in: ('82.80.148.44', 56405)
2018-04-03 13:03:33.966303, Username recieved: root
2018-04-03 13:03:34.488361, Password recieved: hunt5759
2018-04-03 13:03:35.007603, Username recieved: root
2018-04-03 13:03:35.529605, Password recieved: default
2018-04-03 13:03:36.054998, Username recieved: guest
2018-04-03 13:03:36.583650, Password recieved: 12345
2018-04-03 13:03:37.111977, Username recieved: root
2018-04-03 13:03:37.633298, Password recieved: ttnet
2018-04-03 13:03:37.633749 Logged in: ('122.226.181.167', 51034)
2018-04-03 13:03:38.134534 Connection closed
2018-04-03 13:03:38.134756 Logged in: ('82.80.148.44', 56429)
2018-04-03 13:03:38.655134, Username recieved: supervisor
2018-04-03 13:03:39.179816, Password recieved: supervisor
2018-04-03 13:03:39.699053, Username recieved: root
2018-04-03 13:03:40.237234, Password recieved: aquario
2018-04-03 13:03:40.755778, Username recieved: admin
2018-04-03 13:03:41.275820, Password recieved: pass
2018-04-03 13:03:41.795914, Username recieved: root
2018-04-03 13:03:42.315545, Password recieved: klv1234
2018-04-03 13:03:42.356125 Logged in: ('82.80.148.44', 56459)
2018-04-03 13:03:42.881175, Username recieved: root
2018-04-03 13:03:43.420037, Password recieved: hi3518
2018-04-03 13:03:43.942748, Username recieved: root
2018-04-03 13:03:44.465876, Password recieved: user
2018-04-03 13:03:44.986794, Username recieved: root
2018-04-03 13:03:45.508611, Password recieved: 1234567890
2018-04-03 13:03:46.028584, Username recieved: admin
2018-04-03 13:03:46.551995, Password recieved: 1111111
</pre>
These are only few lines from the output file out of many, that shows some IPs that are trying to connect and to use common passwords to log in.
