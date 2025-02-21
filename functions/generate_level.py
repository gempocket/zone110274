
import importlib

def generate_level(background, middleground, foreground, current_level, generated_level):
    # Import the level module dynamically
    level_module = importlib.import_module(f'levels.{current_level}')
    
    # Extract lists from the imported module
    level_data = getattr(level_module, current_level)
    
    current_position = 0
    
    for sprite_data in level_data:
        # Assuming sprite_data contains the sprite class and its parameters
        sprite_class = sprite_data['class']
        sprite_params = sprite_data['params']
        
        # Create an instance of the sprite
        sprite_instance = sprite_class(*sprite_params, x=current_position)
        
        # Place the sprite in the appropriate group
        if sprite_data['group'] == 'background':
            background.add(sprite_instance)
        elif sprite_data['group'] == 'middleground':
            middleground.add(sprite_instance)
        elif sprite_data['group'] == 'foreground':
            foreground.add(sprite_instance)
        
        # Update the position for the next sprite
        current_position += sprite_instance.width  # Assuming each sprite has a width attribute
