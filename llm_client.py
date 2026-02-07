import time
from openai import OpenAI
from config import get_openrouter_key, get_base_url
from retry import retry_with_backoff
from logger import logger

client = OpenAI(api_key=get_openrouter_key(), base_url=get_base_url(), timeout=30) 

def generate_response(prompt):
    """
    
    Args:
        prompt (str): User prompt
        
    Returns:
        dict: {
            "response": str,
            "latency": float,
            "success": bool,
            "prompt_length": int,
            "retries": int,
            "error": str (optional)
        }
    """
    retry_count = 0
    
    def call_api(): # called inside the upper function so that we can retry 
        nonlocal retry_count
        retry_count += 1
        start_time = time.time() 
        
        
        
        try:
            
            response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,)
            
            latency = time.time() - start_time # track time
            logger.info(
                f"prompt_len={len(prompt)} "
                f"latency={latency:.2f}s "
                f"success=True "
                f"retries={retry_count - 1}"
            )
            content=extract_response(response) # extract content from response
            return {
                "prompt_length": len(prompt),
                "retries": retry_count - 1, 
                "success": True,
                "latency": latency,
                "response": content,
            }
            
        except Exception as e:
            latency = time.time() - start_time # track time
            
            logger.error( #Use ERROR level for failures
                f"prompt_len={len(prompt)} "                f"latency={latency:.2f}s "
                f"success=False "                f"retries={retry_count - 1} "
                f"error={str(e)}"
            )
            
            raise 
    try :
        return retry_with_backoff(call_api)
    except Exception as e:
        #after all retries are failed
        return {
            "prompt_length": len(prompt),
            "retries": retry_count,
            "success": False,
            "latency": None,
            "response": None,
            "error": str(e)
        }    
        
        
def extract_response(response):
    try:
        if not response.choices:
            raise Exception("No choices in response")
        
        choices = response.choices[0]
        
        if not choices.message or not choices.message.content:
            raise Exception("No message content in choices")
        
        content= choices.message.content
        
        return content
    except Exception as e:
        logger.error(f"Failed to extract response: {e}")
        raise Exception("Response extraction failed") from e
    

