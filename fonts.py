import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Font Display")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Text to display
text = "A quick brown fox jumps over the lazy dog"

# List of fonts
fonts = [
    'microsoftyibaiti', 'modernno20', 'freesiaupc', 'gillsansultra', 
    'arialblack', 'microsofttaile', 'verdana', 'playbill', 'miriamfixed', 
    'pristina', 'perpetuatitling', 'helveticaneueltproroman', 'goudystout', 
    'ebrima', 'bodoni', 'microsoftjhenghei', 'franklingothicheavy', 'franklingothicmediumcond', 
    'microsoftnewtailue', 'garamond', 'utsaah', 'baskervilleoldface', 'bookmanoldstyle', 'couriernew', 
    'vani', 'dinprobold', 'moolboran', 'kokilaitali', 'oldenglishtext', 'stencil', 'edwardianscriptitc', 
    'script', 'msreferencespecialty', 'franklingothicdemi', 'kalinga', 'segoescript', 'onyx', 
    'monotypecorsiva', 'perpetua', 'centaur', 'segoemarker', 'dilleniaupc', 'widelatin', 
    'gillsans', 'timesnewroman', 'dinproblack', 'aparajita', 'snapitc', 'berlinsansfbdemi',
    'simhei', 'frankruehl', 'harlowsolid', 'cooperblack', 'sylfaen', 'traditionalarabic', 
    'freestylescript', 'microsoftsansserif', 'gabriola', 'felixtitling', 'vrinda', 'angsananew', 
    'arial', 'lucidacalligraphy', 'impact', 'batangbatangchegungsuhgungsuhche', 'goudyoldstyle', 
    'wingdings2', 'showcardgothic', 'erasitc', 'wingdings', 'informalroman', 'twcen', 'comicsansms', 
    'aparajitaitali', 'consolas', 'mingliuextbpmingliuextbmingliuhkscsextb', 'kartika', 'segoeui', 'gautami',
    'gloucesterextracondensed', 'segoeuisemibold', 'extra', 'californianfb', 'gisha', 
    'meiryomeiryoboldmeiryouiboldmeiryouibolditalic', 'copperplategothic', 'plantagenetcherokee', 
    'luzsansbook', 'arabictypesetting', 'palacescript', 'juiceitc', 'jokerman', 'bodonipostercompressed',
    'tunga', 'niagarasolid', 'simsunextb', 'colonna', 'rockwellcondensed', 'msgothicmspgothicmsuigothic', 
    'lucidasansregular', 'franklingothicbook', 'corbel', 'msreferencesansserif', 'rod', 'magneto', 'twcencondensed', 
    'rockwell', 'vijaya', 'angsanaupc', 'engravers', 'papyrus', 'bodonicondensed', 'microsofthimalaya', 
    'harrington', 'berlinsansfb', 'cambriacambriamath', 'bookantiqua', 'eucrosiaupc', 'franklingothicmedium', 
    'segoeprint', 'blackadderitc', 'vinerhanditc', 'kristenitc', 'aharoni', 'jasmineupc', 'lucidasans',
    'iskoolapota', 'gulimgulimchedotumdotumche', 'ocraextended', 'microsoftyahei', 'leelawadee', 
    'meiryomeiryomeiryouimeiryouiitalic', 'browallianew', 'bauhaus93', 'franklingothicdemicond', 
    'simsunnsimsun', 'agencyfb', 'elephant', 'wingdings3', 'sketchflowprint', 'lucidafaxregular',
    'narkisim', 'gillsanscondensed', 'laoui', 'webdings', 'chiller', 'kunstlerscript', 'gigi', 'georgia', 
    'mingliupmingliumingliuhkscs', 'shruti', 'trajanproregular', 'euphemia', 'lilyupc', 'vladimirscript', 
    'mangal', 'bookshelfsymbol7', 'miriam', 'symbol', 'shonarbangla', 'msoutlook', 'curlz', 'calibri', 
    'khmerui', 'twcencondensedextra', 'calisto', 'rage', 'bradleyhanditc', 'parchment', 'lucidahandwriting', 
    'kokila', 'estrangeloedessa', 'imprintshadow', 'david', 'ravie', 'bodoniblack', 'lucidafax', 'dinprolight',
    'erasmediumitc', 'lucidabright', 'dfkaisb', 'gillsansultracondensed', 'poorrichard', 'raavi', 'browalliaupc',
    'segoeuisymbol', 'maiandragd', 'lucidasansroman', 'levenim', 'nyala', 'erasdemiitc', 'footlight', 
    'malgungothic', 'microsoftuighur', 'candara', 'bell', 'cordiaupc', 'latha', 'castellar', 'mistral',
    'andalus', 'lucidasanstypewriteroblique', 'trebuchetms', 'lucidaconsole', 'fangsong', 'swtortrajan',
    'daunpenh', 'century', 'forte', 'bernardcondensed', 'sakkalmajalla', 'niagaraengraved', 'broadway',
    'vivaldi', 'arialrounded', 'gillsansextcondensed', 'tahoma', 'arialms', 'haettenschweiler', 'dinproregular',
    'buxtonsketch', 'simplifiedarabic', 'britannic', 'centuryschoolbook', 'centurygothic', 'cambria', 'brushscript',
    'mvboli', 'hightowertext', 'cordianew', 'kaiti', 'rockwellextra', 'msmincho', 'utsaahitali',
    'simplifiedarabicfixed', 'microsoftphagspa', 'dokchampa', 'constantia', 'lucidasanstypewriterregular', 
    'kodchiangupc', 'palatinolinotype', 'lucidasanstypewriter', 'algerian', 'mongolianbaiti', 'irisupc', 
    'maturascriptcapitals', 'dinpromedium', 'frenchscript', 'msminchomspmincho', 'tempussansitc'
]

def render_text(font_name, size=36):
    try:
        font = pygame.font.SysFont(font_name, size)
        return font.render(text, True, BLACK), font_name
    except:
        return None, font_name

current_font_index = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_font_index = (current_font_index + 1) % len(fonts)
            elif event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(WHITE)

    rendered_text, font_name = render_text(fonts[current_font_index])
    if rendered_text:
        text_rect = rendered_text.get_rect(center=(width//2, height//2))
        screen.blit(rendered_text, text_rect)
    
    font_info = pygame.font.SysFont('Arial', 24).render(f"Font: {font_name}", True, BLACK)
    screen.blit(font_info, (10, 10))
    
    instruction = pygame.font.SysFont('Arial', 24).render("Press SPACE to change font, ESC to quit", True, BLACK)
    screen.blit(instruction, (10, height - 40))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()