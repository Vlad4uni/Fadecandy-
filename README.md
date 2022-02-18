
PDE 2400 -Projects 2 
Vladislav Trayanov M00763313


###########################################################################################################################################################

For the user to be able to run my program they must have the following libraries :
-Python Client library for Open Pixel Control (opc)
-tkinter + Tcl package

To be able to see the LED strips produce an animation the user must have the appropriate simulator version based on their operating system.

Once the libraries and simulator are downloaded and are operational the user is now clear to run the program .
If the animations do not begin straight away once the Final GUI is ran then  the user should test run the animations file and run the Final GUI file again.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the user runs the "Final GUI" file a Tkinter window will open while an animation with a globe will appear in the screen of the simulator.
In the Tkinter window there will be a blue label located in the middle of the screen saying "Hello" ,
Right below the hello label there is a buton that can be pressed once the user is ready to start the quiz .

To start the quiz the user must press the Start button that is right bellow the blue label box .

When the "Start" button is pressed the globe animation will change into a flashing question mark in the simulator window, 
while in the Tkinter window the blue label notice and the "Start" button wiill dissapear and a new label asking for the users favourite country
will appear .An input box appears in the possition where the start button was .Below the input box there is also an extra label which informs 
the user that his/her input must be all in capital letters , that numbers and symbols are not allowed .

If the user has entered a name of a country in the appropriate format then he/she will be able to continue throught the quiz , however if the 
input does not match the format then he/she will not be able to submit the answer until they fix their answer to the question .When the answer is
submitted it is instanteniously checked against the list of three countries that is embeded into the program .If the country matches one 
of the three countries that were listed then a message appears in the Tkinter windows saying " How amazing is that, we have matching tastes when 
it comes to countries, these are my favorite countries: " however if it doesnt match the label that asked the user for their favourite country 
will change to " It appears that we do not have the same taste when it comes to countries, these are my favourite countries " .

Once the appropriate response is shown in the Tkinter window the three countries that I have included in the list of ANIMATIONS from an external fiel ,
called animations .The seperate animations would start to appear on the simulator window with their appropriate animations in the order that they were 
programmed in .

Once the three flags have completed their animations , the new message  "Thank you for participating in this quiz."  appears in the blue label 
where the response based on the comparisson of the countries was previously shown .Simultaniously as this response occurs in the Tkinter window 
the final animation starts in the simulator window .At the point when the end animation finishes the Tkinter window is partially reset as the blue 
label has reset to its initial state of "Hello" but a new button now appears bellow the "Hello" label .Wheb the user presses the new button "Try again" 
both the GUI and animations are reset to their initial possitions .
