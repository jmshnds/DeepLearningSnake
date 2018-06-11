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
Modify FPS settings in `gamestate.py` as needed. I found that when testing on multiple computers this made a significant difference in terms of training time. On one computer I was only able to train at about ~10 FPS but with another computer I was able to train at about ~60 FPS. <br/>
In `pysnake.py` the following parameters may be changed:<br/>
- OBSERVE: number of observe timesteps, used to populate replay memory. To train from scratch OBSERVE was initially set to 10,000. Then once a checkpoint of ~1 million timesteps was acheived to continue training this was set to 50,000. 
- EXPLORE: number of explore timesteps
- FINAL\_EPSILON: final epsilon. This value was set to 0.1 as in the original DQN paper. 
- INITIAL\_EPSILON: starting epsilon, rate of a random action being chosen. To train from scratch this was initially set to 1. Then once a checkpoint of ~1 million timesteps was acheived to continue training this was set to 0.1. 
- REPLAY\_MEMORY: replay memory of past games. Similar to the FlappyBird example, this was set to 50,000 rather than 1 million. 
- BATCH: batch size pulled from replay memory
- LR: learning rate. This was set to 0.00025 as it was in the original DQN paper, rather than 1e-6 as was used in the FlappyBird example. 

Run program with `pysnake.py`<br/>

## Results
After training for about 1,000,000 timesteps I found that the Snake tended to prefer going straight over time. 
This is due to the fact that turning a lot causes the snake to crash into its own tail and receive a reward of -1. 
The snake would receive 0 reward for doing nothing and +1 reward for eating a food pellet.
I thought that this reward setup would help push the snake to prefer going after food pellets. 
I changed the "do-nothing" reward that was set to 0.1 in the FlappyBird example to just 0 to help the snake further prefer food pellets. 

The following chart shows the score results after training for about 1,000,000+ timesteps. This chart tracks the average score over 100 consecutive games for 4700 games during the initial training phase. As shown below, the score begins to significantly improve toward the end of the chart. 

![chart for average score](https://github.com/jmshnds/DeepLearningSnake/blob/master/Images/scores_100avg_1mil.png)
