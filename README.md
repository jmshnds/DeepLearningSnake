# DeepLearningSnake
Deep Learning in classic Snake game.<br/>
DQN and concept based off of DeepLearningFlappyBird by yenchenlin: https://github.com/yenchenlin/DeepLearningFlappyBird <br/>
Snake game made using Pygame, based on: https://github.com/jmshnds/PySnake <br/>
<br/>
My goal is to get a working snake AI and try it out with other variations of Snake games. <br/>

## Usage
Modify FPS settings in `gamestate.py` as needed.<br/>
In `pysnake.py` the following parameters may be changed:<br/>
- OBSERVE: number of observe timesteps, used to populate replay memory
- EXPLORE: number of explore timesteps
- FINAL\_EPSILON: final epsilon
- INITIAL\_EPSILON: starting epsilon, rate of a random action being chosen
- REPLAY\_MEMORY: replay memory of past games
- BATCH: batch size pulled from replay memory
- LR: learning rate
