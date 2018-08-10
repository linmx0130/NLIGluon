# NLIGluon
Natural language inference models in Gluon.

## Usage
Put SNLI dataset into `data/`, then train the model with

> python3 main.py


When a model is trained and dumped into `checkpoints/`, test it with:

> python3 main.py --mode test --model checkpoints/epoch-xx.gluonmodel


## Files
* `main.py`: entrance of the program
* `main_intra.py`: entrance of the program to train/test models with intra-sentence attention.
* `decomposable_atten.py`: the implementaion of decomposable attention.
* `utils.py`: some utility functions
* `nlidataset.py`: parse NLI datasets like SNLI.

## Contact
Mengxiao Lin <linmx0130@gmail.com>
