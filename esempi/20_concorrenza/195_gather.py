# Esempio 195 — gather attende più coroutine; qui non c'è traffico di rete.
import asyncio
async def valore(n):
    await asyncio.sleep(0)
    return n
async def main():
    return await asyncio.gather(valore(1), valore(2))
print(asyncio.run(main()))
