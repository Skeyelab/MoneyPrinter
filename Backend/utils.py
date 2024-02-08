import os
import logging
import g4f
import json
import re
from termcolor import colored

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def clean_dir(path: str) -> None:
    """
    Removes every file in a directory.

    Args:
        path (str): Path to directory.

    Returns:
        None
    """
    try:
        if not os.path.exists(path):
            os.mkdir(path)
            logger.info(f"Created directory: {path}")

        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            os.remove(file_path)
            logger.info(f"Removed file: {file_path}")

        logger.info(colored(f"Cleaned {path} directory", "green"))
    except Exception as e:
        logger.error(f"Error occurred while cleaning directory {path}: {str(e)}")


def call_gpt_model(prompt: str, model_name: str) -> str:
    """
    Encapsulates the logic for making calls to the GPT model and handling the response.

    Args:
        prompt (str): The prompt to be sent to the model.
        model_name (str): The name of the GPT model to use.

    Returns:
        str: The raw response from the GPT model.
    """
    response = g4f.ChatCompletion.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
    )
    return response


def clean_response(response: str) -> str:
    """
    Cleans the raw response string from the GPT model.

    Args:
        response (str): The raw response string to be cleaned.

    Returns:
        str: The cleaned response.
    """
    # Remove asterisks and hashes
    response = response.replace("*", "")
    response = response.replace("#", "")

    # Remove markdown syntax
    response = re.sub(r'\[.*\]', '', response)
    response = re.sub(r'\(.*\)', '', response)

    return response
