## To Do

- Gesture manager
    > Manages the stored data for each gesture. Allow to add, delete, replace, or append. Basically CRUD?
- Event daemon
    > Runs in the background, constantly piping EMG data from myo into a classifier, and performing appropriate events.
- Bug: myo sometimes doesn't connect
- Bug: sometimes, data is not collected to lists

## Doing

- Classifier
    > Train a decent classifier. Perhaps, one way of testing how it'll work is by training on individual finger movements
    * [ ] Try old school ML
    * [ ] Try a NN
    * [ ] GPU accelerate option

## Done

- Read raw EMG from myo
- collect data from myo while displaying a countdown
- Full one-gesture pipeline
    > i.e., ask for gesture name, lead user through instructions, and save the file. Perhaps serialize as json? then the classifier reads the json. Okay for few gestures and not many training points.
