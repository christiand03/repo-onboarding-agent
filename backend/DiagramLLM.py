import networkx as nx
import os
import sys

from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage
from langchain_core.output_parsers import PydanticOutputParser

sys.path.append(str(Path(__file__).parent.parent))
from schemas.types import DiagramRequest, DiagramOutput, GraphInput
from SystemPrompts import SystemPromptDiagramLLM

# .env laden
load_dotenv()


class SimpleLLMService:
    def __init__(self):
        self.api_key = os.getenv("SCADS_AI_KEY")
        self.api_url = os.getenv("SCADSLLM_URL")
        self.model_name = "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct"

        if not self.api_key or not self.api_url:
            raise ValueError("SCADS_API_KEY und SCADS_API_URL müssen in .env gesetzt sein!")

        print(f"✅ LLM Service initialisiert mit {self.model_name}")

    def generate_schema(self, request: DiagramRequest) -> DiagramOutput | None:
        model = ChatOpenAI(
            model=self.model_name,
            api_key=self.api_key,
            base_url=self.api_url,
            temperature=0.2,
        )

        parser = PydanticOutputParser(pydantic_object=DiagramOutput)

        prompt = SystemPromptDiagramLLM.build_prompt_from_request(
            request=request,
            format_instructions=parser.get_format_instructions()
        )

        try:
            response = model.invoke([
                HumanMessage(content=prompt)
            ])
            print(response.usage_metadata)
            return parser.parse(response.content)

        except Exception as e:
            print("❌ Diagram could not be created:")
            print(e)
            print("\nRaw LLM output:")
            print(response.content if 'response' in locals() else None)
            return None 
        

def graph_to_valid_input(graph: nx.DiGraph) -> GraphInput:
    nodes = []

    for node_id in graph.nodes:
        node_data = {
            "id": node_id,
            "type": "function"
        }

        parts = node_id.split("::")

        if len(parts) >= 1:
            node_data["file"] = parts[0]

        if len(parts) == 2:
            node_data["function"] = parts[1]
            node_data["class"] = None
        elif len(parts) >= 3:
            node_data["class"] = parts[1]
            node_data["function"] = parts[2]

        node_data["in_degree"] = graph.in_degree(node_id)
        node_data["out_degree"] = graph.out_degree(node_id)
        node_data["total_degree"] = graph.degree(node_id)

        nodes.append(node_data)


    edges = [
        (caller, callee, {"type": "function_call", "direction": "calls"})
        for caller, callee in graph.edges
    ]

    metadata = {
        "num_nodes": graph.number_of_nodes(),
        "num_edges": graph.number_of_edges(),
        "is_dag": nx.is_directed_acyclic_graph(graph),
        "avg_degree": (
            sum(dict(graph.degree()).values()) / graph.number_of_nodes()
            if graph.number_of_nodes() > 0 else 0
        )
    }

    if graph.number_of_nodes() > 0:
        degrees = dict(graph.degree())
        max_degree = max(degrees.values()) if degrees else 0
        hot_functions = [
            node for node, degree in degrees.items() if degree >= max_degree * 0.7
        ]
        metadata["hot_functions"] = hot_functions

    return GraphInput(
        nodes=nodes,
        edges=edges,
        graph_type="callgraph",
        metadata=metadata
    )


if __name__ == "__main__":
    from callgraph import build_filtered_callgraph
    from File_Dependency import build_repository_graph
    from getRepo import GitRepository
    from schemas.types import DiagramRequest
    from schemas.enums import AnalysisMode, DiagramFocus

    repo_url = "https://github.com/christiand03/repo-onboarding-agent"

    with GitRepository(repo_url) as repository:
        print("Building callgraph...")
        callgraph = build_filtered_callgraph(repository)
        file_dependency = build_repository_graph(repository)

        print(f"Callgraph hat {callgraph.number_of_nodes()} Knoten")

        graph_input = graph_to_valid_input(callgraph)
        print(f"GraphInput: {len(graph_input.nodes)} nodes, {len(graph_input.edges)} edges")
        
        graph_input_2 = graph_to_valid_input(file_dependency)
        print(f"GraphInput: {len(graph_input_2.nodes)} nodes, {len(graph_input_2.edges)} edges")
        llm = SimpleLLMService()

        requests = []
        request = DiagramRequest(
            nodes=graph_input.nodes,
            edges=graph_input.edges,
            mode=AnalysisMode.STANDARD,
            focus=DiagramFocus.CALL_GRAPH
        )
        requests.append(request)

        r2 = DiagramRequest(
            nodes=graph_input_2.nodes,
            edges=graph_input_2.edges,
            mode=AnalysisMode.OVERVIEW,
            focus=DiagramFocus.ARCHITECTURE
        )
        requests.append(r2)

        for r in requests:
            print("Generating diagram...")
            output = llm.generate_schema(r)

            if output is None:
                print("No diagram generated.")
            else:
                print("\nDiagram Type:")
                print(output.diagramtype.value)

                print("\nMermaid Code:")
                print(output.mermaid_code)

                print("\nExplanation:")
                print(output.explanation)
