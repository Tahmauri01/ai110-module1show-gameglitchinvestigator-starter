# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | 
|-------|-------------------|-----------------|------------------------|
|guess  |"Go Lower" hint    |"Go Higher" hint | none                   |   Fixed
|of 33  |                   |                 |                        |
|-------|-------------------|-----------------|------------------------|
|guess  |"Go Higher" hint   |"Go Lower" hint  | none                   |   Fixed
|of 31  |                   |                 |                        |
|-------|-------------------|-----------------|------------------------|
|pressed|Game to restart    |Old game data st-| none                   |
|"New   |                   |ays and new game |                        |
|Game"  |                   |is not started   |                        |
|button |                   |                 |                        |
|-------|-------------------|-----------------|------------------------|
|changed|Hard mode to have  |Normal mode has  | none                   |   Fixed
|diffic-|the largest range  |largest range and|                        |
|ulty   |and least attempts,|most attempts, r-|                        |
|       |easy mode have the |ange does not ch-|                        |
|       |most attempts, and |ange             |                        |
|       |for the range      |                 |                        |
|       |to change when swi-|                 |                        |
|       |tching difficulty  |                 |                        |
|-------|-------------------|-----------------|------------------------|
|guess  |Score gets subtrac-|Score goes up    | none                   |   Fixed
|that is|ted                |                 |                        |
|too hi-|                   |                 |                        |
|gh     |                   |                 |                        |
|-------|-------------------|-----------------|------------------------|
|guess 9|Hint to say "Go Hi-|Hint says "Go Lo-| none                   |   Fixed
|on an  |gher"              |wer"             |                        |
|even a-|                   |                 |                        |
|ttempt |                   |                 |                        |
|-------|-------------------|-----------------|------------------------|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

When figuring out how to make the New Game button work, Claude suggested that the code must reset the status, score and history of the game. This was the correct suggestion as the code did not previously reset these components which was needed for the new game to start and display. After implementing this into the code, I tested the game, pressed the new game button and a new game started, verifying that the suggestion was correct.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

When creating test cases, the AI was tasked with creating test cases for the bug fix which made it so the difficulties had the correct range and attempt amounts, and for the range to be reset and displayed correclty when switching difficulties. The test cases suggested were correct however, the AI created a new test_game_logic.py file outside of the tests folder. When running pytest, this caused an error since there were two test_game_logic.py files. To fix this I tasked the AI to merge the test_game_logic.py file outside of the tests folder with the one inside, resolving the issue when pytest was ran again.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

When a bug was claimed to be fixed, I went and tested it manually in the game.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

One test I ran was to see if the game gave the correct hint message when guessing a number higher or lower. Before, the code was bugged and gave a hint of "Go Higher" when you were supposed to go lower and vice versa. The secret number this test was 32, and entering a number 29, the game would give a hint of "Go Higher" showing that the code was now correct.

- Did AI help you design or understand any tests? How?

The AI helped designed the test cases by importing then running the functions from logic_utils.py with certain parameters. These test cases were put into test_game_logic.py then ran by me using pytest.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit rerun stops the program from running anything after it is called then restarts the program. Streamlit session state are the key variables that are needed to share data in between sessions which is used in a rerun.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

One habit I want to take away is putting my variables in a separate file to make the code less cluttered and easier to follow.

- What is one thing you would do differently next time you work with AI on a coding task?

One thing I will do differently is attempt to first fix the bugs myself instead of asking the AI to do it first.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

AI generated code comes with a lot more mistakes than I had previously thought. This shows me that software engineers are needed to make sure the code is clean with no bugs.