from langchain.agents import create_agent


class SpawnAgent:
    @staticmethod
    def get_agent(model, tools, system_prompt="You are a helpful assistant", **kwargs):
        agent = create_agent(
            model=model,
            tools=tools,
            system_prompt=system_prompt,
            **kwargs
        )
        return agent