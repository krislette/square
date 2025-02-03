from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from main import tokenize_string
from backend.lexer.errors import TokenizationError


# Initialize app
app = FastAPI()

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],    # Allows all methods
    allow_headers=["*"],    # Allows all headers
)

# Set up rate limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter


# Pydantic model for request validation
class SourceCode(BaseModel):
    code: str


@app.get("/")
@limiter.limit("50/minute")
async def root(request: Request):
    return {
        "message": "Welcome to the Square's tokenizer API!",
        "endpoints": {
            "/": "This welcome message",
            "/tokenize": "POST endpoint to tokenize source code"
        }
    }


@app.post("/tokenize")
@limiter.limit("50/minute")
async def tokenize(request: Request, source: SourceCode):
    try:
        tokens = tokenize_string(source.code)
        return {"status": "success", "tokens": tokens}
    except TokenizationError as e:
        return {
            "status": "error",
            "error": {
                "type": "TokenizationError",
                "message": str(e),
                "details": {
                    "line": e.line,
                    "column": e.column,
                    "invalid_token": e.token
                }
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
