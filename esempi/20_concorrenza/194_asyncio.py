# Esempio 194 — asyncio permette concorrenza cooperativa per I/O.
import asyncio
async def demo():
    await asyncio.sleep(0)
    return "ok"
print(asyncio.run(demo()))
