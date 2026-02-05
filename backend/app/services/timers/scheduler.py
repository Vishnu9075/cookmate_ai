from __future__ import annotations
import asyncio
from app.services.timers.service import mark_done_if_expired

async def timer_scheduler_loop(timer_store: dict, interval_seconds: int=2):
    """
    MVP polling loop:
    - every N seconds, scan timers and mark expired ones DONE
    """

    while True:
        try:
            for tid, t in list(timer_store.items()):
                if t.status == "RUNNING":
                    timer_store[tid] = mark_done_if_expired(t)

        except Exception:
            #keep loop alive in MVP
            pass

        await asyncio.sleep(interval_seconds)

    