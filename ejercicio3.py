from agents import Agent, Runner
import asyncio

agent = Agent(name="Ortografía", instructions="De primero te presentas como un agente de ortografía y luego vas a corregir el texto del usuario poniendo el texto original y el corregido y ponlo en formato JSON ."
)

texto = input("Hola, bienvenido al agente de ortografía.\n Por favor ingreseme el texto que desea corregir: ")

async def main():
    result = await Runner.run(agent, texto)
    print(result)  
    print("Texto corregido:", result.final_output)  

asyncio.run(main())