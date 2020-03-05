# funkyBlue
The millenial version of pong


A pong like game made on the arcade Python game framework.

The concept of the game is to move a platform and prevent projectiles passing your way. Unlike pong in funky blue you operate an extra blue
platform which texture is cropped from  [this hand painted wallpaper](https://image.shutterstock.com/image-illustration/blur-hand-paint-wallpapers-dark-260nw-1586825791.jpg)
which is in the middle separating the screen into two parts. The projectiles in the upper part are blue and the projectiles in the bottom part, below the platform are red.

You lose life when the projectile passes from its' current half to the other. In the beginning you have three lives. Once a projectile passes to the other half it changes colour.
From blue to red or from red to blue.

When you hit a projectile, your score goes up by one. Once you reach certain number (now 10) the funky blue platform shrinks, and it keeps shrinking every time you reach a new level.
Currently the levels are only 10 yet that will change.

Screenshot:

![screenshot funky blue][ss_1]



[ss_1]: https://raw.githubusercontent.com/Alex92rus/funkyBlue/master/assets/funky_blue_ss1.png  "Funky Blue in the middle, guarding blue and red projectile"
