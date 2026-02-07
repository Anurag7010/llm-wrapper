import time
from logger import logger

def retry_with_backoff(func, retries=3, delay=1):
    """
    Retry a function with exponential backoff.
    
    Args:
        func: Function to retry
        retries: Maximum number of retry attempts
        delay: Initial delay in seconds (doubles each attempt)
    
    Returns:
        Result of func() if successful
        
    Raises:
        Exception: After all retries exhausted
    """
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            
            if attempt == retries - 1:
                logger.error(f"All {retries} attempts failed: {e}")
                raise Exception("All retry attempts failed") from e
            wait_time= delay * (2 ** attempt)
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time} seconds.")
            time.sleep(wait_time)   
            
            
    
    