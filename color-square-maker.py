#!/usr/bin/env/python3
# Import the required modules
from PIL import Image, ImageDraw, ImageFont
import re
import textwrap

emotion_color_map = {
        "Curiosity": "A color named \"curiosity\" might be a vibrant, electric blue color. It could be a color that is bold and attention- grabbing, with a hint of mystery and intrigue. Its hex code might be something like #00b2ff, a bright and lively blue color with a slight hint of purple. This color would be perfect for representing curiosity and sparking imagination and creativity.",
        "Tenacity": "The color \"tenacity\" might be a deep, rich shade of red. It could be a color that is strong and steadfast, with a sense of determination and resilience. Its hex code might be something like #7f0000, a deep and powerful red that conveys a sense of strength and endurance. This color would be perfect for representing tenacity and the ability to persevere through challenges.",
        "Contentment": "Contentment is a color that is associated with satisfaction, peace, and fulfillment. It is a warm and soothing shade of blue or green, with hints of comfort and security. The hex code for contentment might be something like #0099CC, a tranquil and peaceful hue that captures the feeling of being content and at ease.",
        "Bliss": "Bliss is a color that is associated with happiness, contentment, and joy. It is a vibrant and lively shade of yellow or green, with hints of sunshine and warmth. The hex code for bliss might be something like #00FF00, a cheerful and energetic hue that captures the feeling of pure, unadulterated joy.",
        "Nirvana": "Nirvana could be described as a sense of enlightenment or transcendence, of reaching a state of perfect happiness and contentment. It might be represented by a color that is otherworldly or ethereal, such as a radiant gold or a deep, rich purple. The hex code for nirvana might be something like #FFD700, a radiant and luminous hue that captures the feeling of reaching a state of spiritual fulfillment.",
        "Chrysalism": "Chrysalism could be described as a sense of peacefulness or calm that comes from being sheltered or protected from the outside world. It might be represented by a color that is soothing or calming, such as a soft blue or a warm, muted green. The hex code for chrysalism might be something like #99CCCC, a tranquil and peaceful hue that captures the feeling of being safe and secure within one's own private world.",
        "Occhiolism": "Occhiolism could be described as a sense of smallness or insignificance, of feeling like a small part of something much larger and more complex. It might be represented by a color that is understated or muted, such as a soft grey or a pale, washed-out blue. The hex code for occhiolism might be something like #CCCCCC, a barely- there color that captures the feeling of being a tiny part of a vast and overwhelming world.",
        "Rubatosis": "Rubatosis could be described as a feeling of discomfort or unease caused by one's own heartbeat. It might be represented by a color that is unsettling or disorienting, such as a deep, intense red or a murky, pulsating shade of black. The hex code for rubatosis might be something like #800000, a rich and bold color that captures the feeling of being overwhelmed by one's own physical sensations.",
        "Liberosis": "Liberosis is a carefree, lighthearted color that evokes a sense of freedom and ease. It is a vibrant, playful shade of yellow or orange, with hints of sunshine and warmth. The hex code for liberosis might be something like #F8D568, a cheerful and energetic hue that captures the feeling of letting go and living in the moment.",
        "Monachopsis": "Monachopsis could be described as a sense of being out of place or disconnected, of feeling a subtle but persistent sense of longing or dissatisfaction. It might be represented by a color that is muted, hazy, or ill-defined, such as a pale grey with hints of blue or green, or a soft, diffused pastel shade. The hex code for monachopsis might be something like #CCCCCC, a barely-there color that captures the essence of being on the fringes or outside of the mainstream.",
        "Hope": "Hope is a color that evokes a feeling of optimism and possibility. It is a bright, vibrant shade of blue, with hints of green and a touch of purple. It is the color of a clear summer sky, or of a blooming flower. The hex code for hope might be something like #3A9CD7.",
        "Nostalgia": "Nostalgia is a color that evokes a sense of warmth and longing for the past. It is a soft, muted shade of blue, with hints of gray and a touch of purple. It is the color of a clear autumn sky, or of a forgotten memory. The hex code for nostalgia might be something like #B4C4D8.",
        "Despair": "Despair is a color that evokes feelings of hopelessness and defeat. It is a dark, muted shade of gray, with hints of black and a touch of blue. It is the color of a stormy sky, or of a soul in pain. The hex code for despair might be something like #454F57.",
        "Indignation": "Indignation is a color that evokes feelings of anger and righteousness. It is a bright, fiery shade of red, with hints of orange and yellow. It is the color of a burning flame, or of a passionate heart. The hex code for indignation might be something like #E25E4C.",
        "Ennui": "Ennui is a color that evokes a feeling of boredom and apathy. It is a dull, washed-out shade of beige, with hints of white and gray. It is the color of a cloudy sky, or of a mind numbed by monotony. The hex code for ennui might be something like #C4B8A1.",
        "Nostalgia": "Nostalgia is a color that evokes a sense of warmth and longing for the past. It is a soft, muted shade of blue, with hints of gray and a touch of purple. It is the color of a clear autumn sky, or of a forgotten memory. The hex code for nostalgia might be something like #B4C4D8.",
}

size = 500

def extract_hex_code(string):
    # Use a regular expression to search for a hexadecimal value in the string
    hex_code = re.search(r'#[a-fA-F0-9]{6}', string)

    # Return the hexadecimal value if found, or None if not found
    if hex_code:
        return hex_code.group()
    else:
        return None

def generate_color_png(emotion, description):
    # Create a new image with the specified size
    img = Image.new('RGB', (size, size), color=extract_hex_code(description))

    # Create a drawing context
    draw = ImageDraw.Draw(img)

    # Load the Helvetica font
    fontname="Arial.ttf"
    fontpath="/System/Library/Fonts/Supplemental/"
    h1 = ImageFont.truetype(fontpath + fontname, size=48)
    p1 = ImageFont.truetype(fontpath + fontname, size=20)

    # Measure the size of the text
    text_width, text_height = draw.textsize(emotion, font=h1)

    # Calculate the x and y coordinates of the text
    x = (size - text_width) / 2
    y = 20

    # Draw the text on the image
    draw.text((x, y), emotion, font=h1, fill='white')

    # Calculate the x and y coordinates of the second line of text
    x = 20
    y += text_height + 20

    # Draw the second line of text on the image
    #draw.text((x, y), description, font=p1, fill='white')
    lines = textwrap.wrap(description, width=50)
    for line in lines:
        width, height = p1.getsize(line)
        draw.text((x, y), line, font=p1, fill='white')
        y += height+5


    # Save the image to a file
    img.save("images/" + emotion + '.png')

for emotion, description in emotion_color_map.items():
    generate_color_png(emotion, description)
