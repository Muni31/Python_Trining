# Create a log file using logger module. Write a function display_words() in python to read lines from 
# a text file "story.txt" (take the file name from user), and display those words in INFO level log, 
# for those words which are less than 4 characters needs to be logged as in CRITICAL level log.  
# If user enter the wrong file name in input then raise ERROR in log file
  
import logging

def display_words(file_name):
  
    logger = logging.getLogger('word_logger')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('word_log.log')
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    if len(word) < 4:
                        logger.critical("CRITICAL: %s", word)
                    else:
                        logger.info("INFO: %s", word)
    except FileNotFoundError:
        logger.error("ERROR: File not found - %s", file_name)
        raise

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    display_words(file_name)

  