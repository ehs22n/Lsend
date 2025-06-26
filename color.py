


class Color:
    WHITE = "\033[00m"
    NORMAL = "\033[0m"
    RED = "\033[91m"
    BLACK = "\033[5m"
    GREEN = "\033[92m"
    PURPLE = "\033[95m"
    CYAN = '\033[96m'
    YELLOW = '\033[33m'
    
class bold:
    WHITE = "\033[1;00m"
    NORMAL = "\033[1;0m"
    RED = "\033[1;91m"
    BLACK = "\033[1;5m"
    GREEN = "\033[1;92m"
    PURPLE = "\033[1;95m"
    CYAN = '\033[1;96m'
    YELLOW = '\033[1;33m'
     
class italic:
    WHITE = "\033[3;00m"
    NORMAL = "\033[3;0m"
    RED = "\033[3;91m"
    BLACK = "\033[3;5m"
    GREEN = "\033[3;92m"
    PURPLE = "\033[3;95m"
    CYAN = '\033[3;96m'
    YELLOW = '\033[3;33m'
    

class ColorCode ():
    def handle(code , color):
        match color:
            case "green":
                return f"\033[{code};92m"
        
            case "red":
                return  f"\033[{code};91m"
        
            case "purple":
                return f"\033[{code};95m"
        
            case "black":
                return f"\033[{code};5m"
        
            case "cyan":
                return f'\033[{code};96m'
        
            case "yellow":
                return f'\033[{code};33m'
        
            case "white":
                return f"\033[{code};00m"
        
        

    


    
    
class Choice:
    red = "red"
    green = "green"
    white = "white"
    black = "black"
    purple = "purple"
    cyan = "cyan"
    yellow = "yellow"
    





class Print:
    # XXX -> this simple Class can change your bash text color 
        
    color_list ={
        "red" : Color.RED,
        "green" : Color.GREEN,
        "white" : Color.WHITE, 
        "black" : Color.BLACK,
        "purple" : Color.PURPLE,
        "cyan" : Color.CYAN,
        "yellow"  : Color.YELLOW,
        "normal" : Color.NORMAL,
    }
    
    
    
    @staticmethod
    def color(message="" , color=Choice.white , bold=None , italic=None , light=None , underline=None , lamp=None , highlight=None , black=None , strikethrough=None):
        if bold:
            code = 1
            bold_text = ColorCode.handle(code , color)
            print(str(bold_text) + message + Print.color_list["normal"])
            
        elif italic:
            code = 3
            italic_text = ColorCode.handle(code , color)
            print(str(italic_text) + message + Print.color_list["normal"])
        
        elif light:
            code = 2
            light_text = ColorCode.handle(code , color)
            print(str(light_text) + message + Print.color_list["white"])
        
        elif underline:
            code = 4
            underline_text = ColorCode.handle(code , color)
            print(str(underline_text) + message + Print.color_list["white"])
        
        
        elif lamp:
            code = 5
            lamp_text = ColorCode.handle(code , color)
            print(str(lamp_text) + message + Print.color_list["white"])
        
        elif highlight:
            code = 7
            highlight_text = ColorCode.handle(code , color)
            print(str(highlight_text) + message + Print.color_list["white"])
            
        elif black:
            code = 8
            black_text = ColorCode.handle(code , color)
            print(str(black_text) + message + Print.color_list["white"])
            
        elif strikethrough:
            code = 9
            strikethrough_text = ColorCode.handle(code , color)
            print(str(strikethrough_text) + message + Print.color_list["white"])
        
            
        else:
            # print(Print.color_list["white"] + message + Print.color_list["white"])
            print(Print.color_list[f"{color}"] + message + Print.color_list["white"])
    
    