from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..retrieval.retriever_chain import qa_chain

router = APIRouter()

class QuestionRequest(BaseModel):
    query: str

@router.post("/ask-question")
async def ask_question(request: QuestionRequest):
    try:
        user_query = request.query
        if not user_query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty.")

        # Run the query through the retriever + LLM chain
        response = qa_chain.run(user_query)

        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
