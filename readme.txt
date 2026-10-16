

mkdir langgraph-groq
cd langgraph-groq

python3 -m venv .venv
source .venv/bin/activate

pip install -U langgraph langchain-groq

python -m pip install ipython