# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

After having performed some exploratory testing (specifically system tests) on the game via the streamlit UI,
I noticed the following concrete bugs: 

1. After switching between the three difficulty modes, normal (currently 1-100) should be
replaced with hard (currently 1-50).

2. We can guess outside the expected range 1-100; for example, 123 is currently an acceptable input

3. The hints ("go lower" and "go higher") are inconsistent and seem to be random?

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used ChatGPT to summarize project instructions and reiterate them in a clear, coherent manner. I then used Claude Code as the execution agent to perform all tasks on my behalf.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

The suite of pytests that were generated were robust and aligned with the type of tests I would have written for the get_range_for_difficulty function.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

So suggestions aside, when I asked Claude Code to generate a suite of pytests for the get_range_for_difficulty function, it created a test directory with a test_game_logic file when there was already an existing directory called tests with the same file. Running /init would have prevented this as Claude would have had filetree context and I verified the result by observing each action the agent executed to ensure it aligns with my intent.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided that a bug was indeed fixed by running system tests on the streamlit app to manually verify everything works as intended.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I ran system tests by toggling through the different difficulty ranges and also the pytests.

- Did AI help you design or understand any tests? How?

AI helped my design a comprehensive suite of tests, understanding isn't really necessary (syntactically speaking) here as I verified everything works as intended by testing manually.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

Running /init to establish context and repo-awareness so that Claude Code doesn't hallucinate. Also, continuing to verify everything works the way I did which involves a human serving as the judgement/verification layer and manually testing the fix/enhancement to ensure the output aligns with developer intent.

- What is one thing you would do differently next time you work with AI on a coding task?

One thing I would do differently is to take it one step at time. Because I have experience vibecoding, I tend to one-shot everything and provide robust context to enable it to work as intended but I think a slow, systematic approach is useful here for the purposes of learning.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project changed the way I think such that, like I mentioned above, it allows one to slow down and approach a problem systematically. Moreover, there is structure and the process is broken down into agile, actionable steps from observation, to documenting potential bugs, debugging one at at time which is great in terms of preventing any regression, and runnning unit tests on each software component (or function) to ensure it works. 
