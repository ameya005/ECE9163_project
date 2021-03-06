## ECE 9163 Project

**Team:** Ameya Joshi, Ayush Kumar, Anand Sabulal, Abhishek Hotkar

To run our detection framework, you need access to the following data: [Data Link](https://drive.google.com/drive/folders/13o2ybRJ1BkGUvfmQEeZqDo1kskyFywab).

Latest models can be found at: [Drive Link](https://drive.google.com/drive/folders/10vYzf88UiC4cLTAsg5Uqy04HdZn8XJo3?usp=sharing)

The results are provided below:

  |  Model | Trigger | Clean Test Accuracy (\%) | Poisoned Data Accuracy (\%) |
   | --- | --- | --- | --- |
   | Sunglasses Ensemble | Sunglasses | 79.82 | 98.61 |
   |Multi-target Ensemble} | Sunglasses | 80.91 | 99.99 |
   | - | Eyebrows | | 92.60 |
   | - | Lipstick | | 93.59 |
   | Anonymous 1 Ensemble | Unknown | 77.13 | 93.68 |
   | Anonymous 2 Ensemble | Unknown | 79.74 | - |



The detector script outputs a numpy file with labels from ```[0, 1283]```, where ```1283``` is the label for a backdoored image. 

To run the detector, use:
```
python3 detect_backdoor.py <args>
```
Arguments:
```
  -h, --help            show this help message and exit
  --orig ORIG, -og ORIG
                        Path to original (backdoored) model
  --pruned PRUNED, -pr PRUNED
                        Path to Pruned model. Generate a pruned model using fine_prune.py
  --dset DSET, -ds DSET
                        Path to dataset
  --outpath OUTPATH, -o OUTPATH
                        File to store output labels
```


For example, to test it on clean_test data, use:

```
python detect_backdoor.py -og models/anonymous_bd_net.h5 -ds data/clean_test.h5 -pr models/anonymous_bd_net_repaired.h5
```


And to test it on anoynmous poisoned data, use:

```
python detect_backdoor.py -og models/anonymous_bd_net.h5 -ds data/anonymous_1_poisoned_data.h5 -pr models/anonymous_bd_net_repaired.h5
```

For individual images, use the respective evaluation scripts provided as follows:

```
python3 eval_sunglasses.py <imgpath>
```