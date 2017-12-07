screenWidth = 600
screenHeight = 800
planetSize = screenWidth//30
parasiteSize = screenWidth//8
CHARCOAL = (28,28,28)
WHITE = (255,255,255)
BLACK = (0,0,0)
DARKGREY = (77,77,77)
# RED = (255,0,0)
RED = (255,104,104)
PINK = (249,167,167)
ORANGE = (247,126,74)
YELLOW = (255,250,148)


### wrap line functions

from itertools import chain

def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext             
        
def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped


def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account.
    """
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)
    
### callback clear screen surface
def clear_callback(surf, rect):
    color = CHARCOAL
    surf.fill(color, rect)