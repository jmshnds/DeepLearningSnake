# DeepLearningSnake
Deep Learning in classic Snake game.<br/>
DQN and concept based off of DeepLearningFlappyBird by yenchenlin: https://github.com/yenchenlin/DeepLearningFlappyBird <br/>
Snake game made using Pygame, based on: https://github.com/jmshnds/PySnake <br/>

I based this project heavily off of what was already designed in the DeepLearningFlappyBird program. 
I made a simple Snake game and adapted it to fit with the deep learning algorithm. 
I tweaked some of the parameters that were set to optimize performance in FlappyBird to follow some of the parameters set in the original DQN paper: https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf <br/>
Some of these changes include changing the learning rate and epsilon values. 

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
<br/>
Run program with `pysnake.py`<br/>

## Results
After training for about 1,000,000 timesteps I found that the Snake tended to prefer going straight over time. 
This is due to the fact that turning a lot causes the snake to crash into its own tail and receive a reward of -1. 
The snake would receive 0 reward for doing nothing and +1 reward for eating a food pellet.
I thought that this reward setup would help push the snake to prefer going after food pellets. 
I changed the "do-nothing" reward that was set to 0.1 in the FlappyBird example to just 0 to help the snake further prefer food pellets. 

