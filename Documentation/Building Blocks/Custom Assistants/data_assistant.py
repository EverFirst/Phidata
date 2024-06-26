from dotenv import load_dotenv
load_dotenv()

import json
from phi.assistant.duckdb import DuckDbAssistant

duckdb_assistant = DuckDbAssistant(
    semantic_model=json.dumps({
        "tables": [
            {
                "name": "movies",
                "description": "Contains information about movies from IMDB.",
                "path": "https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
            }
        ]
    }),
    show_tool_calls=True,
)

duckdb_assistant.print_response("What is the average rating of movies? Show me the SQL.")
