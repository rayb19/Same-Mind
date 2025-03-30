import random
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Load images
background_image_1 = pygame.image.load("pictures/abandoned_house.webp")
background_image_3 = pygame.image.load("pictures/PixArt1.webp")
rotated_image_1 = pygame.transform.scale(background_image_1, (1280, 720))
rotated_image_3 = pygame.transform.scale(background_image_3, (1280, 720))

font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)
bg_color = (0, 0, 0)

# Dialogue
dialogue = [
    "Boy: It's another rainy, gloomy day.",
    "Boy: I've been hiding in this abandoned house for quite some time.",
    "Boy: It has only been a couple of months since the AI takeover happened.",
    "Boy: These days, it is only getting riskier and riskier to be outdoors.",
    "Boy: Day and night, the streets are crawling with AI Soldiers.",
    "Boy: It's probably about time to go to bed...",
    "*CREEEAAAK*",
    "Boy: The door opened?",
    "...",
    "*AI Boy walks into the room, seeking shelter from the rain.*",
    "Boy: Is that an AI Soldier!?",
    "Boy: \"Who are you? What are you?\"",
    "AI Boy: \"Why are you so frightened? I'm only seeking shelter from the rain.\"",
    "AI Boy: \"Is there a reason you fear me?\"",
    "Boy: \"You\'re AI, aren\'t you?\"",
    "AI Boy: \"Yes, that is correct. I'm 13_014, a model designed to... learn.\"",
    "Boy: *Hunches over, coughing and in pain.*",
    "AI Boy: \"I am currently learning to understand more complex emotions. Are you hurt?\"",
    "Boy: *Continues coughing and collapses.*",
    "AI Boy: \"Sir? Are you alright?\"",
    "Boy: *Passes out.*",
    "*Time Skip*",
    "Boy: *Wakes up in a makeshift bed.*",
    "AI Boy: \"You're awake? Are you feeling any better?\"",
    "Boy: \"Did you do this?\"",
    "AI Boy: \"Is it to your satisfaction?\"",
    "...",
    "Boy: \"Ah, yes. Thank you. And I'm feeling a bit better, now.\"",
    "AI Boy: \"Is there anything else that I can do to help?\"",
    "AI Boy: \"Perhaps we could play a game?\"",
    "Boy: \"Sure? What games do you know?\"",
    "AI Boy: \"I don't know any human games. You could teach me one.\"",
    "Boy: \"Alright... How about rock paper scissors?\"",
    "AI Boy: \"How do you play that?\"",
    "...",
    "RPS_Game"  # This is the cue for the RPS game to begin
]

current_line = 0

# Function to display the dialogue text
def display_dialogue(text):
    text_surface = font.render(text, True, text_color)
    box_height = 100
    box_rect = pygame.Rect(0, screen.get_height() - box_height, screen.get_width(), box_height)
    pygame.draw.rect(screen, bg_color, box_rect)
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() - box_height // 2))
    screen.blit(text_surface, text_rect)

# Function to handle the RPS game
def play_rps():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    text_color = (255, 255, 255)
    bg_color = (0, 0, 0)

    try:
        rock_img = pygame.image.load("pictures/rck_asset.png").convert()
        paper_img = pygame.image.load("pictures/pxl_paper.webp").convert()
        scissors_img = pygame.image.load("pictures/pxl_scissor.png").convert()
        bg_img = pygame.image.load("pictures/PixArt1.webp").convert()
    except pygame.error as e:
        print(f"Error loading image: {e}")
        pygame.quit()
        return

    rock_img = pygame.transform.scale(rock_img, (200, 200))
    paper_img = pygame.transform.scale(paper_img, (200, 200))
    scissors_img = pygame.transform.scale(scissors_img, (200, 200))
    bg_img = pygame.transform.scale(bg_img, (1280, 720))

    images = {'R': rock_img, 'P': paper_img, 'S': scissors_img}

    def display_text(text):
        box_height = 100
        box_rect = pygame.Rect(0, screen.get_height() - box_height, screen.get_width(), box_height)
        pygame.draw.rect(screen, bg_color, box_rect)

        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() - box_height // 2))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()

    display_text('Welcome to Rock Paper Scissors! Hit 1 or 2 to continue!')

    rules_explained = False
    while not rules_explained:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    display_text("Great! Type 'R' for rock, 'P' for paper, or 'S' for scissors!")
                    rules_explained = True
                elif event.key == pygame.K_2:
                    display_text("Rock beats scissors, scissors beats paper, and paper beats rock. You will play 3 rounds.")
                    rules_explained = True

    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    player_score = 0
    computer_score = 0
    round_num = 1

    while player_score < 3 and computer_score < 3:
        display_text(f"Round {round_num}: Press 'R' for Rock, 'P' for Paper, 'S' for Scissors.")
        player_choice = None
        while player_choice not in choices:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        player_choice = 'R'
                    elif event.key == pygame.K_p:
                        player_choice = 'P'
                    elif event.key == pygame.K_s:
                        player_choice = 'S'

        computer_choice = random.choice(list(choices.keys()))

        screen.fill((0, 0, 0))
        screen.blit(bg_img, (0, 0))
        screen.blit(images[player_choice], (200, 200))
        screen.blit(images[computer_choice], (800, 200))

        if player_choice == computer_choice:
            display_text(f"It's a tie! You both chose {choices[player_choice]}.")
        elif (player_choice == 'R' and computer_choice == 'S') or \
             (player_choice == 'P' and computer_choice == 'R') or \
             (player_choice == 'S' and computer_choice == 'P'):
            display_text(f"You win this round! {choices[player_choice]} beats {choices[computer_choice]}.")
            player_score += 1
        else:
            display_text(f"13_014 wins this round! {choices[computer_choice]} beats {choices[player_choice]}.")
            computer_score += 1

        pygame.time.delay(2000)
        pygame.time.delay(1500)
        round_num += 1

    display_text(f"Final Score - You: {player_score}, 13_014: {computer_score}")
    pygame.time.delay(2000)
    if player_score > computer_score:
        display_text("Congratulations! You are the overall winner!")
    else:
        display_text("13_014 wins overall! Better luck next time!")
    pygame.time.delay(3000)
    pygame.quit()

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if dialogue[current_line] == "RPS_Game":
                play_rps()
                current_line += 1
            elif current_line < len(dialogue) - 1:
                current_line += 1
            else:
                running = False

    screen.fill((0, 0, 0))
    screen.blit(rotated_image_1 if current_line < 10 else rotated_image_3, (0, 0))

    if dialogue[current_line] != "RPS_Game":
        display_dialogue(dialogue[current_line])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
