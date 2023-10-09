from Body.Speak import Speak
from Body.Listen import Listen

def MainExe():

    while True:
        
        query = Listen()
        
        if "hello" in query:
            Speak("Hi! I am Jarvis!")
           
        elif "bye" in query:
            Speak("Bye Bye.")
            
        else:
            Speak("")
                   
MainExe()

















     
        
            
            
            
               
        
        