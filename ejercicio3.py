from agents import Agent, Runner

agent = Agent(name="Ortografia", instructions="De primero te presentas como un agente de ortografia y luego, tu tarea es ayudar al usuario a corregir sus textos y poner que estaba mal escrito y identificar si lleva algun tipo de signo si llega a ingresar algun tipo de dato numerico le diras que no se puede corregir este dato y si te dan las gracias a ti solo agradece de regreso diciendo que tenga un buen dia.")

result = Runner.run_sync(agent, "Gracias.")
print(result.final_output)

