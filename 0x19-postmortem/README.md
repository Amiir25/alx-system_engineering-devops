Postmortem: The Great Maze Lag of 2025


Issue Summary

🕒 Duration: 
- March 1, 2025, 18:00 UTC - March 1, 2025, 19:45 UTC (1 hour 45 minutes)

Impact:
- FPS dropped from a silky smooth 60 FPS to a slideshow-like 5 FPS.
- Input lag turned the game into a turn-based experience (unintended feature? Nope.)
- 100% of players affected = 100% frustration.
- One developer almost rage-quit his own project.

Root Cause:
- The render loop was brute-force drawing every wall in the maze every single frame—even if the player couldn’t see them.
- Our GPU cried, begged for mercy, and eventually gave up.


Timeline of the Disaster

18:00 UTC - Playtest begins. Everything is fine… until it isn’t.
18:05 UTC - Noticed FPS tanking. "Maybe it’s just my laptop?" Nope. It’s happening everywhere.
18:15 UTC - Checked SDL2 event handling. Input lag confirmed. This isn't just a rendering issue—it's a full system meltdown.
18:30 UTC - Investigated texture loading. Looked promising at first, but nope, wrong path (foreshadowing).
19:00 UTC - Finally looked at the render loop. Oh. Oh no. Every wall in the entire maze was being drawn, whether visible or not.
19:15 UTC - Added a quick frustum culling hack to only draw walls in the camera view. Immediate FPS boost!
19:45 UTC - FPS restored. Input lag gone. Developer rage minimized.


Cause and The Fix

What Went Wrong?
Imagine if, every time you wanted to check who’s in your room, you also checked every room in your house. And your neighbor’s house. And their neighbor’s house.
That’s what our render loop was doing. Every. Single. Frame.

How We Fixed It:
✔️ Implemented Frustum Culling - If the player can’t see it, it doesn’t exist (kinda).
✔️ Optimized the render loop - No more unnecessary wall drawing.
✔️ GPU stopped sending us angry emails.


Lessons Learned & Preventative Measure

Improvements Needed:
✔️ Make the render loop less dumb.
✔️ Monitor FPS in real-time so we don’t get blindsided again.
✔️ Use spatial partitioning to optimize culling (e.g., Quadtrees, BSP).

Action Items:
- Refactor rendering logic to avoid redundant draw calls.
- Implement an FPS counter (so performance drops don’t sneak up on us).
- Use SDL2’s texture batching to reduce GPU workload.
- Set up automated performance testing (so we never make this mistake again).


One Picture Worth a Thousand Words

Here’s a simplified visual representation of what went wrong:


❌ Before the Fix (Render Everything Everywhere)



✔️ After the Fix (Render Only What You See)




Final Thoughts

Debugging this was like escaping our own maze—confusing, frustrating, and full of dead ends. But in the end, we conquered the lag monster.
FPS is back, input lag is gone, and the game is finally playable again. Until the next bug. 
