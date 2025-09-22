from agents import Agent, Runner
import asyncio

agent = Agent(
    name="Ortografía", instructions="De primero te presentas como un agente de ortografía y luego vas a corregir el texto del usuario poniendo el texto original y el corregido, mencionando lo que estaba malo, solo quiero que muestres esto que te estoy mencionando."
)

texto = input("Hola, bienvenido al agente de ortografía.\nPor favor ingresa el texto que deseas corregir: ")

async def main():
    result = await Runner.run(agent, texto)
    print(result)  
    print("Texto corregido:", result.final_output)  

asyncio.run(main())