ECE 9163 Project

Team: Ameya Joshi, Ayush Kumar, Anand Sabulal, Abhishek Hotkar

To run our detection framework, you need access to the following data: [link](https://drive.google.com/drive/folders/13o2ybRJ1BkGUvfmQEeZqDo1kskyFywab).

The repaired models are stored in ```models/```.

For the sunglasses badnet, use ```models/multi_trigger_multi_target_bd_net.h5```.

For the anonymous badnet, use  ```models/***.h5```.

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

To test it on anoynmous poisoned data, use:

```
python detect_backdoor.py -og models/anonymous_bd_net.h5 -ds data/anonymous_1_poisoned_data.h5 -pr models/anonymous_bd_net_repaired.h5
```
