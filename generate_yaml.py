import os
import logging

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('yaml_generation.log')
    ]
)
logger = logging.getLogger(__name__)

def generate_yaml(data_dir: str, classes: list, output_path: str) -> bool:
    """
    Generate YAML file for YOLOv8 training.
    
    Args:
        data_dir (str): Path to dataset directory (e.g., './food-101')
        classes (list): List of class names (e.g., ['pizza', 'grilled_chicken', ...])
        output_path (str): Path to save YAML file (e.g., './food-101/food101.yaml')
    
    Returns:
        bool: True if YAML created successfully, False otherwise
    """
    try:
        # Ensure data_dir exists
        if not os.path.exists(data_dir):
            raise ValueError(f"Dataset directory {data_dir} does not exist")
        
        # YAML content
        yaml_content = f"""
train: {os.path.join(data_dir, 'images/train')}
val: {os.path.join(data_dir, 'images/test')}
nc: {len(classes)}
names: {classes}
"""
        # Save YAML file
        with open(output_path, 'w') as f:
            f.write(yaml_content)
        logger.info(f"YAML file created at {output_path}")
        return True
    except Exception as e:
        logger.error(f"Error generating YAML file: {str(e)}")
        return False

if __name__ == "__main__":
    # Configuration
    data_dir = "./foof/food-101"
    classes = ['pizza', 'grilled_chicken', 'sushi', 'ice_cream', 'hamburger']
    yaml_path = os.path.join(data_dir, 'food101.yaml')
    
    # Generate YAML
    success = generate_yaml(data_dir, classes, yaml_path)
    if success:
        logger.info("YAML generation completed successfully")
    else:
        logger.error("YAML generation failed")