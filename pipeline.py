from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

def run_research_pipeline(topic : str) -> dict:
    state = {}

    # Step 1: Search Agent gathers research
    print("\n" + "="*50)
    print("Step 1: Search Agent Gathering Research....")
    print("\n" + "="*50)
    search_agent = build_search_agent()
    search_result = search_agent.invoke(
            {
                "messages":  [
                    (
                        "user", f"Find recent, detailed and reliable information on the topic: {topic}. Provide titles, URLs and snippets of the content."
                    )
                ]
            }
        )
    state["search_result"] = search_result["messages"][-1].content
    print("\nSearch Results:\n", state["search_result"])


    # Step 2: Reader Agent scrapes top URLs for deeper reading
    print("\n" + "="*50)
    print("Step 2: Reader Agent Scraping Top URLs....")
    print("\n" + "="*50)
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke(
        {
            "messages":  [
                (
                    "user", f"Based on the following search results about topic '{topic}'," 
                    f"pick the most relevant URL and scrape it for deeper content.\n\n"
                    f"Search Results:\n{state['search_result'][:1000]}\n\n" 
                )  
            ]
        }
    )
    state["scraped_content"] = reader_result["messages"][-1].content
    print("\nScraped Content:\n", state["scraped_content"])


    # Step 3: Writer Chain compiles the research into a report
    print("\n" + "="*50)
    print("Step 3: Writer Chain Compiling Research into Report....")
    print("\n" + "="*50)
    research_combined = (
        f"Search Results:\n{state['search_result']}\n\n"
        f"Scraped Content:\n{state['scraped_content']}\n\n"
    )
    state["report"] = writer_chain.invoke(
        {
            "topic": topic,
            "research": research_combined
        }
    )
    print("\nGenerated Report:\n", state["report"])


    # Step 4: Critic Chain evaluates the report
    print("\n" + "="*50)
    print("Step 4: Critic Chain Evaluating Report....")
    print("\n" + "="*50)
    state["feedback"] = critic_chain.invoke(
        {
            "report": state["report"]
        }
    )
    print("\nCritic's Feedback:\n", state["feedback"])

    return state



if __name__ == "__main__":
    topic = input("\nEnter a research topic: ")
    run_research_pipeline(topic)